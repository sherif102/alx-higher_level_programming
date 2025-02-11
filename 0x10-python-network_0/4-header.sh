#!/bin/bash
# sends customized request to the server with GET
curl -sX GET -d "X-School-User-Id=98" "$1"
