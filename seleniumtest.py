from selenium import webdriver


class intranetbot:
	def __init__(self):
		self.driver = webdriver.Chrome()
		self.driver.get("https://intranet.hbtn.io/projects/240")


intranetbot()
