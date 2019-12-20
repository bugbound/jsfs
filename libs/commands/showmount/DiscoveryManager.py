from libs.commands.showmount.DiscoveryAngularV1NgResource import DiscoveryAngularV1NgResource
from libs.commands.showmount.DiscoveryReactOnRails import DiscoveryReactOnRails

class DiscoveryManager:
	def __init__(self):
		self.version = 0.1
		#self.modules = [DiscoveryAngularV1NgResource(), DiscoveryReactOnRails()]
		self.modules = [DiscoveryAngularV1NgResource()]

	def find_services(self, webnuke):
		rtndata = []
		for module in self.modules:
			services_found = module.find_services(webnuke)
			for service in services_found:
				rtndata.append(service)
				
		return rtndata
		
	def mount_service(self, webnuke, svcname, svctype):
		for module in self.modules:
			module.mount_service(webnuke, svcname, svctype)
			
