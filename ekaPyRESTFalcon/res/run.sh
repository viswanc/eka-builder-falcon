#!/bin/bash

cd "$(dirname $0)/src"
gunicorn main:api
