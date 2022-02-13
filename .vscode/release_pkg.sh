#!/bin/sh

cd $1
rm -rf $1/test_package/build/*
conan create -pr:b=default -s build_type=Release . --build=missing
