import time
import unittest
from aio_executor import AioExecutor, run_with_asyncio


async def _func(*args):
    return 'ret:' + ','.join([str(arg) for arg in args])


class TestAioExecutor(unittest.TestCase):
    def test_submit(self):
        aioexec = AioExecutor()
        fut1 = aioexec.submit(_func, 'foo', 'bar')
        fut2 = aioexec.submit(_func, 1)
        fut3 = aioexec.submit(_func)
        self.assertEqual(fut1.result(), 'ret:foo,bar')
        self.assertEqual(fut2.result(), 'ret:1')
        self.assertEqual(fut3.result(), 'ret:')
        self.assertFalse(aioexec._shutdown)
        self.assertTrue(aioexec._thread.is_alive())
        aioexec.shutdown()
        self.assertTrue(aioexec._shutdown)
        self.assertFalse(aioexec._thread.is_alive())

    def test_with_submit(self):
        with AioExecutor() as aioexec:
            fut1 = aioexec.submit(_func, 'foo', 'bar')
            fut2 = aioexec.submit(_func, 1)
            fut3 = aioexec.submit(_func)
        self.assertEqual(fut1.result(), 'ret:foo,bar')
        self.assertEqual(fut2.result(), 'ret:1')
        self.assertEqual(fut3.result(), 'ret:')
        self.assertTrue(aioexec._shutdown)
        self.assertFalse(aioexec._thread.is_alive())

    def test_shutdown(self):
        aioexec = AioExecutor()
        aioexec.shutdown(wait=False)
        self.assertTrue(aioexec._shutdown)
        while aioexec._thread.is_alive():
            time.sleep(0.1)
        self.assertRaises(RuntimeError, aioexec.submit, _func)

    def test_map(self):
        with AioExecutor() as aioexec:
            ret = aioexec.map(_func, ['foo', 'bar'], [1, 2])
            self.assertEqual(list(ret), ['ret:foo,1', 'ret:bar,2'])


class TestRunWithAsyncioDecorator(unittest.TestCase):
    def test_run_with_asyncio_decorator(self):
        f = run_with_asyncio(_func)
        g = run_with_asyncio(_func)
        self.assertNotEqual(f, g)
        self.assertEqual(f('foo', 'bar'), 'ret:foo,bar')
        self.assertEqual(g('foo', 'bar'), 'ret:foo,bar')
        self.assertEqual(f(1), 'ret:1')
        self.assertEqual(g(1), 'ret:1')
        self.assertEqual(f(), 'ret:')
        self.assertEqual(g(), 'ret:')


if __name__ == '__main__':
    unittest.main()
