import os
from sys import argv
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
        print('\n')
        print(
            "Thank you for choosing the HippoSweeper, Holberton's Superior Project Creator")
        print('\n')
        print("You have selected {}".format(project_url))
        self.driver.get(
            "https://intranet.hbtn.io/projects/{:s}".format(argv[1]))

    # GET REPO NAME
        try:
            readme_repo_name = self.driver.find_element_by_xpath(
                '/html/body/main/article/p[1]/small').text
            if readme_repo_name == 'Foundations - Low-level programming & Algorithm ― Hatching out':
                repo_name = 'holbertonschool-low_level_programming'
            elif readme_repo_name == 'Foundations - Higher-level programming ― Python':
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
            directory_search = self.driver.find_element_by_xpath(
                '/html/body/main/article/section[2]/div[1]/div/ul[2]/li[2]/code').text
            if any(char.isdigit() for char in directory_search):
                directory_name = directory_search
            else:
                pass
        except NoSuchElementException:
            pass
        try:
            directory_search = self.driver.find_element_by_xpath(
                '/html/body/main/article/section[2]/div[1]/div/ul/li[2]/code').text
            if any(char.isdigit() for char in directory_search):
                directory_name = directory_search
            else:
                pass
        except NoSuchElementException:
            pass
        try:
            directory_search = self.driver.find_element_by_xpath(
                '/html/body/main/article/section/div[1]/div/ul/li[2]/code').text
            if any(char.isdigit() for char in directory_search):
                directory_name = directory_search
            else:
                pass
        except NoSuchElementException:
            pass

        try:
            directory_search = self.driver.find_element_by_xpath(
                '/html/body/main/article/section/div[1]/div/ul[2]/li[2]/code').text
            if any(char.isdigit() for char in directory_search):
                directory_name = directory_search
            else:
                pass
        except NoSuchElementException:
            pass
        print(directory_name)

    # GET FILE NAME

        file_name_array = []
    # /html/body/main/article/section[2]/div[1]/div/ul[2]/li[3]/code
    # /html/body/main/article/section/div[1]/div/ul[2]/li[3]/code
    # /html/body/main/article/section/div[1]/div/ul/li[3]/code
        for i in range(0, 21):
            try:
                file_name = self.driver.find_element_by_xpath(
                    '/html/body/main/article/section[2]/div[{:d}]/div/ul[2]/li[3]/code'.format(i)).text
                if any(char.isdigit() for char in file_name):
                    file_name_array.append(file_name)
                else:
                    pass
            except NoSuchElementException:
                pass
        for i in range(0, 21):
            try:
                file_name = self.driver.find_element_by_xpath(
                    '/html/body/main/article/section[2]/div[{:d}]/div/ul[3]/li[3]/code'.format(i)).text
                if any(char.isdigit() for char in file_name):
                    file_name_array.append(file_name)
                else:
                    pass
            except NoSuchElementException:
                pass
        for i in range(0, 21):
            try:
                file_name = self.driver.find_element_by_xpath(
                    '/html/body/main/article/section/div[{:d}]/div/ul[2]/li[3]/code'.format(i)).text
                if any(char.isdigit() for char in file_name):
                    file_name_array.append(file_name)
                else:
                    pass
            except NoSuchElementException:
                pass

        for i in range(0, 21):
            try:
                file_name = self.driver.find_element_by_xpath(
                    '/html/body/main/article/section/div[{:d}]/div/ul/li[3]/code'.format(i)).text
                if any(char.isdigit() for char in file_name):
                    file_name_array.append(file_name)
                else:
                    pass
            except NoSuchElementException:
                pass

# PRINT ARRAY
        try:
            directory_path = '/users/qpv2/' + repo_name + '/' + directory_name
        except UnboundLocalError:
            pass
            # if len(argv) < 2:
            # print("DIRECTORY NAME UNKNOWN ENTER THE DIRECTORY NAME AS 4TH ARGUMENT")
            # print("DIRECTORY NAME UNKNOWN ENTER THE DIRECTORY NAME AS 4TH ARGUMENT")
        #	else:
            #	print("")
            # if len(argv) > 1:
            # print("Inserted directory manually: {:s}".format(argv[2]))
            #	directory_name = argv[2]
            #	directory_path = '/users/qpv2/' + repo_name + '/' + directory_name

# MAKE DIRECTORY
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            print("Creating: {:s}".format(directory_path))
# CD INTO DIRECTORY TO PLACE FILES IN IT
        os.chdir(directory_path)
        print("cd into {:s}".format(directory_path))
# MAKE FILES AND APPEND
        file_name_array = list(dict.fromkeys(file_name_array))
        number_of_project_files = len(file_name_array)
        readme_file_name_array = file_name_array

        print("Project files created:")
        print('\n')
        for file_name_array in file_name_array:
            print(file_name_array)
            if repo_name == 'holbertonschool-low_level_programming':
                with open("{}".format(file_name_array), "w") as f:
                    f.write("#include holberton.h\n\n/**\n*\n*\n**/\n")
            elif repo_name == 'holbertonschool-higher_level_programming':
                with open("{}".format(file_name_array), "w") as f:
                    f.write("#!/usr/bin/python3\n")

# FIND MAIN.C FILES SECTION/DIV[1]/div/pre/code
# if any(char.isdigit() for char in directory_search):
        # directory_name = directory_search
        # else:
        # pass
        if repo_name == 'holbertonschool-low_level_programming':
            for i in range(0, number_of_project_files + 2):
                try:
                    main_file = self.driver.find_element_by_xpath(
                        '/html/body/main/article/section/div[{:d}]/div/pre/code'.format(i)).text
                    main_C_file_count = 0
                    main_C_file_count += 1
                    f = open("{:d}-main.c".format(i - 1), "w+")
                    f.write(main_file)
                except NoSuchElementException:
                    pass
                # if any(char.isdigit() for char in directory_search):
            # directory_name = directory_search
            # else:
            # pass
            for i in range(0, number_of_project_files + 2):
                try:
                    main_file = self.driver.find_element_by_xpath(
                        '/html/body/main/article/section[2]/div[{:d}]/div/pre/code'.format(i)).text
                    main_C_file_count = 0
                    main_C_file_count += 1
                    f = open("{:d}-main.c".format(i - 1), "w+")
                    f.write(main_file)
                except NoSuchElementException:
                    pass
            print("{:d} main.c files created".format(
                number_of_project_files))
            print("README.md created")
            print('\n')
            print("GOOD LUCK WITH YOUR PROJECT")
            print('\n')
            print(directory_path)

# MAKE MAIN.PY FILES
        else:
            for i in range(0, number_of_project_files + 2):
                try:
                    main_file = self.driver.find_element_by_xpath(
                        '/html/body/main/article/section[2]/div[{:d}]]/div/pre/code'.format(i)).text
                    main_PY_file_count = 0
                    main_PY_file_count += 1
                    f = open("{:d}-main.py".format(i - 1), "w+")
                    f.write(main_file)
                except NoSuchElementException:
                    pass
            for i in range(0, number_of_project_files + 2):
                try:
                    main_file = self.driver.find_element_by_xpath(
                        '/html/body/main/article/section/div[{:d}]]/div/pre/code'.format(i)).text
                    main_PY_file_count = 0
                    main_PY_file_count += 1
                    f = open("{:d}-main.py".format(i - 1), "w+")
                    f.write(main_file)
                except NoSuchElementException:
                    pass

            print('\n')
            print("{:d} main.py files created".format(number_of_project_files))
            print('\n')
            print("GOOD LUCK WITH YOUR PROJECT")
            print('\n')
            print(directory_path)
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
            # if any(char.isdigit() for char in directory_search):
            # directory_name = directory_search
            # else:
            # pass
        try:
            project_title = self.driver.find_element_by_xpath(
                '/html/body/main/article/h1').text
        except NoSuchElementException:
            pass

        question_title_array = []

        for i in range(0, number_of_project_files + 1):
            try:
                question_title = self.driver.find_element_by_xpath(
                    '/html/body/main/article/section[2]/div[{:d}]/div/h4'.format(i)).text
                if any(char.isdigit() for char in question_title):
                    question_title_array.append(question_title)
                else:
                    pass
            except NoSuchElementException:
                pass
        for i in range(0, number_of_project_files + 1):
            try:
                question_title = self.driver.find_element_by_xpath(
                    '/html/body/main/article/section/div[{:d}]/div/h4'.format(i)).text
                if any(char.isdigit() for char in question_title):
                    question_title_array.append(question_title)
                else:
                    pass
            except NoSuchElementException:
                pass
        question_title_array = list(dict.fromkeys(question_title_array))
        question_title_array_without_mandatory = []
        substring = 'mandatory'
        substring2 = '#advanced'
        for question_title_array in question_title_array:
            if question_title_array.endswith(substring):
                remove_mandatory = question_title_array[:-(len(substring))]
                question_title_array_without_mandatory.append(remove_mandatory)
            elif question_title_array.endswith(substring2):
                remove_advanced = question_title_array[:-(len(substring2))]
                question_title_array_without_mandatory.append(
                    remove_advanced)

        question_description_array = []
        for i in range(0, number_of_project_files + 1):
            try:
                question_description = self.driver.find_element_by_xpath(
                    '/html/body/main/article/section[2]/div[{:d}]/div/p[1]'.format(i)).text
                question_description_array.append(question_description)
            except NoSuchElementException:
                pass
        f = open('README.md', "w+")
        f.write(
            "# {}\n## Description\n This project is part of {}:\n## Project tasks :wrench:\n".format(project_title, readme_repo_name))
        f = open('README.md', "a")
# CREATE README
        question_title_array = question_title_array_without_mandatory
        try:
            f.write(
                "### [{}](./{}) \n* {}\n".format(question_title_array[0], readme_file_name_array[0], question_description_array[0]))
        except IndexError:
            pass
        try:
            f.write(
                "### [{}](./{}) \n* {}\n".format(question_title_array[1], readme_file_name_array[1], question_description_array[1]))
        except IndexError:
            pass
        try:
            f.write(
                "### [{}](./{}) \n* {}\n".format(question_title_array[2], readme_file_name_array[2], question_description_array[2]))
        except IndexError:
            pass
        try:
            f.write(
                "### [{}](./{}) \n* {}\n".format(question_title_array[3], readme_file_name_array[3], question_description_array[3]))
        except IndexError:
            pass
        try:
            f.write(
                "### [{}](./{}) \n* {}\n".format(question_title_array[4], readme_file_name_array[4], question_description_array[4]))
        except IndexError:
            pass
        try:
            f.write(
                "### [{}](./{}) \n* {}\n".format(question_title_array[5], readme_file_name_array[5], question_description_array[5]))
        except IndexError:
            pass
        try:
            f.write(
                "### [{}](./{}) \n* {}\n".format(question_title_array[6], readme_file_name_array[6], question_description_array[6]))
        except IndexError:
            pass
        try:
            f.write(
                "### [{}](./{}) \n* {}\n".format(question_title_array[7], readme_file_name_array[7], question_description_array[7]))
        except IndexError:
            pass
        try:
            f.write(
                "### [{}](./{}) \n* {}\n".format(question_title_array[8], readme_file_name_array[8], question_description_array[8]))
        except IndexError:
            pass
        try:
            f.write(
                "### [{}](./{}) \n* {}\n".format(question_title_array[9], readme_file_name_array[9], question_description_array[9]))
        except IndexError:
            pass
        try:
            f.write(
                "### [{}](./{}) \n* {}\n".format(question_title_array[10], readme_file_name_array[10], question_description_array[10]))
        except IndexError:
            pass
        try:
            f.write(
                "### [{}](./{}) \n* {}\n".format(question_title_array[11], readme_file_name_array[11], question_description_array[11]))
        except IndexError:
            pass
        try:
            f.write(
                "### [{}](./{}) \n* {}\n".format(question_title_array[12], readme_file_name_array[12], question_description_array[12]))
        except IndexError:
            pass
        try:
            f.write(
                "### [{}](./{}) \n* {}\n".format(question_title_array[13], readme_file_name_array[13], question_description_array[13]))
        except IndexError:
            pass
        try:
            f.write(
                "### [{}](./{}) \n* {}\n".format(question_title_array[14], readme_file_name_array[14], question_description_array[14]))
        except IndexError:
            pass
        try:
            f.write(
                "### [{}](./{}) \n* {}\n".format(question_title_array[15], readme_file_name_array[15], question_description_array[15]))
        except IndexError:
            pass
        try:
            f.write(
                "### [{}](./{}) \n* {}\n".format(question_title_array[16], readme_file_name_array[16], question_description_array[16]))
        except IndexError:
            pass
        try:
            f.write(
                "### [{}](./{}) \n* {}\n".format(question_title_array[17], readme_file_name_array[17], question_description_array[17]))
        except IndexError:
            pass
        try:
            f.write(
                "### [{}](./{}) \n* {}\n".format(question_title_array[18], readme_file_name_array[18], question_description_array[18]))
        except IndexError:
            pass
        try:
            f.write(
                "### [{}](./{}) \n* {}\n".format(question_title_array[19], readme_file_name_array[19], question_description_array[19]))
        except IndexError:
            pass
        f = open('README.md', "a")
        f.write(
            '---\nCreated by [DT Van](https://github.com/dtvangogh)')


InstaBot('1661@holbertonschool.com', password)
