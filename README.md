# GraphQL-core

GraphQL for Python

[![PyPI version](https://badge.fury.io/py/graphql-core.svg)](https://badge.fury.io/py/graphql-core)
[![Build Status](https://travis-ci.org/graphql-python/graphql-core.svg?branch=master)](https://travis-ci.org/graphql-python/graphql-core)
[![Coverage Status](https://coveralls.io/repos/graphql-python/graphql-core/badge.svg?branch=master&service=github)](https://coveralls.io/github/graphql-python/graphql-core?branch=master)
[![Public Slack Discussion](https://graphql-slack.herokuapp.com/badge.svg)](https://graphql-slack.herokuapp.com/)


## Project Status

This library is a port of [graphql-js](https://github.com/graphql/graphql-js) to Python.

We are currently targeting feature parity with `v0.4.14` of the reference implementation, and are currently on `v0.4.13`.

Please see [issues](https://github.com/graphql-python/graphql-core/issues) for the progress.

## Getting Started

An overview of the GraphQL language is available in the 
[README](https://github.com/facebook/graphql/blob/master/README.md) for the
[Specification for GraphQL](https://github.com/facebook/graphql). 
The overview describes a simple set of GraphQL examples that exist as [tests](tests/core_starwars)
in this repository. A good way to get started is to walk through that README and the corresponding tests
in parallel. 

### Using `graphql-core`

Install from pip:

```sh
pip install graphql-core
```

### Supported Python Versions
`graphql-core` supports the following Python versions:
 
* `2.7.x`
* `3.3.x`
* `3.4.x`
* `3.5.0`
* `pypy-2.6.1`

### Built-in Concurrency Support
Support for `3.5.0`'s `asyncio` module for concurrent execution is available via an executor middleware at 
`graphql.core.execution.middlewares.asyncio.AsyncioExecutionMiddleware`.

Additionally, support for `gevent` is available via 
`graphql.core.execution.middlewares.gevent.GeventExecutionMiddleware`.

Otherwise, by default, the executor will use execute with no concurrency.

## Main Contributors

 * [@syrusakbary](https://github.com/syrusakbary/)
 * [@jhgg](https://github.com/jhgg/)
 * [@dittos](https://github.com/dittos/)

## License

[MIT License](https://github.com/graphql-python/graphql-core/blob/master/LICENSE)
