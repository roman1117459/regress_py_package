# Regression Evaluation Package 

[![image](https://img.shields.io/pypi/v/py-package-template.svg)](#)
[![Build Status](https://travis-ci.org/AlexIoannides/py-package-template.svg?branch=master)](#)

The regress_py package allows users to download the contents of this [GiHub repository](https://github.com/roman1117459/regress_py_package),  containing a Regression Evaluating Python package project to be used as a gradient descent, loss and regression problem for kick-starting Machine learning or Deep Learning algorithm model evaluation of **any** type of Package; destined for upload to just for local install using Pip. The downloaded package includes the following components to measure or evalute the loss or any kind of measurement without having to spend time cloning existing set-ups from other projects:

- a minimal `setup.py` file;
- testing with PyTest;
- Evaluate the gradient descent loss and info; 

A description of how to work with (and modify) each of these components, is provided in more detail in the sections that follow-on below, as well as in the documentation and within the example code bundled with the package.

This is obviously a opinionated view of how a Python package project ought to be structured, based largely on my own experiences and requirements.

## Installing

Install and update using [pip](https://pip.pypa.io/en/stable/quickstart/):

```bash
pip3 install regresspy
```

## Downloading a regress_py package

To down load the latest version of this project located in [this GiHub repository](https://github.com/roman1117459/regress_py_package), execute the following command from the command line:

```bash
pip install regresspy
```

This will be downloaded to the current directory and will contain the following directory structure:

```bash
regress_py_package/

 |-- regresspy/
 |-- |-- __init__.py
 |-- |-- gradient_descent.py
 |-- |-- loss.py
 |-- |-- regression.py
 |-- test/
 |-- |   __init__.py
 |-- |   model.py
 |-- |   test.py
 |-- .idea
 |-- .gitignore
 |-- License
 |-- README.md
 |-- requirements.txt
 |-- setup.py
```


