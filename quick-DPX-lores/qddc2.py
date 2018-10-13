import os
import sys


def main():
	source_dir = raw_input("Select dpx folder: ")

	source_dir = source_dir.replace("\"", "")

	if os.path.isdir(source_dir) == False:
		print "\nError! Selected item is not a directory. Can not continue."
		cont = raw_input("")
		sys.exit(0)


	abs_file = []

	for root, dirs, files in os.walk(source_dir):
		for file in files:
			if file.endswith(".dpx"):
				abs_file.append(os.path.join(root, file))

	#dirs = os.listdir(source_dir)
	#for file in dirs:
	#	if file.endswith(".dpx"):
	#		abs_file.append(os.path.join(source_dir, file))



	if len(abs_file) == 0:
		print "No file(s) found with extension \'." + file_extension + "\'"
		cont = raw_input("")
		sys.exit(0)



	#destination_directory = source_dir + "\\" +"lores_jpeg\\"


	destination = raw_input("Enter destination directory: ")

	destination = destination.replace("\"", "")
	if os.path.isdir(destination) == False:
		print "\nError! Selected item is not a directory. Can not continue."
		cont = raw_input("")
		sys.exit(0)

	#os.mkdir(destination_directory)

	for filename in abs_file:
		#os.system("ffmpeg -i " + filename + " " + destination + filename.split("\\")[-1] + ".jpeg")	
		copypp(filename, destination)

	print "Jpegs exported to " + str(destination)
	print "Press enter to continue...."
	cont = raw_input("")
	sys.exit(0)


def copypp(source_file, destination):
    # get the directory name of the selected file, and split it into pairs
    file_directory = os.path.dirname(source_file).split("\\")

    # change destination
    file_directory[0] = destination

    # get the file name
    file_name = source_file.split("\\")[-1].replace("\"", "")

    joined_path = os.path.join(*file_directory)  # + "\\"

    print "\nFile name  : " + file_name
    print "\nSplit path : " + str(file_directory)
    print "\nJoined path: " + joined_path

    if os.path.exists(joined_path) == True:
        print "\n......Path already exists.......continuing...."
    else:
        print "\n....setting up new directory structure...."
        os.makedirs(joined_path)

    if os.path.exists(joined_path + "\\" + file_name) == True:
        print "\n" + file_name + " exists..."
        ch = raw_input("\n[O]verwrite / [C]ancel?\n")

        if str.lower(ch) == 'c':
            print "Process cancelled."
            cont = raw_input("")
            sys.exit(0)

        if str.lower(ch) == 'o':
            print "Overwriting...."

    #shutil.copy(source_file, joined_path)
    os.system("ffmpeg -i \"" + source_file + "\" \"" + joined_path + "\\" + source_file.split("\\")[-1] + ".jpeg\"")	
    print "File copied successfully!"




if __name__ == '__main__':
	main()