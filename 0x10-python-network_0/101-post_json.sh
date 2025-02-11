#!/bin/bash
# sends json post request to url
curl -sX POST --json @"$2" "$1"
