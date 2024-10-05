#!/bin/sh

# Create symbolic link based on the environment variable
ln -sf file-$ENVIRONMENT.txt file.txt

# Start the Go server
exec ./server
