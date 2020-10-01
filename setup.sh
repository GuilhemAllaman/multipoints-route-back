#!/bin/bash

# create virutalenv
virtualenv .env

# activate virtualenv
source .env/bin/activate

# install dependencies
pip install -r requirements.txt

