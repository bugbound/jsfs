from libs.WebManager import WebManager

class WebNuke:
	def __init__(self, start_page, proxy):
		self.version = 0.1
		self.status = "working..."
		self.webmanager = WebManager(start_page, proxy)
		
	def run_javascript(self, script_to_run):
		return self.webmanager.run_javascript(script_to_run)

	def get(self, url):
		return self.webmanager.get(url)
		
	def quit(self):
		self.webmanager.quit()
