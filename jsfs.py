#!/bin/python
"""Usage: 
	jsfs.py [--proxy=<proxy>] 
	jsfs.py -h | --help
	jsfs.py --version
	
Options:
    --proxy=<proxy>    		   set browser to use proxy, eg --proxy=http://localhost:8080
	-h --help                  show this
	--version                  shows the current version
"""
from docopt import docopt

from cmd import Cmd

from libs.WebNuke import WebNuke
from libs.commands.JSFSInterpreter import JSFSInterpreter

start_page = "about:blank"

if __name__ == "__main__":
	arguments = docopt(__doc__, version='jsfs 0.1 BETA')
	proxy = arguments['--proxy']
	mainapp = JSFSInterpreter()
	webnuke = WebNuke(start_page, proxy)
	mainapp.setWebnuke(webnuke)
	mainapp.cmdloop()
	mainapp.quit()
