from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


class WebManager:
	def __init__(self, start_page, proxy):
		self.version=0.1
		self.webdrivers = []
		self.current_driver = -1
		self.start_page = start_page
		
        
		options = Options()
		options.add_argument("start-maximized")
		options.binary_location="/usr/bin/chromium-browser"
        if proxy:
            options.add_argument("--proxy-server={0}".format(proxy))
		driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/bin/chromedriver')		
		driver.get(self.start_page)
		self.webdrivers.append(driver)
		self.current_driver = 0
	
	def run_javascript(self, script_to_run):
		try:
			return self.webdrivers[self.current_driver].execute_script(script_to_run)
		except:
			return "Error with run_javascript"
			raise

	def get(self, url):
		try:
			return self.webdrivers[self.current_driver].get(url)
		except:
			return "Error with run_javascript"
			raise
			
	def quit(self):
		for x in self.webdrivers:
			#x.close()
			x.quit()
