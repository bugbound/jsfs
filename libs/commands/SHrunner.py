class SHrunner:
	@staticmethod
	def run(fakeFileSystem, webnuke, line):
		#print(line)
		#remove arg stuff
		args = line.split(' ')
		filepath = args[0]
		fileargs = ",".join(args[1:])
		filepathinfo = fakeFileSystem.CD_merge_filepath(filepath)
		fakeFileSystem.SH(webnuke, filepathinfo['newpath'], fileargs)
		#print(filepathinfo)
