import asyncio
from concurrent.futures import Executor
from functools import wraps
from threading import Thread


class AioExecutor(Executor):
    """A concurrent.futures.Executor implementation that runs asynchronous
    tasks in an asyncio event loop. Example usage::

        from aio_executor import AioExecutor

        async def my_async_function(arg):
            # ...

        with AioExecutor() as aioexec:
            aioexec.submit(my_async_function, 'foo')
            aioexec.map(my_async_function, ['foo', 'bar', 'baz'])

    :param loop: (optional) An existing event loop to be used by the executor.
                 A new event loop is created when this argument isn't given.
    """
    def __init__(self, loop=None):
        self.loop = loop or asyncio.new_event_loop()
        self._shutdown = False
        self._thread = Thread(target=self._aiothread)
        self._thread.daemon = True
        self._thread.start()

    def submit(self, fn, *args, **kwargs):
        if self._shutdown:
            raise RuntimeError('cannot schedule new futures after shutdown')
        return asyncio.run_coroutine_threadsafe(fn(*args, **kwargs), self.loop)

    def shutdown(self, wait=True):
        self._shutdown = True
        self.loop.call_soon_threadsafe(self.loop.stop)
        if wait:
            self._thread.join()

    def _aiothread(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()
        pending = asyncio.all_tasks(loop=self.loop)
        self.loop.run_until_complete(asyncio.gather(*pending))
        self.loop.close()


def run_with_asyncio(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        fut = run_with_asyncio.aio_executor.submit(f, *args, **kwargs)
        return fut.result()

    if getattr(run_with_asyncio, 'aio_executor', None) is None:
        run_with_asyncio.aio_executor = AioExecutor()
    return wrapped
