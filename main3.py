import os
import csv
from trdg.generators import GeneratorFromStrings
from tqdm import tqdm

# Define the path to the Unicode text file
text_file = 'si.txt'

# Define the path to the font file
font_files = ['FMRashmee.ttf', 'FMAbhaya.ttf', 'FMMalithi.ttf', 'FMBindumathi.ttf']

# Read the Unicode text file and create a list of strings
with open(text_file, 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file]
    print('Total lines ', len(lines))

# Define the generator with larger image size and specified font
generator = GeneratorFromStrings(
    lines,
    count=len(lines),
    blur=3,
    random_blur=True,
    size=256,
    fonts=font_files
)

# Create "out" folder if it does not exist
if not os.path.exists('out'):
    os.makedirs('out')

# Open a CSV file for writing
with open('out.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Filename', 'Text'])

    # Generate images from the list of strings
    with tqdm(total=len(lines), dynamic_ncols=True, unit='file') as progress_bar:
        for i, (img, txt) in enumerate(generator):
            # Generate an image and save it with a numbered filename
            print(i)
            if img is not None:
                filename = f'{i+1}.jpg'
                img.save(os.path.join('out', filename))

                # Write the filename and text to the CSV file
                csvwriter.writerow([filename, txt])

            progress_bar.update(1)
