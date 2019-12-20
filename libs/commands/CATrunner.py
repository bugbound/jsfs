class CATrunner:
	@staticmethod
	def run(fakeFileSystem, webnuke, line):
		#print(line)
		filepathinfo = fakeFileSystem.CD_merge_filepath(line)
		fakeFileSystem.CAT(webnuke, filepathinfo['newpath'])
		#print(filepathinfo)
