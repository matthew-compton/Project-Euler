#!/bin/bash
# This script just creates a bunch of folders because I like organization

# Make the base problem directory
mkdir "Problems"

# Create directory for each problem
for i in {1..434}
do
   mkdir "Problems/$i"
done