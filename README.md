# aio-executor

[![Build Status](https://travis-ci.org/miguelgrinberg/aio-executor.svg?branch=master)](https://travis-ci.org/miguelgrinberg/aio-executor)

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
