#!/bin/sh

set -e

docker login -u pooriazmn -p CVNdDcASqE4G6Qa
kopf run /crud_operator.py --standalone --all-namespaces
