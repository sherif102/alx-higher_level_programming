#!/bin/bash
# gets all the http methods the server will acept
curl -I "$1" | grep -i "allow:" | cut -d " " -f 2-
