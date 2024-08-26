#!/bin/bash

# Run the OpenSSL command to generate the key and certificate in the current directory

openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes



echo "key.pem and cert.pem have been created in the current directory: $(pwd)"

