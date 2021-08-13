# Python Package Template Project

[![image](https://img.shields.io/pypi/v/py-package-template.svg)](#)
[![Build Status](https://travis-ci.org/AlexIoannides/py-package-template.svg?branch=master)](#)

The py-template-project package allows users to download the contents of this [GiHub repository](https://github.com/AlexIoannides/py-package-template),  containing a skeleton Python package project to be used as a template for kick-starting development of **any** type of Package; destined for upload to PyPI, or just for local install using Pip. The downloaded package includes the following components to aid rapid development without having to spend time cloning existing set-ups from other projects:

- a minimal `setup.py` file;
- testing with PyTest;
- documentation (HTML and PDF) generated using Sphinx with auto-documentation setup; 
- an entry-point that allows the package to execute functions directly from the command line - e.g. to start a server, interact with a user, download a GitHub repository, etc.; and,
- automated testing and deployment using Travis CI.

A description of how to work with (and modify) each of these components, is provided in more detail in the sections that follow-on below, as well as in the documentation and within the example code bundled with the package.

This is obviously a opinionated view of how a Python package project ought to be structured, based largely on my own experiences and requirements. Where I have needed guidance on this subject, I have leant heavily on the advice given by the [Python Packaging Authority (PyPA)](https://packaging.python.org/guides/distributing-packages-using-setuptools/) and used the excellent [Requests](https://github.com/requests/requests) and [Flask](https://github.com/pallets/flask) projects as references for 'best practices'.

## Installing

Install and update using [pip](https://pip.pypa.io/en/stable/quickstart/):

```bash
pip3 install py-template-project
```

## Downloading a Python Package Template Project

To down load the latest version of the Python Package Template project located in [this GiHub repository](https://github.com/AlexIoannides/py-package-template), execute the following command from the command line:

```bash
py-package-template install
```

This will be downloaded to the current directory and will contain the following directory structure:

```bash
py-package-tempate/
 |-- docs/
 |-- |-- build_html/
 |-- |-- build_latex/
 |-- |-- source/
 |-- py-pkg/
 |-- |-- __init__.py
 |-- |-- __version__.py
 |-- |-- curves.py
 |-- |-- entry_points.py
 |-- tests/
 |-- |-- test_data/
 |-- |   |-- supply_demand_data.json
 |-- |   __init__.py
 |-- |   conftest.py
 |-- |   test_curves.py
 |-- .env
 |-- .gitignore
 |-- Pipfile
 |-- Pipfile.lock
 |-- README.md
 |-- setup.py
```


