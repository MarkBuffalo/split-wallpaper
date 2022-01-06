#!/usr/bin/env python3

# pip3 install image-slicer
# Usage: ./split.py wallpaper.jpg rows cols
# Example: ./split.py wallpaper.jpg 2 4
# ^-- This will split the wallpaper evenly by 8. Say, you have 4 columns (4 monitors) on top, and 2 rows which means 4 more on the bottom.

# This is UGLY. Quick and dirty script with zero error checking. 

import image_slicer
import sys
import os
 
wallpaper = sys.argv[1]
 
rows = int(sys.argv[2])
cols = int(sys.argv[3])
 
image_slicer.slice(wallpaper, row=rows, col=cols)
