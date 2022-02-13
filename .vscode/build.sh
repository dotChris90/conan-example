#!/bin/sh

rm -rf $1/build 
rm -rf $1/cmake-build-$3
mkdir -p $1/build
cd $1/build
conan install -pr:b=default -s build_type=$2 .. --build=missing
conan build ..