#!/bin/bash
# This script use curl
curl -X POST -H "Content-Type: application/json" -d @./"$2" "$1"
