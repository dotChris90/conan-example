#!/bin/sh

cd $1
rm -rf $1/test_package/build/*
conan create -pr:b=default -s build_type=Debug . --build=missing

ln -s $(find $1/test_package/build/ -name 'pkg_test') $1/test_package/build/pkg_test