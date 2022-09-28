#!/usr/bin/env bash

set -e
set -x

mypy msaServer
flake8 msaServer docs_src
black msaServer docs_src --check
isort msaServer docs_src scripts --check-only

