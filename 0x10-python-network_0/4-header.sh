#!/bin/bash
# Sends a request to a URL, and displays the body of the response
curl -s -X GET -H "X-School-User-Id: 98" "$1"
