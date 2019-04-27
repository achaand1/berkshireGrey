import unittest, listoffiles, mock



class getfiles(unittest.TestCase):
	# Test Case 1 - Verify if the filepath from main is also in getFileList
	def test_find(self):
		self.assertTrue(listoffiles.getFileList(dirpath))
		print('Test case 1 complete')

	# Test Case 2 - Count the number of files are the same and function recursed through all the files.
	def test_count(self):
		var = len(listoffiles.getFileList(dirpath))
		self.assertTrue(var,3)
		print('Test case 2 complete')

	# Test Case 3 - Verify the input functionality
	def test_input(self):
		with mock.patch('builtins.input', return_value=dirpath):
			self.assertEqual(listoffiles.get_input(dirpath), "C:\\python\\berkshireGrey")
			print('Test case 3 complete')

if __name__=='__main__':
	dirpath = "C:\\python\\berkshireGrey"
	unittest.main()
