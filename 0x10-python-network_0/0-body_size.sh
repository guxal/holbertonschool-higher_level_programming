#!/bin/bash
# This script use curl
curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}'
