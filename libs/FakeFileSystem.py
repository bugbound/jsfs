from libs.FileUtil import FileUtil

class FakeFileSystem:
    PWD = '/'


    def LS(self, webnuke, filepath):
        dir_exists = self.CD_does_dir_exist(webnuke, filepath)
        if (dir_exists):
			input_file = './extract_keys.js'
			x = FileUtil.read_file(input_file)
			webnuke.run_javascript(x)
			
			jspath = self.convert_filepath_to_jspath(filepath)
			keys = []
			keys = webnuke.run_javascript("return window.__webnuke_run_collector("+jspath+");")
			
			OKBLUE = '\033[94m'
			OKGREEN = '\033[92m'
			OKGRAY = '\033[37m'
			ENDCOLOUR = '\033[0m'
			if 'props' in keys and keys['props']:
				print(OKBLUE+(", ".join(keys['props']))+ENDCOLOUR)
			if 'funcs' in keys and keys['funcs']:
				print(OKGREEN+(", ".join(keys['funcs']))+ENDCOLOUR)        
			if 'files' in keys and keys['files']:
				print(OKGRAY+(", ".join(keys['files']))+ENDCOLOUR)
        else:
			print("Directory %s, does not exist!"%filepath)
    
    def SH_does_function_exist(self, webnuke, jspath):
        is_somejsshit = webnuke.run_javascript("return (typeof "+jspath+" === 'function');")
        return is_somejsshit

    def SH(self, webnuke, filepath, fileargs):
        jspath = self.convert_filepath_to_jspath(filepath)
        file_exists = self.SH_does_function_exist(webnuke, jspath)
        if (file_exists):
			results = ""
			if fileargs:
				print(fileargs)
				results = webnuke.run_javascript("return %s(%s);"%(jspath, fileargs))
			else:
				results = webnuke.run_javascript("return %s();"%jspath)
			print(results)
        else:
			print("Function %s, does not exist!"%filepath)
    
    def SH_does_function_exist(self, webnuke, jspath):
        is_somejsshit = webnuke.run_javascript("return (typeof "+jspath+" === 'function');")
        return is_somejsshit


    def CAT(self, webnuke, filepath):
        #print(filepath)
        jspath = self.convert_filepath_to_jspath(filepath)
        function_exists = self.SH_does_function_exist(webnuke, filepath)
        if function_exists:
			jspath = jspath+".toString()"
			jscontent = webnuke.run_javascript("return "+jspath)
			print(jscontent)
			return True
			
        file_exists = self.CAT_does_file_exist(webnuke, filepath)
        if (file_exists):
			#print("Catting %s..."%filepath)
			
			#print(jspath)
			jscontent = webnuke.run_javascript("return "+jspath)
			print(jscontent)
        else:
			print("File %s, does not exist!"%filepath)
    
    def CAT_does_file_exist(self, webnuke, pathstring):
        jspath = self.convert_filepath_to_jspath(pathstring)
        is_somejsshit = webnuke.run_javascript("return (typeof "+jspath+" === 'object' || typeof "+jspath+" === 'function' || typeof "+jspath+" === 'string' || typeof "+jspath+" === 'number'  || typeof "+jspath+" === 'boolean');")
        return is_somejsshit
        	
    def CD(self, webnuke, newdir):
        new_dir_exists = self.CD_does_dir_exist(webnuke, newdir)
        if (new_dir_exists):
			self.PWD = newdir
        else:
			print("Directory %s, does not exist!"%newdir)
        
    def CD_does_dir_exist(self, webnuke, pathstring):
        jspath = self.convert_filepath_to_jspath(pathstring)
        is_dir = webnuke.run_javascript("return typeof "+jspath+" === 'object';")
        return is_dir
			
    def CD_merge_filepath(self, pathstring):
        rtndata={'newpath': ''}
        
        # remove trailing /
        if pathstring.endswith('/'):
			pathstring = pathstring[:-1]
        
        if pathstring.startswith('/'):
			rtndata['newpath'] = pathstring
        else:
			if pathstring == "..":
				one_dir_back = "/".join(self.PWD.split('/')[:-1])
				if one_dir_back == '':
					one_dir_back = "/"
				rtndata['newpath'] = one_dir_back
			else:
				if self.PWD.endswith('/'):
					rtndata['newpath'] = self.PWD+pathstring
				else:
					rtndata['newpath'] = self.PWD+"/"+pathstring
		
        return rtndata

    def convert_filepath_to_jspath(self, filepath):
        rtnpath = ""
        if(filepath == "/"):
			rtnpath = "window"
        rtnpath = "window"+filepath.replace('/', '.')
        
        if rtnpath.endswith('.'):
			#remove last char
			rtnpath = rtnpath[:-1]
        return rtnpath
