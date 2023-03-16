#!/bin/bash

# Check if the input file name is specified
if [ -z "$1" ]
  then
    echo "Usage: $0 input_file"
    exit 1
fi

convert "$1" -colors 256 -depth 8 temp.png
python png2pal.py temp.png palette_8bit.bin
python png2file.py temp.png image_8bit.bin
rm temp.png
