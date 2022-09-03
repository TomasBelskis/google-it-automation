#!/usr/bin/env python3
import os, sys
from PIL import Image

path_to_images = '/Users/tomasbelskis/Developer/Personal/google-it-automation/module-1-project/images/'
dir_list = os.listdir(path_to_images)
output_path = '/Users/tomasbelskis/Developer/Personal/google-it-automation/module-1-project/'
output_dir = 'converted-images'
path_to_output = os.path.join(output_path, output_dir)
if not os.path.isdir(path_to_output):
    os.mkdir(path_to_output)
for f in dir_list:
    # Ignore hidden directories & files
    if not f.startswith('.'):
        outfile = f + ".jpeg"
        if f != outfile:
            try:
                with Image.open(path_to_images + f)as im:
                    # Convert LA to RGB for JPEG format 
                    rgb_im = im.convert('RGB')
                    # Rotate anti clockwise
                    rgb_im_rotated = rgb_im.rotate(-90)
                    # Resize to to correct resolution
                    im_final = rgb_im_rotated.resize((128, 128))
                    # Write converted images to output dir
                    im_final.save(path_to_output + '/' + outfile)
                    print("saved converted image at " + path_to_output + '/' + outfile)
            except OSError:
                print("cannot covert",  path_to_images + f)
