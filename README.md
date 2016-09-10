# CtraxBackgroundExtractor
Extracts the background image binary from Ctrax's annotation file.

Requirements:
Uses the following python libraries: re, numpy, Image, sys, getopt

Usage:
python CtraxExportBG.py -i "inputannfile" -o "backgroundoutput" -h "imageheight"

Issues:
If height does not match the actual value, either the program will either crash or produce a nonsense image.
If the header handle does not exist, I'm not sure what the program will do... See ToDo below.
As with Ctrax, this script must have enough available memory to load the entire file into memeory at once. Annotation files are normally on the order of 12Mb, so this is normall not an issue.

ToDo:
Add in detection of available header handles. According to a comment in the Ctrax source, all possible values include: "background median", "med", "background mean", "mean", "background center", "center", "background mad", "mad", "background std", "std", "background dev", "dev", "fracframesisback", "isarena", "hfnorm".

This will search and export the background median image from an annotation file.
It is designed to work AFTER the background model has been initialized into the annotation file.
This was first built to work with Ctrax V 0.5.6.
