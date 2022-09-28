#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --in-place msaServer docs_src --exclude=__init__.py
black msaServer docs_src
isort msaServer docs_src
