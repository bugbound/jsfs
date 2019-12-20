class GDBrunner:
	@staticmethod
	def run(fakeFileSystem, webnuke, line):
		#print(line)
		print("<<<<<GDB>>>>>")
		if line:
			newpath = fakeFileSystem.CD_merge_filepath(line)['newpath']
			jspath = fakeFileSystem.convert_filepath_to_jspath(newpath)
			print(webnuke.run_javascript("return Object.keys("+jspath+");"))
		else:
			print("USAGE: gdb /folder/function")
		
		print('')
