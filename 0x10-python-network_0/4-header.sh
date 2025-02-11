#!/bin/bash
# sends customized request to the server with GET
curl -X GET -d "X-School-User-Id=98" "$1"
