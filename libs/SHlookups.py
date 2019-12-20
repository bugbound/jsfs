class SHlookups:
	@staticmethod
	def SHlookup(fakeFileSystem, webnuke, lookuptext, fullArgs):
		rtndata = []
		args = fullArgs.split(' ')
		args_count = len(args)
		command = args[0]
		command_input = args[1]
		
		input_file = './extract_keys.js'
		f = open(input_file, 'r')
		x = f.read()
		f.close()
		webnuke.run_javascript(x)
		
		# args[0] == ls
		# args[1] == first arg (in this case... hopefully a filepath)
		#print(lineargs_count)
		if not lookuptext:
			if not command_input:
				#print("NO lookuptext given!")
				jspath = fakeFileSystem.convert_filepath_to_jspath(fakeFileSystem.PWD)
				keys = webnuke.run_javascript("return window.__webnuke_run_collector("+jspath+");")
				dirs = keys['props']
				for dirpath in dirs:
					if dirpath not in rtndata:
						rtndata.append(dirpath)
				funcs = keys['funcs']
				for dirpath in funcs:
					if dirpath not in rtndata:
						rtndata.append(dirpath)
			else:
				newpath = fakeFileSystem.CD_merge_filepath(command_input)['newpath']
				is_dir = fakeFileSystem.CD_does_dir_exist(webnuke, newpath)
				if(is_dir):
					jspath = fakeFileSystem.convert_filepath_to_jspath(newpath)
					keys = webnuke.run_javascript("return window.__webnuke_run_collector("+jspath+");")
					dirs = keys['props']
					for dirpath in dirs:
						if dirpath not in rtndata:
							rtndata.append(dirpath)
					funcs = keys['funcs']
					for dirpath in funcs:
						if dirpath not in rtndata:
							rtndata.append(dirpath)
				else:
					newpath = "/".join(newpath.split('/')[:-1])
					jspath = fakeFileSystem.convert_filepath_to_jspath(newpath)
					keys = webnuke.run_javascript("return window.__webnuke_run_collector("+jspath+");")
					dirs = keys['props']
					for dirpath in dirs:
						if dirpath not in rtndata:
							rtndata.append(dirpath)
					funcs = keys['funcs']
					for dirpath in funcs:
						if dirpath not in rtndata:
							rtndata.append(dirpath)
		else:
			#print("LS with lookup")
			#we have lookup text!
			newpath = fakeFileSystem.CD_merge_filepath(command_input)['newpath']
			is_dir = fakeFileSystem.CD_does_dir_exist(webnuke, newpath)
			if(is_dir):
				jspath = fakeFileSystem.convert_filepath_to_jspath(newpath)
				#print(jspath)
				keys = webnuke.run_javascript("return window.__webnuke_run_collector("+jspath+");")
				dirs = keys['props']
				for dirpath in dirs:
					if dirpath not in rtndata and dirpath.startswith(lookuptext):
						rtndata.append(dirpath)
				funcs = keys['funcs']
				for dirpath in funcs:
					if dirpath not in rtndata and dirpath.startswith(lookuptext):
						rtndata.append(dirpath)
			else:
				newpath = "/".join(newpath.split('/')[:-1])
				jspath = fakeFileSystem.convert_filepath_to_jspath(newpath)
				keys = webnuke.run_javascript("return window.__webnuke_run_collector("+jspath+");")
				dirs = keys['props']
				for dirpath in dirs:
					if dirpath not in rtndata and dirpath.startswith(lookuptext):
						rtndata.append(dirpath)
				funcs = keys['funcs']
				for dirpath in funcs:
					if dirpath not in rtndata and dirpath.startswith(lookuptext):
						rtndata.append(dirpath)
			
			
		return rtndata
