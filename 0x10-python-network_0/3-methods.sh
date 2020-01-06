#!/bin/bash
# This script use curl
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
