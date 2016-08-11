import re
import numpy as np
import Image
import sys
import getopt

def main(argv):
	# Default arguments
	inputfilename = 'movie.avi.ann'
	height = 480
	outputfile = 'movie_background.png'
	# Try to import the arguments
	try:
		opts, args = getopt.getopt(argv,"i:o:h:",["ifile=","ofile=","height="])
	except getopt.GetoptError:
		print 'CtraxExportBG.py -i <inputannfile> -o <backgroundoutput> -h <imageheight>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '--help':
			print 'CtraxExportBG.py -i <inputannfile> -o <backgroundoutput> -h <imageheight>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfilename = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
		elif opt in ("-h", "--height"):
			height = int(arg)
	# Open file in read mode
	annfile = open(inputfilename, 'r')
	contents = annfile.read()
	# Search for the header line
	medianlabelloc = re.search("background median:([0-9]*)", contents)
	# Extract number of bytes that is used to store the image
	numbytes = int(medianlabelloc.group(1))
	# Pull out the bytes from the file
	rawbytes = contents[medianlabelloc.end(1)+1:medianlabelloc.end(1)+1+numbytes]
	# Convert the bytes to a float vector
	image=np.fromstring(rawbytes,np.float64)
	# Reshape the vector into the image matrix
	width=len(image)/height
	image=image.reshape((height,width))
	# Explort the image as an 8-bit int
	im=Image.fromarray(image.astype(np.uint8))
	im.save(outputfile)

if __name__ == "__main__":
	main(sys.argv[1:])
