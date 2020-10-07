#!/bin/bash

# create virtualenv
virtualenv venv

# activate virtualenv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

