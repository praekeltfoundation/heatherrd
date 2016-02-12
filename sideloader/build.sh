#!/bin/bash

cp -a $REPO ./build/$NAME

${PIP} install -e $REPO
