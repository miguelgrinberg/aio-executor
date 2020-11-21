# aio-executor

[![Build status](https://github.com/miguelgrinberg/aio-executor/workflows/build/badge.svg)](https://github.com/miguelgrinberg/aio-executor/actions)

A concurrent.futures.Executor implementation that runs asynchronous tasks in an asyncio loop.

Example usage:

```python
from aio_executor import AioExecutor

async def my_async_function(arg):
    # ...

with AioExecutor() as aioexec:
    # single invocation
    f = aioexec.submit(my_async_function, 'foo')
    result = f.result()

    # multiple concurrent invocations using "map"
    results = aioexec.map(my_async_function, ['foo', 'bar', 'baz'])
```

As a convenience, a `run_with_asyncio` decorator is also provided. This
decorator runs the decorated async function in a `AioExecutor` instance.

The example below shows how to implement an async view function for the Flask
framework using this decorator:

```python
@app.route('/')
@run_with_asyncio
async def index():
    return await get_random_quote()
```

How to Install
--------------

```
pip install aio-executor
```

Other Implementations
---------------------

The idea of implementing an `Executor` instance based on asyncio is apparently
not that original. I initially attempted to register this package on PyPI as
"asyncio-executor" and found that the name was already taken.

Below is the list of fairly similar implementations I know about. If for any
reason my version does not work for you, be sure to try these others out.

- https://gist.github.com/seglberg/0b4487b57b4fd425c56ad72aba9971be
- https://github.com/Python-Tools/asyncio-executor
- https://gist.github.com/vxgmichel/d16e66d1107a369877f6ef7e646ac2e5
