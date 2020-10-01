#!/bin/bash

# create virtualenv
virtualenv .env

# activate virtualenv
source .env/bin/activate

# install dependencies
pip install -r requirements.txt

