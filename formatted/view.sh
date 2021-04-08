#!/bin/bash
FILE=$1
FILE_NO_EXT="${FILE%%.*}"
lilypond $1 && zathura $FILE_NO_EXT.pdf
