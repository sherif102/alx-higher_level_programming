#!/bin/bash
# takes in a url and get the body size of the response
curl -s "$1" | wc -c
