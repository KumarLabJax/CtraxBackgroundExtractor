# CtraxBackgroundExtracter
Extracts the background image binary from Ctrax's annotation file.

Requirements:
Uses the following python libraries: re, numpy, Image, sys, getopt

Usage:
python CtraxExportBG.py -i "inputannfile" -o "backgroundoutput" -h "imageheight"

This will search and export the background median image from an annotation file.
It is designed to work AFTER the background model has been initialized into the annotation file.
This was first built to work with Ctrax V 0.5.6.
