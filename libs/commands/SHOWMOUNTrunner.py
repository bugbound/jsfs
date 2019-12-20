from libs.commands.showmount.DiscoveryManager import DiscoveryManager

class SHOWMOUNTrunner:
	@staticmethod
	def run(fakeFileSystem, webnuke, line):
		dm = DiscoveryManager()
		
		services = dm.find_services(webnuke)
		print("NAME - TYPE")
		for x in services:
			print("%s - %s"%(x['name'], x['type']))
		print('')
