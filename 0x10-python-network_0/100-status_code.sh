#!/bin/bash
# This script use curl
curl -so /dev/null -w "%{http_code}" "$1"
