#!/bin/sh

mkdir -p $1/build
cd $1/build
conan install -pr:b=default -g deploy .. 
conan install -pr:b=default -g deploy ../test_package/
python3 $1/.vscode/prepare_header.py

