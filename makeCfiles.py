import os
import array
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from secrets import password

class InstaBot:
	##LOGIN AND GO TO PROJECT PAGE
	def __init__(self, username, password):
		self.driver = webdriver.Chrome()
		self.driver.get("https://intranet.hbtn.io/projects/221")
		self.driver.find_element_by_xpath("//input[@id=\"user_login\"]")\
            .send_keys(username)
		self.driver.find_element_by_xpath("//input[@id=\"user_password\"]")\
            .send_keys(password)
		self.driver.find_element_by_xpath('/html/body/main/article/div/form/div[4]/input')\
            .click()
	##CHOICE PROJECT PAGE
		self.driver.get("https://intranet.hbtn.io/projects/222")
	##GET REPO NAME
		try:
			repo_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[1]/div/ul[2]/li[1]/code').text
			print(repo_name)
		except NoSuchElementException:
				pass
		try:
			repo_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[1]/div/ul/li[1]/code').text
			print(repo_name)
		except NoSuchElementException:
				pass
		try:
			repo_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[1]/div/ul[2]/li[1]/code').text
			print(repo_name)
		except NoSuchElementException:
				pass
		##try:
		##	repo_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[1]/div/ul/li[1]/code').text
		##	print(repo_name)
		##except NoSuchElementException:
			##	pass

	##GET DIRECTORY NAME
		try:
			directory_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[1]/div/ul[2]/li[2]/code').text
			print(directory_name)
		except NoSuchElementException:
				pass
		try:
			directory_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[1]/div/ul/li[2]/code').text
			print(directory_name)
		except NoSuchElementException:
				pass
		try:
			directory_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[1]/div/ul[2]/li[2]/code').text
			print(directory_name)
		except NoSuchElementException:
				pass
		##try:
		##	directory_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[1]/div/ul/li[2]/code').text
		##	print(directory_name)
		##except NoSuchElementException:
			##	pass

	##GET FILE NAME

		file_name_array = []
	##/html/body/main/article/section[2]/div[1]/div/ul[2]/li[3]/code
	##/html/body/main/article/section/div[1]/div/ul[2]/li[3]/code
	##/html/body/main/article/section/div[1]/div/ul/li[3]/code
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[1]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		file_name_array = []
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[1]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[2]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
        		pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[3]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
        		pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[4]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
        		pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[5]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
        		pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[6]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
        		pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[7]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
        		pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[8]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
        		pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[9]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
        		pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[10]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
        		pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[11]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
        		pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[12]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
        		pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[13]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
        		pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[14]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
        		pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[15]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
        		pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[16]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
        		pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[17]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
        		pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[18]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
        		pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[19]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
        		pass

		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[20]/div/ul[2]/li[3]/code').text
		except NoSuchElementException:
        		pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[2]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[3]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[4]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[5]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[6]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[7]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[8]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[9]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[10]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[11]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[12]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[13]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[14]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[15]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[16]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[17]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[18]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[19]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[20]/div/ul[2]/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[1]/div/ul/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[2]/div/ul/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[2]/div/ul/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[3]/div/ul/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[4]/div/ul/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[5]/div/ul/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[6]/div/ul/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[7]/div/ul/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[8]/div/ul/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[9]/div/ul/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[10]/div/ul/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[11]/div/ul/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[12]/div/ul/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[13]/div/ul/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[14]/div/ul/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[15]/div/ul/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[16]/div/ul/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[17]/div/ul/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[18]/div/ul/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
		try:
			file_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[19]/div/ul/li[3]/code').text
			file_name_array.append(file_name)
		except NoSuchElementException:
				pass
##PRINT ARRAY
		directory_path = '/users/qpv2/' + repo_name + '/' + directory_name
		print(directory_path)
#MAKE DIRECTORY
		if not os.path.exists(directory_path):
			os.makedirs(directory_path)
			print("{:s} has been created".format(directory_path))
#CD INTO DIRECTORY TO PLACE FILES IN IT
		os.chdir(directory_path)
		print("cd into {:s}".format(directory_path))
##MAKE FILES AND APPEND
		print("Project files created:")
		print(file_name_array)
		print(repo_name)
		for file_name_array in file_name_array:
    			with open("{}".format(file_name_array), "w") as f:
        				f.write("#include holberton.h\n\n/**\n*\n*\n**/\n")
		f = open('README.md', "a")
		f.write("README.md")
		print("README.md made")
##FIND MAIN FILES SECTION/DIV[1]/div/pre/code
		if repo_name == 'holbertonschool-low_level_programming':
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[1]/div/pre/code').text
				print("main file made")
				f= open("0-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[2]/div/pre/code').text
				print("main file made")
				f= open("1-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[3]/div/pre/code').text
				print("main file made")
				f= open("2-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[4]/div/pre/code').text
				print("main file made")
				f= open("3-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[5]/div/pre/code').text
				print("main file made")
				f= open("4-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[6]/div/pre/code').text
				print("main file made")
				f= open("5-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[7]/div/pre/code').text
				print("main file made")
				f= open("6-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[8]/div/pre/code').text
				print("main file made")
				f= open("7-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[9]/div/pre/code').text
				print("main file made")
				f= open("8-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[10]/div/pre/code').text
				print("main file made")
				f= open("9-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[11]/div/pre/code').text
				print("main file made")
				f= open("10-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[12]/div/pre/code').text
				print("main file made")
				f= open("11-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[13]/div/pre/code').text
				print("main file made")
				f= open("12-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[14]/div/pre/code').text
				print("main file made")
				f= open("13-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[15]/div/pre/code').text
				print("main file made")
				f= open("14-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[16]/div/pre/code').text
				print("main file made")
				f= open("15-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[17]/div/pre/code').text
				print("main file made")
				f= open("16-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[18]/div/pre/code').text
				print("main file made")
				f= open("17-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[19]/div/pre/code').text
				print("main file made")
				f= open("18-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[20]/div/pre/code').text
				print("main file made")
				f= open("19-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass

##FIND MAIN FILES section[2]/div[1]/div/pre/code
		if repo_name == 'holbertonschool-low_level_programming':
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[1]/div/pre/code').text
				print("main file made")
				f= open("0-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[2]/div/pre/code').text
				print("main file made")
				f= open("1-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[3]/div/pre/code').text
				print("main file made")
				f= open("2-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[4]/div/pre/code').text
				print("main file made")
				f= open("3-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[5]/div/pre/code').text
				print("main file made")
				f= open("4-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[6]/div/pre/code').text
				print("main file made")
				f= open("5-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[7]/div/pre/code').text
				print("main file made")
				f= open("6-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[8]/div/pre/code').text
				print("main file made")
				f= open("7-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[9]/div/pre/code').text
				print("main file made")
				f= open("8-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[10]/div/pre/code').text
				print("main file made")
				f= open("9-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[11]/div/pre/code').text
				print("main file made")
				f= open("10-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[12]/div/pre/code').text
				print("main file made")
				f= open("11-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[13]/div/pre/code').text
				print("main file made")
				f= open("12-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[14]/div/pre/code').text
				print("main file made")
				f= open("13-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[15]/div/pre/code').text
				print("main file made")
				f= open("14-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[16]/div/pre/code').text
				print("main file made")
				f= open("15-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[17]/div/pre/code').text
				print("main file made")
				f= open("16-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[18]/div/pre/code').text
				print("main file made")
				f= open("17-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[19]/div/pre/code').text
				print("main file made")
				f= open("18-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[20]/div/pre/code').text
				print("main file made")
				f= open("19-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
	##EDIT MAIN.C FILES
			lookup = 'gcc'
			try:
				myFile = open('0-main.c')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('0-main.c')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('0-main.c', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('0-main.c', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = 'gcc'
			try:
				myFile = open('1-main.c')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('1-main.c')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('1-main.c', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('1-main.c', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = 'gcc'
			try:
				myFile = open('2-main.c')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('2-main.c')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('2-main.c', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('2-main.c', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = 'gcc'
			try:
				myFile = open('3-main.c')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('3-main.c')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('3-main.c', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('3-main.c', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = 'gcc'
			try:
				myFile = open('4-main.c')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('4-main.c')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('4-main.c', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('4-main.c', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = 'gcc'
			try:
				myFile = open('5-main.c')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('5-main.c')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('5-main.c', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('5-main.c', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = 'gcc'
			try:
				myFile = open('6-main.c')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('6-main.c')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('6-main.c', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('6-main.c', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = 'gcc'
			try:
				myFile = open('7-main.c')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('7-main.c')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('7-main.c', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('7-main.c', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = 'gcc'
			try:
				myFile = open('8-main.c')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('8-main.c')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('8-main.c', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('8-main.c', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = 'gcc'
			try:
				myFile = open('9-main.c')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('9-main.c')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('9-main.c', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('9-main.c', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = 'gcc'
			try:
				myFile = open('10-main.c')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('10-main.c')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('10-main.c', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('10-main.c', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = 'gcc'
			try:
				myFile = open('11-main.c')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('11-main.c')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('11-main.c', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('11-main.c', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = 'gcc'
			try:
				myFile = open('12-main.c')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('12-main.c')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('12-main.c', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('12-main.c', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = 'gcc'
			try:
				myFile = open('13-main.c')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('13-main.c')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('13-main.c', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('13-main.c', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = 'gcc'
			try:
				myFile = open('14-main.c')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('14-main.c')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('14-main.c', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('14-main.c', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = 'gcc'
			try:
				myFile = open('15-main.c')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('15-main.c')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('15-main.c', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('15-main.c', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = 'gcc'
			try:
				myFile = open('16-main.c')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('16-main.c')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('16-main.c', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('16-main.c', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = 'gcc'
			try:
				myFile = open('17-main.c')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('17-main.c')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('17-main.c', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('17-main.c', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = 'gcc'
			try:
				myFile = open('18-main.c')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('18-main.c')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('18-main.c', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('18-main.c', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = 'gcc'
			try:
				myFile = open('99-main.c')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('99-main.c')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('99-main.c', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('99-main.c', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
#MAKE MAIN.PY FILES
		else:
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[1]/div/pre/code').text
				print("main file made")
				print(main_file)
				f= open("0-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[2]/div/pre/code').text
				print("main file made")
				f= open("1-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[3]/div/pre/code').text
				print("main file made")
				f= open("2-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[4]/div/pre/code').text
				print("main file made")
				f= open("3-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[5]/div/pre/code').text
				print("main file made")
				f= open("4-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[6]/div/pre/code').text
				print("main file made")
				f= open("5-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[7]/div/pre/code').text
				print("main file made")
				f= open("6-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[8]/div/pre/code').text
				print("main file made")
				f= open("7-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[9]/div/pre/code').text
				print("main file made")
				f= open("8-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[10]/div/pre/code').text
				print("main file made")
				f= open("9-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[11]/div/pre/code').text
				print("main file made")
				f= open("10-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[12]/div/pre/code').text
				print("main file made")
				f= open("11-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[13]/div/pre/code').text
				print("main file made")
				f= open("12-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[14]/div/pre/code').text
				print("main file made")
				f= open("13-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[15]/div/pre/code').text
				print("main file made")
				f= open("14-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[16]/div/pre/code').text
				print("main file made")
				f= open("15-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[17]/div/pre/code').text
				print("main file made")
				f= open("16-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[18]/div/pre/code').text
				print("main file made")
				f= open("17-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[19]/div/pre/code').text
				print("main file made")
				f= open("18-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[20]/div/pre/code').text
				print("main file made")
				f= open("19-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
	##EDIT MAIN FILES
			lookup = './'
			try:
				myFile = open('0-main.py')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('0-main.py')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('0-main.py', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('0-main.py', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = './'
			try:
				myFile = open('1-main.py')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('1-main.py')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('1-main.py', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('1-main.py', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = './'
			try:
				myFile = open('2-main.py')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('2-main.py')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('2-main.py', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('2-main.py', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = './'
			try:
				myFile = open('3-main.py')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('3-main.py')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('3-main.py', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('3-main.py', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = './'
			try:
				myFile = open('4-main.py')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('4-main.py')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('4-main.py', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('4-main.py', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = './'
			try:
				myFile = open('5-main.py')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('5-main.py')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('5-main.py', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('5-main.py', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = './'
			try:
				myFile = open('6-main.py')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('6-main.py')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('6-main.py', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('6-main.py', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = './'
			try:
				myFile = open('7-main.py')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('7-main.py')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('7-main.py', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('7-main.py', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = './'
			try:
				myFile = open('8-main.py')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('8-main.py')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('8-main.py', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('8-main.py', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = './'
			try:
				myFile = open('9-main.py')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('9-main.py')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('9-main.py', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('9-main.py', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = './'
			try:
				myFile = open('10-main.py')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('10-main.py')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('10-main.py', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('10-main.py', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = './'
			try:
				myFile = open('11-main.py')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('11-main.py')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('11-main.py', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('11-main.py', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = './'
			try:
				myFile = open('12-main.py')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('12-main.py')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('12-main.py', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('12-main.py', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = './'
			try:
				myFile = open('13-main.py')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('13-main.py')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('13-main.py', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('13-main.py', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = './'
			try:
				myFile = open('14-main.py')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('14-main.py')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('14-main.py', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('14-main.py', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = './'
			try:
				myFile = open('15-main.py')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('15-main.py')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('15-main.py', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('15-main.py', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = './'
			try:
				myFile = open('16-main.py')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('16-main.py')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('16-main.py', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('16-main.py', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = './'
			try:
				myFile = open('17-main.py')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('17-main.py')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('17-main.py', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('17-main.py', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = './'
			try:
				myFile = open('18-main.py')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('18-main.py')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('18-main.py', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('18-main.py', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
			lookup = './'
			try:
				myFile = open('99-main.py')
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = 'cat'
				myFile = open('99-main.py')
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open('99-main.py', 'r+')
				data = myFile.read().splitlines(True)
				myFile = open('99-main.py', 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass

InstaBot('1661@holbertonschool.com', password)
