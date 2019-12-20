class FileUtil:
	@staticmethod
	def read_file(filename):
		f = open(filename, 'r')
		filecontent = f.read()
		f.close()
		return filecontent
