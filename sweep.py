import os
from sys import argv
from project_url import url
from array import array
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from secrets import password
# BUGS: PROJECT 226, doesn't fetch question 3 and 4
# BUGS:


class InstaBot:
	# LOGIN AND GO TO PROJECT PAGE
	def __init__(self, username, password):
		self.driver = webdriver.Chrome()
		self.driver.get("https://intranet.hbtn.io/projects/221")
		self.driver.find_element_by_xpath("//input[@id=\"user_login\"]")\
            .send_keys(username)
		self.driver.find_element_by_xpath("//input[@id=\"user_password\"]")\
            .send_keys(password)
		self.driver.find_element_by_xpath('/html/body/main/article/div/form/div[4]/input')\
            .click()
	# CHOICE PROJECT PAGE
		project_url = "\"intranet.hbtn.io/projects/{}\"".format(argv[1])
		print(project_url)
		self.driver.get("https://intranet.hbtn.io/projects/{:s}".format(argv[1]))
		print("IF DIRECTORY IS INCORRECT WRITE DIRECTORY NAME AS 4TH ARGUMENT")

	# GET REPO NAME
		try:
			repo_name = self.driver.find_element_by_xpath(
			    '/html/body/main/article/p[1]/small').text
			print(repo_name)
			if repo_name == 'Foundations - Low-level programming & Algorithm ― Hatching out':
				repo_name = 'holbertonschool-low_level_programming'
			elif repo_name == 'Foundations - Higher-level programming ― Python':
				repo_name = 'holbertonschool-higher_level_programming'
		except NoSuchElementException:
				pass

		# try:
		# repo_name = self.driver.find_element_by_xpath('/html/body/main/article/section/div[1]/div/ul/li[1]/code').text
		# print(repo_name)
		# except NoSuchElementException:
			# pass

	# GET DIRECTORY NAME
		try:
			directory_name = self.driver.find_element_by_xpath(
			    '/html/body/main/article/section[2]/div[1]/div/ul[2]/li[2]/code').text
			print(directory_name)
		except NoSuchElementException:
				pass
		try:
			directory_name = self.driver.find_element_by_xpath(
			    '/html/body/main/article/section[2]/div[1]/div/ul/li[2]/code').text
			print(directory_name)
		except NoSuchElementException:
				pass
		try:
			directory_name = self.driver.find_element_by_xpath(
			    '/html/body/main/article/section/div[1]/div/ul/li[2]/code').text
			print(directory_name)
		except NoSuchElementException:
				pass

		try:
			directory_name = self.driver.find_element_by_xpath(
			    '/html/body/main/article/section/div[1]/div/ul[2]/li[2]/code').text
			print(directory_name)
		except NoSuchElementException:
				pass

	# GET FILE NAME

		file_name_array = []
	# /html/body/main/article/section[2]/div[1]/div/ul[2]/li[3]/code
	# /html/body/main/article/section/div[1]/div/ul[2]/li[3]/code
	# /html/body/main/article/section/div[1]/div/ul/li[3]/code
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
# PRINT ARRAY
		try:
			directory_path = '/users/qpv2/' + repo_name + '/' + directory_name
		except UnboundLocalError:
			if len(argv) < 2:
				print("DIRECTORY NAME UNKNOWN ENTER THE DIRECTORY NAME AS 4TH ARGUMENT")
				print("DIRECTORY NAME UNKNOWN ENTER THE DIRECTORY NAME AS 4TH ARGUMENT")
			else:
				print("")
			if len(argv) > 1:
				print("Inserted directory manually: {:s}".format(argv[2]))
				directory_name = argv[2]
				directory_path = '/users/qpv2/' + repo_name + '/' + directory_name
			pass
			pass

# MAKE DIRECTORY
		if not os.path.exists(directory_path):
			os.makedirs(directory_path)
			print("{:s} has been created".format(directory_path))
# CD INTO DIRECTORY TO PLACE FILES IN IT
		os.chdir(directory_path)
		print("cd into {:s}".format(directory_path))
# MAKE FILES AND APPEND
		print("Project files created:")
		print(file_name_array)
		for file_name_array in file_name_array:
			if repo_name == 'holbertonschool-low_level_programming':
    				with open("{}".format(file_name_array), "w") as f:
        				f.write("#include holberton.h\n\n/**\n*\n*\n**/\n")
			elif repo_name == 'holbertonschool-higher_level_programming':
    				with open("{}".format(file_name_array), "w") as f:
        				f.write("#!/usr/bin/python3\n")
		f = open('README.md', "a")
		f.write("README.md")
		print("README.md made")
# FIND MAIN FILES SECTION/DIV[1]/div/pre/code
		if repo_name == 'holbertonschool-low_level_programming':
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[1]/div/pre/code').text
				main_C_file_count = 0
				main_C_file_count += 1
				f= open("0-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[2]/div/pre/code').text
				main_C_file_count += 1
				f= open("1-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[3]/div/pre/code').text
				main_C_file_count += 1
				f= open("2-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[4]/div/pre/code').text
				main_C_file_count += 1
				f= open("3-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[5]/div/pre/code').text
				main_C_file_count += 1
				f= open("4-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[6]/div/pre/code').text
				main_C_file_count += 1
				f= open("5-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[7]/div/pre/code').text
				main_C_file_count += 1
				f= open("6-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[8]/div/pre/code').text
				main_C_file_count += 1
				f= open("7-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[9]/div/pre/code').text
				main_C_file_count += 1
				f= open("8-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[10]/div/pre/code').text
				main_C_file_count += 1
				f= open("9-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[11]/div/pre/code').text
				main_C_file_count += 1
				f= open("10-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[12]/div/pre/code').text
				main_C_file_count += 1
				f= open("11-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[13]/div/pre/code').text
				main_C_file_count += 1
				f= open("12-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[14]/div/pre/code').text
				main_C_file_count += 1
				f= open("13-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[15]/div/pre/code').text
				main_C_file_count += 1
				f= open("14-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[16]/div/pre/code').text
				main_C_file_count += 1
				f= open("15-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[17]/div/pre/code').text
				main_C_file_count += 1
				f= open("16-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[18]/div/pre/code').text
				main_C_file_count += 1
				f= open("17-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[19]/div/pre/code').text
				main_C_file_count += 1
				f= open("18-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section/div[20]/div/pre/code').text
				main_C_file_count += 1
				f= open("19-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass

# FIND MAIN FILES section[2]/div[1]/div/pre/code
		if repo_name == 'holbertonschool-low_level_programming':
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[1]/div/pre/code').text
				main_C_file_count += 1
				f= open("0-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[2]/div/pre/code').text
				main_C_file_count += 1
				f= open("1-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[3]/div/pre/code').text
				main_C_file_count += 1
				f= open("2-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[4]/div/pre/code').text
				main_C_file_count += 1
				f= open("3-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[5]/div/pre/code').text
				main_C_file_count += 1
				f= open("4-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[6]/div/pre/code').text
				main_C_file_count += 1
				f= open("5-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[7]/div/pre/code').text
				main_C_file_count += 1
				f= open("6-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[8]/div/pre/code').text
				main_C_file_count += 1
				f= open("7-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[9]/div/pre/code').text
				main_C_file_count += 1
				f= open("8-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[10]/div/pre/code').text
				main_C_file_count += 1
				f= open("9-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[11]/div/pre/code').text
				main_C_file_count += 1
				f= open("10-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[12]/div/pre/code').text
				main_C_file_count += 1
				f= open("11-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[13]/div/pre/code').text
				main_C_file_count += 1
				f= open("12-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[14]/div/pre/code').text
				main_C_file_count += 1
				f= open("13-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[15]/div/pre/code').text
				main_C_file_count += 1
				f= open("14-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[16]/div/pre/code').text
				main_C_file_count += 1
				f= open("15-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[17]/div/pre/code').text
				main_C_file_count += 1
				f= open("16-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[18]/div/pre/code').text
				main_C_file_count += 1
				f= open("17-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[19]/div/pre/code').text
				main_C_file_count += 1
				f= open("18-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[20]/div/pre/code').text
				main_C_file_count += 1
				f= open("19-main.c", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			print("{:d} main.c files created".format(main_C_file_count))
# MAKE MAIN.PY FILES
		else:
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[1]/div/pre/code').text
				main_PY_file_count = 0
				main_PY_file_count += 1
				f= open("0-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[2]/div/pre/code').text
				main_PY_file_count += 1
				f= open("1-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[3]/div/pre/code').text
				main_PY_file_count += 1
				f= open("2-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[4]/div/pre/code').text
				main_PY_file_count += 1
				f= open("3-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[5]/div/pre/code').text
				main_PY_file_count += 1
				f= open("4-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[6]/div/pre/code').text
				main_PY_file_count += 1
				f= open("5-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[7]/div/pre/code').text
				main_PY_file_count += 1
				f= open("6-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[8]/div/pre/code').text
				main_PY_file_count += 1
				f= open("7-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[9]/div/pre/code').text
				main_PY_file_count += 1
				f= open("8-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[10]/div/pre/code').text
				main_PY_file_count += 1
				f= open("9-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[11]/div/pre/code').text
				main_PY_file_count += 1
				f= open("10-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[12]/div/pre/code').text
				main_PY_file_count += 1
				f= open("11-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[13]/div/pre/code').text
				main_PY_file_count += 1
				f= open("12-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[14]/div/pre/code').text
				main_PY_file_count += 1
				f= open("13-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[15]/div/pre/code').text
				main_PY_file_count += 1
				f= open("14-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[16]/div/pre/code').text
				main_PY_file_count += 1
				f= open("15-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[17]/div/pre/code').text
				main_PY_file_count += 1
				f= open("16-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[18]/div/pre/code').text
				main_PY_file_count += 1
				f= open("17-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[19]/div/pre/code').text
				main_PY_file_count += 1
				f= open("18-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			try:
				main_file = self.driver.find_element_by_xpath('/html/body/main/article/section[2]/div[20]/div/pre/code').text
				main_PY_file_count += 1
				f= open("19-main.py", "w+")
				f.write(main_file)
			except NoSuchElementException:
					pass
			print("{:d} main.py files created".format(main_PY_file_count))
# EDIT MAIN FILES
# EDIT MAIN.PY
		mainPY_file_array = []
		mainPY_file_array.append('0-main.py')
		mainPY_file_array.append('1-main.py')
		mainPY_file_array.append('2-main.py')
		mainPY_file_array.append('3-main.py')
		mainPY_file_array.append('4-main.py')
		mainPY_file_array.append('5-main.py')
		mainPY_file_array.append('6-main.py')
		mainPY_file_array.append('7-main.py')
		mainPY_file_array.append('8-main.py')
		mainPY_file_array.append('9-main.py')
		mainPY_file_array.append('10-main.py')
		mainPY_file_array.append('11-main.py')
		mainPY_file_array.append('12-main.py')
		mainPY_file_array.append('13-main.py')
		mainPY_file_array.append('14-main.py')
		mainPY_file_array.append('15-main.py')
		for mainPY_file_array in mainPY_file_array:
			try:
				lookup = './'
				myFile = open(mainPY_file_array)
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = '$ cat'
				myFile = open(mainPY_file_array)
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open(mainPY_file_array, 'r+')
				data = myFile.read().splitlines(True)
				myFile = open(mainPY_file_array, 'w')
				myFile.writelines(data[cat_line_number:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
		mainC_file_array = []
		mainC_file_array.append('0-main.c')
		mainC_file_array.append('1-main.c')
		mainC_file_array.append('2-main.c')
		mainC_file_array.append('3-main.c')
		mainC_file_array.append('4-main.c')
		mainC_file_array.append('5-main.c')
		mainC_file_array.append('6-main.c')
		mainC_file_array.append('7-main.c')
		mainC_file_array.append('8-main.c')
		mainC_file_array.append('9-main.c')
		mainC_file_array.append('10-main.c')
		mainC_file_array.append('11-main.c')
		mainC_file_array.append('12-main.c')
		mainC_file_array.append('13-main.c')
		mainC_file_array.append('14-main.c')
		mainC_file_array.append('15-main.c')
		for mainC_file_array in mainC_file_array:
			try:
				lookup = 'gcc'
				myFile = open(mainC_file_array)
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = '$ cat'
				myFile = open(mainC_file_array)
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open(mainC_file_array, 'r+')
				data = myFile.read().splitlines(True)
				myFile = open(mainC_file_array, 'w')
				myFile.writelines(data[cat_line_number:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass


InstaBot('1661@holbertonschool.com', password)
