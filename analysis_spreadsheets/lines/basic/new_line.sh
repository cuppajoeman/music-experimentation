#!/bin/bash
FILE=$(mktemp line_XXX.sc)
cat base.sc > $FILE
sc-im $FILE

