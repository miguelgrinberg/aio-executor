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
    aioexec.submit(my_async_function, 'foo')

    # multiple concurrent invocations using "map"
    aioexec.map(my_async_function, ['foo', 'bar', 'baz'])
```
