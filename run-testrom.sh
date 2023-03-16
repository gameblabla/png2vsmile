#!/bin/sh
naken_asm -type bin bitmap_8bit.asm
mame vsmile -cart $PWD/out.bin
