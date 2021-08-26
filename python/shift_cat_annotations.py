
'''
shift_cat_annotations.py 
'''

import sys
import os
import subprocess
import gzip

from utils import *

if len(sys.argv) != 3:

	print("Usage: python shift_cat_annotations.py <annotation_gff3_gz_name> <output_gff3_gz_name>\n")
	sys.exit(1)

printScriptHeader()

annotation_file = gzip.open(sys.argv[1], "rb")
out_file = gzip.open(sys.argv[2], "wb")

for line in annotation_file:

	if line[0] == "#":

		out_file.write(line)
		continue

	line_split = line.split("\t")

	if "_sub_" in line_split[0]:

		contig_split = line_split[0].split("_")

		assert(len(contig_split) == 4)
		assert(contig_split[1] == "sub")

		contig_split[2] = int(contig_split[2])
		contig_split[3] = int(contig_split[3])

		line_split[3] = int(line_split[3])
		line_split[4] = int(line_split[4])

		line_split[0] = contig_split[0]

		line_split[3] += contig_split[2]
		line_split[4] += contig_split[2]

		assert(line_split[4] <= contig_split[3])

		line_split[3] = str(line_split[3])
		line_split[4] = str(line_split[4])

		out_file.write("\t".join(line_split));

	else:

		out_file.write(line);

annotation_file.close()
out_file.close()

print("Done")
