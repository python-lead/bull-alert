#!/bin/sh -e
set -x

isort --recursive  --force-single-line-imports --apply src
autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place src --exclude=__init__.py
black src
isort --recursive --apply src
flake8 src
