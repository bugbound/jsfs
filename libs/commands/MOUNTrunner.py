from libs.commands.showmount.DiscoveryManager import DiscoveryManager

class MOUNTrunner:
	@staticmethod
	def run(fakeFileSystem, webnuke, line):
		dm = DiscoveryManager()
		args = line.split(' ')
		show_usage = False
		if len(args) == 1:
			if args[0] == "--all":
				services = dm.find_services(webnuke)
				for x in services:
					dm.mount_service(webnuke, x['name'], x['type'])
			else:
				show_usage = True
		elif len(args) == 2:
			servicename = args[0]
			servicetype = args[1]
			dm.mount_service(webnuke, servicename, servicetype)
			#services = dm.find_services(webnuke)
			#print("NAME - TYPE")
			#for x in services:
			#	print("%s - %s"%(x['name'], x['type']))
		else:
			show_usage = True
		
		if(show_usage):
			print("USAGE:") 
			print("\tmount name type")
			print("\tmount --all")
		print('')
		#filepathinfo = fakeFileSystem.CD_merge_filepath(line)
		#fakeFileSystem.CAT(webnuke, filepathinfo['newpath'])
		#print(filepathinfo)
