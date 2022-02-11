# strip-hidden-form-values

[![PyPI](https://img.shields.io/pypi/v/strip-hidden-form-values.svg)](https://pypi.org/project/strip-hidden-form-values/)
[![Changelog](https://img.shields.io/github/v/release/simonw/strip-hidden-form-values?include_prereleases&label=changelog)](https://github.com/simonw/strip-hidden-form-values/releases)
[![Tests](https://github.com/simonw/strip-hidden-form-values/workflows/Test/badge.svg)](https://github.com/simonw/strip-hidden-form-values/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/strip-hidden-form-values/blob/master/LICENSE)

CLI tool for stripping hidden form values from an HTML document

## Installation

Install this tool using `pip`:

    $ pip install strip-hidden-form-values

## Usage

Usage instructions go here.

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd strip-hidden-form-values
    python -m venv venv
    source venv/bin/activate

Or if you are using `pipenv`:

    pipenv shell

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
