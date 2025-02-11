#!/bin/bash
# send request to url and display only the status code
curl -sI -o /null -w "%{http_code}" "$1"
