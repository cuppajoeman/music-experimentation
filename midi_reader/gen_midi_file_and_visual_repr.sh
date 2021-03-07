#!/bin/bash

# 1: file name
# 2: key 

MIDIFILE=$(basename -- "$1")
KEY=$2

python3 parse.py $MIDIFILE $2

NE="${MIDIFILE%.*}"

mkdir $NE

mv $NE[0-9].* $NE
mv $NE[0-9][0-9].* $NE
mv $NE.* $NE

#feh -F $NE/$NE[0-9].jpg &

timidity $1
