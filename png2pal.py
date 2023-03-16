from PIL import Image
import struct
import sys

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} input_file output_file")
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]

try:
    with Image.open(input_filename) as im:
        palette = im.getpalette()
        # convert palette from RGB to RGB555le format
        palette = [((r >> 3) << 10) | ((g >> 3) << 5) | (b >> 3) for r, g, b in zip(palette[::3], palette[1::3], palette[2::3])]
        # export palette as binary file
        with open(output_filename, "wb") as f:
            for rgb15 in palette:
                f.write(struct.pack("<H", rgb15))
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

sys.exit(0)
