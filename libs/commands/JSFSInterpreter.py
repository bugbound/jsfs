from cmd import Cmd

from libs.FakeFileSystem import FakeFileSystem
from libs.commands.CATrunner import CATrunner
from libs.commands.SHrunner import SHrunner
from libs.commands.LSrunner import LSrunner
from libs.commands.CDrunner import CDrunner
from libs.commands.SHOWMOUNTrunner import SHOWMOUNTrunner
from libs.commands.MOUNTrunner import MOUNTrunner
from libs.commands.GDBrunner import GDBrunner

from libs.LSlookups import LSlookups
from libs.SHlookups import SHlookups

class JSFSInterpreter(Cmd):
    PWD = '/'
    intro = "Welcome! Type ? to list commands"
    prompt_format = "(jsfs: %s ) # "
    fakeFileSystem = FakeFileSystem()
    prompt = prompt_format%fakeFileSystem.PWD
    

    def setWebnuke(self, webnuke):
        self.webnuke = webnuke

    def do_lynx(self, line):
        self.webnuke.get(line)
    
    def help_lynx(self):
        print '\n'.join([ 'lynx <url>','\tgoto url in browser','','EXAMPLE: ', '\tlynx https://somesite.com/somepage/',''])

    def do_pwd(self, line):
        print(self.fakeFileSystem.PWD)
        
    def help_pwd(self):
        print '\n'.join([ 'pwd','\tdisplays current working directory','','EXAMPLE: ','\tpwd',''])

    def do_echo(self, line):
        if ">" not in line:
			print(line)
        if ">" in line:
			args = line.split('>')
			if len(args) == 2:
				echopart = args[0]
				filepath = args[1].strip()
				#print(filepath)
				filepath = self.fakeFileSystem.CD_merge_filepath(filepath)['newpath']
				#print(filepath)
				if(self.fakeFileSystem.CAT_does_file_exist(self.webnuke, filepath) == True):
					jspath = self.fakeFileSystem.convert_filepath_to_jspath(filepath)
					self.webnuke.run_javascript(jspath+"="+echopart+";")
				else:
					print("File %s was not found!"%filepath	)
    def help_echo(self):
        print '\n'.join([ 'echo <text to print>','\techos input, can be used with a ">" to overwrite dom values','','EXAMPLE: ','\techo w00p', '\techo "w00p" > /localStorage/heh',''])
        
    def smashfilepaths(self, current_dir, line):
        rtndata={'fullpath': '', 'dirpath': ''}
        
        if line.startswith('/'):
			rtndata['fullpath'] = line
        else:
			if line == "..":
				one_dir_back = "/".join(current_dir.split('/')[:-2])
				if one_dir_back == '':
					one_dir_back = "/"
				rtndata['fullpath'] = one_dir_back
			else:
				if current_dir.endswith('/'):
					rtndata['fullpath'] = current_dir+line
				else:
					rtndata['fullpath'] = current_dir+"/"+line
		
        rtndata['dirpath'] = "/".join(rtndata['fullpath'].split('/')[:-1])
        return rtndata

    def complete_cd(self, text, line, begidx, endidx):
        return Lookups.LSlookup(self.fakeFileSystem, self.webnuke, text, line)
 
    def do_cd(self, line):
        CDrunner.run(self.fakeFileSystem, self.webnuke, line)
        self.prompt = self.prompt_format%self.fakeFileSystem.PWD
        
    def help_cd(self):
        print '\n'.join([ 'cd <path>','\tchange current working directory','','EXAMPLE: ','\tcd /localStorage','\tcd ..',''])
        
    def complete_cat(self, text, line, begidx, endidx):
        keys = self.webnuke.run_javascript("return window.__webnuke_run_collector(window);")
        return [i for i in keys['files'] if i.startswith(text)]
        
    def do_cat(self, line):
        CATrunner.run(self.fakeFileSystem, self.webnuke, line)
        print('')

    def help_cat(self):
        print '\n'.join([ 'cat <path>','\tread a javascript value, can be used to read directory entries!','','EXAMPLE: ','\tcat /location/host','\tcat /location',''])


    def complete_shOLD(self, text, line, begidx, endidx):
        keys = self.webnuke.run_javascript("return window.__webnuke_run_collector(window);")
        return [i for i in keys['funcs'] if i.startswith(text)]


    def complete_sh(self, text, line, begidx, endidx):
        return SHlookups.SHlookup(self.fakeFileSystem, self.webnuke, text, line)
        
    def do_sh(self, line):
        SHrunner.run(self.fakeFileSystem, self.webnuke, line)
        print('')

    def help_sh(self):
        print '\n'.join([ 'sh <path> [args]','\tRun a javascript function', '\tWorks with functions requiring additional arguments!','','EXAMPLE: ','\tsh showSiteLoading','\tsh hideSiteLoading','\tsh getUrlParam arg1','\tsh /somepath/bah/blahBlahBlah arg1 arg2...',''])

    
    def complete_ls(self, text, line, begidx, endidx):
        return LSlookups.LSlookup(self.fakeFileSystem, self.webnuke, text, line)

    def do_ls(self, line):
        LSrunner.run(self.fakeFileSystem, self.webnuke, line)
        print('') 

    def help_ls(self):
        print '\n'.join([ 'ls <path>','\tlist directories and files','','EXAMPLE: ','\tls /localStorage','\tls',''])
        
    def do_showmount(self, line):
        SHOWMOUNTrunner.run(self.fakeFileSystem, self.webnuke, line)
        print('') 
    def help_showmount(self):
        print '\n'.join([ 'showmount','\tlist reusable framework components (not fully supported!!!)','','EXAMPLE: ','\tshowmount',''])

    def do_mount(self, line):
        MOUNTrunner.run(self.fakeFileSystem, self.webnuke, line)
        print('') 
    def help_mount(self):
        print '\n'.join([ 'mount <name> <type>','\tmount reusable framework component (not fully supported!!!)','\ton success the component will be available in /mount','','EXAMPLE: ','\tmount productSvc angular-v1-ngresource', '\tmount --all',''])
        
    def do_gdb(self, line):
        GDBrunner.run(self.fakeFileSystem, self.webnuke, line)
        print('') 

	#quit
    def do_quit(self, args):
        return self.quit()
    def do_q(self, args):
        return self.quit()
    def quit(self):
        self.webnuke.quit()
        return True
