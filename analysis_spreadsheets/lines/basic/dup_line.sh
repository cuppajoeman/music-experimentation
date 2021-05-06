#!/bin/bash
# Takes the file to be duplicated as an argument

file=''

print_usage() {
  printf "Usage: dup_line -f <dup_file> \n"
}

while getopts 'hf:v' flag; do
  case "${flag}" in
    f) file="${OPTARG}" ;;
    h) print_usage
       exit 1 ;;
    *) exit 1 ;;
  esac
done


FILE=$(mktemp line_XXX.sc)
cat $file > $FILE
sc-im $FILE

