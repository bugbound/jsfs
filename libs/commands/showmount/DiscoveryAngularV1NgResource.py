from libs.FileUtil import FileUtil

class DiscoveryAngularV1NgResource:
	def __init__(self):
		self.version = 0.1
		self.type = "angular-v1-ngresource"
		
	def find_services(self, webnuke):
		rtndata = []
		discoveryJsCode = FileUtil.read_file('libs/commands/showmount/js/discovery-%s.js'%self.type)
		#print(discoveryJsCode)
		webnuke.run_javascript(discoveryJsCode)
		services = webnuke.run_javascript("return window.__webnuke_run_discovery();")
		for x in services:
			rtndata.append({'name': x, 'type': self.type})
			
		return rtndata
		
	def mount_service(self, webnuke, servicename, servicetype):
		if servicetype == self.type:
			jscode = "if (!(typeof window.mount != 'undefined')){window.mount={};};window.mount['"+servicename+"'] = angular.element(document.body).injector().get('"+servicename+"');"
			webnuke.run_javascript(jscode)
			print("Mounted %s in /mount/"%servicename)
		
