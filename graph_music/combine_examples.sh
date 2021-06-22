#!/bin/bash
rm whole_examples.png
convert $(ls  *example.png | sort -V) -append whole_examples.png
