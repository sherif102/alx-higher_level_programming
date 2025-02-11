#!/bin/bash
# send request to url and display only the status code
# `curl -sI "$1" | grep HTTP | cut -d " " -f 2` <- piping solution
curl -sI -o /null -w "%{http_code}" "$1"
