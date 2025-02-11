#!/bin/bash
# request and print customized body response
curl -s -o /null -w "You find me!" "$1"
