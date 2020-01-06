#!/usr/bin/env bash
# This script use curl
curl -so /dev/null "$1" -w '%{size_download}'
echo ""
