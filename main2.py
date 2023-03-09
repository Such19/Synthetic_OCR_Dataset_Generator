import os
from trdg.generators import GeneratorFromStrings

# Define the Unicode strings to use for generating images
unicode_strings = [
    u'Hello',
    u"ke;akï úYajh ms,snoj lrk .fõYKfhka ,nd.kakd oekquhs' úoHd;aul oekqu /ia lsÍfïÈ ms,smÈkafka úoHd;aul l%uhhs'",
]

# Define the path to the font file
font_files = ['FMRashmee.ttf', 'FMAbhaya.ttf', 'FMMalithi.ttf']

# Define the generator with larger image size and specified font
generator = GeneratorFromStrings(
    unicode_strings,
    count=100,
    blur=2,
    random_blur=True,
    size=256,
    fonts=font_files
)

# Create "out" folder if it does not exist
if not os.path.exists('out'):
    os.makedirs('out')

# Generate the images and save them to disk
for img, txt in generator:
    if img is not None:
        img.save(os.path.join('out', f'{txt}.jpg'))
