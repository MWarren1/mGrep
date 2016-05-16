############################# 
##         mGrep           ## 
##      Python 2.7         ## 
##   By Redemption.Man     ## 
############################# 
######
# a very basic version of grep. searches a all files in a folder for a string and outputs all lines that contain that folder in a txt file
######
import argparse
import os.path
from os import walk
## CLI switches
parser = argparse.ArgumentParser(prog='mGrep', description='basic version of Grep')
parser.add_argument('--search', required=True, help='string to search for(case sensative)')
parser.add_argument('--folder', help='Folder for input files FULL PATH NEEDED ENDING IN \\')

args = parser.parse_args()
searchterm = args.search
folder = args.folder
## END of CLI switches

## create and open output file
output = open("mGrep-Output.txt", 'w+')
output.write("##########################################################\n")
output.write("mGrep Log Searching for "+searchterm+" in "+folder+"\n")
output.write("##########################################################\n\n")
## find all files in folder and make a list
(_, _, filenames) = walk(folder).next()
totalfiles = (len(filenames) - 1)
currentfilenum = 0
resultnum = 0
print "Files to search : "+str(totalfiles)
## start of file search loop
while currentfilenum <= totalfiles:
	print "Searching in "+filenames[currentfilenum]
	currentfile = args.folder + filenames[currentfilenum]
	with open(currentfile, 'Ur') as f:
		for line in f:
			if line.find(searchterm) != -1:
				print "Entry Found!!"
				output.write(filenames[currentfilenum]+" - "+line)
				resultnum = resultnum+1
		
	f.close()
	currentfilenum = currentfilenum +1

print str(resultnum)+" Results have been found"	
## closing output
output.close()