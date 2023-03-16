import sys
from PIL import Image

# Check that the correct number of arguments were provided
if len(sys.argv) != 3:
    print("Usage: python script.py input.png output.bin")
    sys.exit(1)

# Extract the input and output file names from the command line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Open the input PNG image file
img = Image.open(input_file)

# Get the custom color palette from the PNG image
palette = img.getpalette()
palette = [(palette[i], palette[i+1], palette[i+2]) for i in range(0, len(palette), 3)]

# Convert the image to indexed color mode using the custom palette
img = img.convert("P", palette=palette)

# Iterate through each pixel in the image and append the corresponding palette index to the output binary data
data = bytearray()
for y in range(img.size[1]):
    for x in range(img.size[0]):
        palette_index = img.getpixel((x, y))
        data.append(palette_index)

# Write the data to the output binary file
with open(output_file, "wb") as f:
    f.write(data)
