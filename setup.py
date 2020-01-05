"""
aio-executor
------------
A concurrent.futures.Executor implementation that runs asynchronous tasks in
an asyncio event loop.
"""
from setuptools import setup


with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='aio-executor',
    version='0.2.0',
    url='http://github.com/miguelgrinberg/aio-executor/',
    license='MIT',
    author='Miguel Grinberg',
    author_email='miguel.grinberg@gmail.com',
    description=('A concurrent.futures.Executor implementation that runs '
                 'asynchronous tasks in an asyncio event loop.'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['aio_executor'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    python_requires='>=3.7',
    install_requires=[],
    test_suite='test_aio_executor',
    classifiers=[
        'Framework :: AsyncIO',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
