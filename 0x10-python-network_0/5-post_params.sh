#!/bin/bash
# send a post request and customized data
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
