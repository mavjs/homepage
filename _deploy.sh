#!/bin/sh
mynt=$(which mynt)

mynt gen -f . _site/ && rsync -rupazv _site/ searxgs:~/mavjs.org/
