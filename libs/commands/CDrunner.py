class CDrunner:
	@staticmethod
	def run(fakeFileSystem, webnuke, line):
		#print(line)
		filepathinfo = fakeFileSystem.CD_merge_filepath(line)
		fakeFileSystem.CD(webnuke, filepathinfo['newpath'])
		#print(filepathinfo)
