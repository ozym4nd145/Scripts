#!/bin/bash
if [ $# -lt 2 ]
  then
    echo "Usage: <script> <pad-name> <filepath>"
fi

curl -X POST --data-binary @$2 -H "X-PAD-ID: $1" https://pad.devclub.in/post
