#!/bin/bash
# sends json post request to url
curl -s -H "Content-Type: application/json" --json @"$2" "$1"
