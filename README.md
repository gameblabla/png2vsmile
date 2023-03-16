V.Smile PNG to 8bpp raw buffer
==============================

This is provided as a set of python scripts to convert both the palette and image to formats
that the V.Smile can accept.
The palette is RGB555 little endian.

Usage
======

This assumes you are on a Linux system.
Simply run the script file
```sh
./convert_png.sh mypng.png
```

And it will output both the palette and raw buffer as binaries in the folder relative
to the bash script.

Other color modes
==================

For Hicolor mode, it pretty much just expects a raw RGB555le buffer.
Run
```
ffmpeg -i mypng.png -c:v rawvideo -pix_fmt rgb555le png.rgb
```
And you will get your file working.
