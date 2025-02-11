#!/bin/bash
# request and print customized body response
curl -s -o /null -w "You got me!" "$1"
