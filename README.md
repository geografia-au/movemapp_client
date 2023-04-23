# `MovemappClient` - 🐍

[![MovemappClient Tests](https://github.com/geografia-au/movemapp_client/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/geografia-au/movemapp_client/actions/workflows/tests.yml)

A Python package for Movemapp client. Allows you to interact with the Movemapp auth and data sources.

# Usage

## Pre-requisites

.env file with the following variables:

```sh
GEODB_MASTER_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
GEODB_URL=https://subdomain.geodb.host/user/username
```


```py
from movemapp_client import MovemappClient
from dotenv import load_dotenv
import os
# load .env
load_dotenv()
# fetch variables from .env
GEODB_MASTER_API_KEY = os.getenv("GEODB_MASTER_API_KEY")
GEODB_URL = os.getenv("GEODB_URL")
lga_number = 24330 # Maribyrnong

client = MovemappClient(
    geodb_master_api_key=GEODB_MASTER_API_KEY,
    geodb_url=GEODB_URL,
    lga_number=lga_number
)
# this will create a new token if it doesn't exist otherwise it will return the existing token based on the following name convention: mvmp_{lga_number}_ro
api_key = client.get("api_key")
print(api_key)
# [output]:
# {
#   'token': TEST_TOKEN,
#   'name': 'mvmp_24330_ro'
# }

```
# install
```
# in your requirements.txt
git+https://github.com/geografia-au/movemapp_client.git@main
```

Or manually:

```sh
git clone git@github.com:geografia-au/movemapp_client.git
cd movemapp_client
pip install .
```

# Development

## Install

```sh
cd movemapp_client
pip install .
```

## Test

Create the .env.test file with the following variables:

```sh
GEODB_MASTER_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
GEODB_URL=https://subdomain.geodb.host/user/username
TEST_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
Where TEST_TOKEN is a token generated for the test lga's tables. Currently only 24330 (Maribyrnong) is supported.


```sh
python -m unittest movemapp_client.tests.test_client
```

## Publish

```sh
python setup.py sdist bdist_wheel
twine upload dist/*
```
