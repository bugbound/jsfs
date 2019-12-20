class LSrunner:
	@staticmethod
	def run(fakeFileSystem, webnuke, line):
		#print(line)
		filepathinfo = fakeFileSystem.CD_merge_filepath(line)
		fakeFileSystem.LS(webnuke, filepathinfo['newpath'])
		#print(filepathinfo)
