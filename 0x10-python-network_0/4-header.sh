#!/bin/bash
# sends specific headers to servers
curl -sX GET $1 -H "X-HolbertonSchool-User-Id: 98" -L
