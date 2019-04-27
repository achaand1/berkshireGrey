import os, re

def get_input(freetext):
	return input(freetext)
 
def getFileList(dirName):
	# create a list of file and sub directories 
	# in the given directory 
	listOfFile = os.listdir(dirName)
	allFiles = list()
	# Iterate over all the entries
	for files in listOfFile:
		# Create full path
		fullPath = os.path.join(dirName, files)
		#fileSize = os.path.getsize(os.path.abspath(fullPath))
		fileSize = os.stat(fullPath).st_size
		name, ext= os.path.splitext(files)
	
		# If file is a directory then get the list of files in this directory 
		if fileSize >=1 and name.startswith('list') and ext == '.py':
			if os.path.isdir(fullPath):
				allFiles = allFiles + getFileList(fullPath)
			else:
				allFiles.append(fullPath)
				
	return allFiles        

 
 
def main():
	
	dirName = get_input('Enter the file path - ')
	checkExist = os.path.exists(dirName)
	if checkExist:
		# Get the list of all files in directory tree at given path
		listOfFiles = getFileList(dirName) 
	
		# Print the files
		for elem in listOfFiles:
			print(elem)
			print ("***** Directory Read Complete *******")
	else:
			print("****** Directory not found *******")
		
if __name__ == '__main__':
	main()