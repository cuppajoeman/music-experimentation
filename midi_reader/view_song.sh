#!/bin/bash

ls -1 $1*.jpg | sort -V | xargs -L1 feh -F 
