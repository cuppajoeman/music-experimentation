#!/bin/bash

MIDIFILE=$1
KEY=$2

python3 $1 $2

NE="${MIDIFILE%%.*}"

feh -F $NE.jpg

timidity $1
