#!/bin/bash
# takes in a URL, sends a get request to that URL, and displays the body of the response
curl -sX GET $1 -L
