import os
import sys
import shutil

def main():
	source = raw_input("Enter source file: ")
	#source = os.path.abspath(os.getcwd())
	destination = raw_input("Enter destination path: ")
	print "\n\n"
	print "Source file: " + source
	print "Destination path: " + destination
	print "\n"
	ch = raw_input("....continue? (Y/N)")
	if str.lower(ch) != 'y':
		print "\nProgram exited."
		sys.exit(0)

	copypp(source, destination)

def copypp(source, destination):
	source_directory = os.path.dirname(source)
	absPath = os.path.realpath(source)
	print "Source directory: " + source_directory
	print "abspath         : " + absPath

	filename = "\"" + source.split("\\")[-1] + "\""
	filename = filename.replace("\"","")
	#file_n = filename.replace(" ","_")
	print "Filename: " + filename

	split_source = source_directory.split("\\")

	split_source[0] = destination
	joined_path = os.path.join(*split_source)
	
	print "Splitting: " + str(split_source)
	print "Joined path: " + joined_path

	#jp  = "\"" + joined_path+"\\"+file_n + "\""
	#print jp
	

	os.makedirs(joined_path)
	print "Copying..."
	shutil.copy(source, joined_path)
	#print "Copied " + source + " to " + joined_path + " successfully!"
	print_str(source, joined_path)
	sys.exit(0)
		
def print_str(source, joined_path):
	print "Copied "
	print source
	print " to "
	print joined_path
	print " successfully!"


if __name__ == "__main__"	:
	main()