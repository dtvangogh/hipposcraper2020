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
    # CHOOSE PROJECT PAGE
        project_url = "\"intranet.hbtn.io/projects/{}\"".format(argv[1])
        print('\n')
        print(
            "Welcome to the HippoSweeper, Holberton's #1 Project Creator")
        print('\n')
        print("You have selected {}".format(project_url))
        self.driver.get(
            "https://intranet.hbtn.io/projects/{:s}".format(argv[1]))

    # GET REPO NAME
        try:
            readme_repo_name = self.driver.find_element_by_xpath(
                '/html/body/main/article/p[1]/small').text
            if readme_repo_name[14] == 'L':
                repo_name = 'holbertonschool-low_level_programming'
            elif readme_repo_name[14] == 'H':
                repo_name = 'holbertonschool-higher_level_programming'
        except NoSuchElementException:
            pass
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

# GET FILE NAMES
        file_name_array = []
        for i in range(0, 36):
            try:
                file_name = self.driver.find_element_by_xpath(
                    '/html/body/main/article/section[2]/div[{:d}]/div/ul[2]/li[3]/code'.format(i)).text
                file_name_array.append(file_name)
            except NoSuchElementException:
                pass
            try:
                file_name = self.driver.find_element_by_xpath(
                    '/html/body/main/article/section[2]/div[{:d}]/div/ul[3]/li[3]/code'.format(i)).text
                file_name_array.append(file_name)
            except NoSuchElementException:
                pass

            try:
                file_name = self.driver.find_element_by_xpath(
                    '/html/body/main/article/section/div[{:d}]/div/ul[2]/li[3]/code'.format(i)).text
                file_name_array.append(file_name)
            except NoSuchElementException:
                pass

            try:
                file_name = self.driver.find_element_by_xpath(
                    '/html/body/main/article/section/div[{:d}]/div/ul/li[3]/code'.format(i)).text
                file_name_array.append(file_name)
            except NoSuchElementException:
                pass
            try:
                file_name = self.driver.find_element_by_xpath(
                    '/html/body/main/article/section[2]/div[{:d}]/div/ul[5]/li[3]/code'.format(i)).text
                file_name_array.append(file_name)
            except NoSuchElementException:
                pass
# GET PROTOTYPE
        prototype_array = []
        semicolon = ";"
        if repo_name == 'holbertonschool-low_level_programming':
            for i in range(0, 21):
                try:
                    prototype = self.driver.find_element_by_xpath(
                        '/html/body/main/article/section[2]/div[{:d}]/div/ul[1]/li/code'.format(i)).text
                        ##ONLY APPEND IF PROTOTYPE, IF ; CHARACTER EXISTS
                    if (semicolon in prototype):
                        prototype_array.append(prototype)
                    else:
                        pass
                except NoSuchElementException:
                    pass
            for i in range(0, 21):
                try:
                    prototype = self.driver.find_element_by_xpath(
                        '/html/body/main/article/section[2]/div[{:d}]/div/ul[1]/li[1]/code'.format(i)).text
                    if (semicolon in prototype):
                        prototype_array.append(prototype)
                    else:
                        pass
                except NoSuchElementException:
                    pass
            for i in range(0, 21):
                try:
                    prototype = self.driver.find_element_by_xpath(
                        '/html/body/main/article/section/div[{:d}]/div/ul[1]/li/code'.format(i)).text
                    if (semicolon in prototype):
                        prototype_array.append(prototype)
                    else:
                        pass
                except NoSuchElementException:
                    pass
            for i in range(0, 21):
                try:
                    prototype = self.driver.find_element_by_xpath(
                        '/html/body/main/article/section/div[{:d}]/div/ul[1]/li[1]/code'.format(i)).text
                    if (semicolon in prototype):
                        prototype_array.append(prototype)
                    else:
                        pass
                except NoSuchElementException:
                    pass
        prototype_array = list(dict.fromkeys(prototype_array))
        edited_prototype_array = []
        lets_edit_prototype_array = prototype_array
        directory_path = '/users/qpv2/' + repo_name + '/' + directory_name
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
##Edit file name string if more than one file
##MULTIPLE FILES IN ONE
        for i in range(0, number_of_project_files):
            try:
                index = [idx for idx, s in enumerate(file_name_array) if ',' in s][0]
                find_comma = file_name_array[index].find(',')
                no_comma = file_name_array[index][:find_comma]
                second_file = file_name_array[index][find_comma + 2:]
                if (',' not in second_file):
                    file_name_array.append(second_file)
                find_comma = second_file.find(',')
                second_file_no_comma = second_file[:find_comma]
                file_name_array.append(second_file_no_comma)
                file_name_array[index] = no_comma
                locate_space = second_file.find(' ')
                third_file = second_file[locate_space + 1:]
                if (',' not in third_file):
                    file_name_array.append(third_file)
                find_comma = third_file.find(',')
                third_file_alone = third_file[:find_comma]
                if (',' not in third_file_alone):
                    file_name_array.append(third_file_alone)
                find_space = third_file.find(' ')
                fourth_file = third_file[find_space + 1:]
                if (',' not in fourth_file):
                    file_name_array.append(fourth_file)
                find_comma = fourth_file.find(',')
                fourth_file_alone = fourth_file[:find_comma]
                if (',' not in fourth_file_alone):
                    file_name_array.append(fourth_file_alone)
                find_space = fourth_file.find(' ')
                fourth_file_alone = fourth_file[find_space + 1:]
                if (',' not in fourth_file_alone):
                    file_name_array.append(fourth_file_alone)
            except IndexError:
                pass
    ##FILTER FILE NAME ARRAY
        file_name_array = list(dict.fromkeys(file_name_array))
        file_name_array = [x for x in file_name_array if len(x) > 5]
        file_name_array = [x for x in file_name_array if x[-1] != '.']
        file_name_array = [x for x in file_name_array if '.' in x]
        file_name_array = [x for x in file_name_array if len(x) < 32]
        file_name_array = [x for x in file_name_array if x[0] != '.']
        file_name_array = [x for x in file_name_array if x[-1] != 'x']
        file_name_array = [x for x in file_name_array if '=' not in x]
        file_name_array = [x for x in file_name_array if '_' not in x]
        file_name_array = [x for x in file_name_array if '<' not in x]
    ##Make file_name_array2
        file_name_array2 = []
        file_name_array2 = [x for x in file_name_array if '/' in x]
        readme_file_name_array = []
        number_of_project_files = len(file_name_array)
        readme_file_name_array = file_name_array
        print("--------------------------------------------------------------------------------------------")
        print("Project files created:")
        print('--------------------------------------------------------------------------------------------')
 ##get C prototypes
        if repo_name == 'holbertonschool-low_level_programming':
            header = 'holberton.h'
            try:
                if argv[2]:
                    header = argv[2]
            except IndexError:
                pass
            i = 1;
            for file_name_array in file_name_array:
                print(file_name_array)
                try:
                    find_prototype = self.driver.find_element_by_xpath(
                    '/html/body/main/article/section[2]/div[{:d}]/div/ul[1]/li/code'.format(i)).text
                except NoSuchElementException:
                    try:
                            find_prototype = self.driver.find_element_by_xpath(
                            '/html/body/main/article/section[2]/div[{:d}]/div/ul[1]/li[1]/code'.format(i)).text
                    except NoSuchElementException:
                        try:
                                find_prototype = self.driver.find_element_by_xpath(
                                '/html/body/main/article/section/div[{:d}/div/ul[1]/li/code'.format(i)).text
                        except NoSuchElementException:
                            try:
                                    find_prototype = self.driver.find_element_by_xpath(
                                    '/html/body/main/article/section/div[{:d}]/div/ul[1]/li[1]/code'.format(i)).text
                            except NoSuchElementException:
                                    find_prototype = 'no prototype'
                    i += 1
    ##EDIT PROTOTYPE FOR COMMENTS SECTION
                copy_of_find_prototype = find_prototype
                find_space = copy_of_find_prototype.find(' ')
                find_parentheses = copy_of_find_prototype.find('(')
                edited_comment_prototype = copy_of_find_prototype[find_space + 1:find_parentheses]
                edited_comment_prototype = edited_comment_prototype + '-'
                with open("{}".format(file_name_array), "w") as f:
                    f.write(
                        "#include \"{:s}\"\n\n/**\n*{:s}\n*\n*\n*\n*Return:\n**/\n\n{:s}\n".format(header, edited_comment_prototype, find_prototype[:-1]))
    ##MAKE PY FILES and FIND PROTOTYPE
        i = 1
        if repo_name != 'holbertonschool-low_level_programming':
            for file_name_array in file_name_array:
                if '/' not in file_name_array:
                    print(file_name_array)
                try:
                    find_prototype = self.driver.find_element_by_xpath(
                    '/html/body/main/article/section[2]/div[{:d}]/div/ul[1]/li/code'.format(i)).text
                except NoSuchElementException:
                    try:
                        find_prototype = self.driver.find_element_by_xpath(
                        '/html/body/main/article/section[2]/div[{:d}]/div/ul[1]/li[1]/code'.format(i)).text
                    except NoSuchElementException:
                        try:
                            find_prototype = self.driver.find_element_by_xpath(
                            '/html/body/main/article/section/div[{:d}/div/ul[1]/li/code'.format(i)).text
                        except NoSuchElementException:
                            try:
                                find_prototype = self.driver.find_element_by_xpath(
                                '/html/body/main/article/section/div[{:d}]/div/ul[1]/li[1]/code'.format(i)).text
                            except NoSuchElementException:
                                find_prototype = 'no prototype'
                if ':' not in find_prototype:
                        find_prototype = 'no prototype'
                i += 1
                if repo_name == 'holbertonschool-higher_level_programming':
                    try:
                        with open("{}".format(file_name_array), "w") as f:
                            f.write("#!/usr/bin/python3\n{:s}\n".format(find_prototype))
                    except FileNotFoundError:
                        pass
        try:
            first_element = file_name_array2[0]
            directory2 = first_element[0:(first_element.find('/'))]
            print(directory2)
            directory_path2 = directory_path + '/' + directory2
            if not os.path.exists(directory_path2):
                os.makedirs(directory_path2)
                print("Creating: {:s}".format(directory_path2))
        except IndexError:
            pass
# CD INTO DIRECTORY TO PLACE FILES IN IT
        try:
            os.chdir(directory_path2)
            print("cd into {:s}".format(directory_path2))
        except UnboundLocalError:
            pass
        for file_name_array2 in file_name_array2:
            try:
                with open("{}".format(file_name_array2), "w") as f:
                            f.write("This is a test file")
            except FileNotFoundError:
                pass
            print(file_name_array2)

##make HOLBERTON.H
        os.chdir(directory_path)
        print("cd into {:s}".format(directory_path))
        if repo_name == 'holbertonschool-low_level_programming':
            with open("{:s}".format(header), "w") as f:
                f.write("#ifndef HOLBERTON_\n#define HOLBERTON_\n\n#include <stdlib.h>\n#include <stdio.h>\n#include <string.h>\n#include <unistd.h>\n#include <stdarg.h>\n#include <sys/types.h>\n#include <fcntl.h>\n\n")
            with open("{:s}".format(header), "a") as f:
                for prototype_array in prototype_array:
                    f.write("{:s}\n".format(prototype_array))
            with open("{:s}".format(header), "a") as f:
                f.write("#endif\n")
# FIND MAIN.C FILES SECTION/DIV[1]/div/pre/code
# if any(char.isdigit() for char in directory_search):
        # directory_name = directory_search
        # else:
        # pass
        if repo_name == 'holbertonschool-low_level_programming':
            main_file_name_array = []
            for i in range(1, number_of_project_files + 2):
                try:
                    main_file = self.driver.find_element_by_xpath(
                        '/html/body/main/article/section/div[{:d}]/div/pre/code'.format(i)).text
                    main_file_name = main_file[(main_file.find("$ cat ") + 6):(main_file.find("main.c")) + 6]
                    main_file_name_array.append(main_file_name)
                    try:
                        f = open("{:s}".format(main_file_name), "w+")
                        f.write(main_file)
                    except FileNotFoundError:
                        pass
                except NoSuchElementException:
                    for i in range(1, 22):
                        try:
                            main_file = self.driver.find_element_by_xpath(
                                '/html/body/main/article/section[2]/div[{:d}]/div/pre/code'.format(i)).text
                            main_file_name = main_file[(main_file.find("$ cat ") + 6):(main_file.find("main.c\n#")) + 6]
                            main_file_name_array.append(main_file_name)
                            try:
                                f = open("{:s}".format(main_file_name), "w+")
                                f.write(main_file)
                            except FileNotFoundError:
                                pass
                        except NoSuchElementException:
                                pass
            if os.path.exists("{:s}/holberton.h".format(directory_path)):
                print('holberton.h created')

# MAKE MAIN.PY FILES
        if repo_name != 'holbertonschool-low_level_programming':
            main_file_name_array = []
            for i in range(1, 22):
                try:
                    main_file = self.driver.find_element_by_xpath(
                        '/html/body/main/article/section[2]/div[{:d}]/div/pre/code'.format(i)).text
                    main_PY_file_count = 0
                    main_PY_file_count += 1
                    main_file_name = main_file[(main_file.find("$ cat ") + 6):(main_file.find("main.py")) + 7 ]
                    main_file_name_array.append(main_file_name)
                    f = open("{:s}".format(main_file_name), "w+")
                    f.write(main_file)
                except (NoSuchElementException, FileNotFoundError) as e:
                    try:
                        main_file = self.driver.find_element_by_xpath(
                            '/html/body/main/article/section/div[{:d}]/div/pre/code'.format(i)).text
                        main_PY_file_count = 0
                        main_PY_file_count += 1
                        main_file_name = main_file[(main_file.find("$ cat ") + 6):(main_file.find("main.py")) + 7 ]
                        main_file_name_array.append(main_file_name)
                        f = open("{:s}".format(main_file_name), "w+")
                        f.write(main_file)
                    except NoSuchElementException:
                        pass
                    except FileNotFoundError:
                        pass

# EDIT MAIN FILES
# EDIT MAIN.PY

#Filter main file array
        main_file_name_array = [x for x in main_file_name_array if len(x) >= 3]
        main_file_name_array = [x for x in main_file_name_array if len(x) < 21]
        main_file_name_array = [x for x in main_file_name_array if '.' in x]
        main_file_name_array = list(dict.fromkeys(main_file_name_array))
        if repo_name != 'holbertonschool-low_level_programming':
            main_file_name_array = [x for x in main_file_name_array if x[-3] == '.']
        if repo_name == 'holbertonshool-low_level_programming':
            main_file_name_array = [x for x in main_file_name_array if x[-2] == '.']
        print("README.md created")
        print('-----------------------------------------------------------------------------------------')
        print('Main files created:')
        print('-----------------------------------------------------------------------------------------')
        if repo_name != 'holbertonschool-low_level_programming':
            for main_file_name_array in main_file_name_array:
                print(main_file_name_array)
                try:
                    lookup = '$ ./'
                    myFile = open(main_file_name_array)
                    for gcc_location, line in enumerate(myFile, 1):
                        if lookup in line:
                            location_minus1 = gcc_location - 1
                    lookup = '$ cat'
                    myFile = open(main_file_name_array)
                    for cat_location, line in enumerate(myFile, 1):
                        if lookup in line:
                            cat_line_number = cat_location
                    myFile = open(main_file_name_array, 'r+')
                    data = myFile.read().splitlines(True)
                    myFile = open(main_file_name_array, 'w')
                    myFile.writelines(data[cat_line_number:location_minus1])
                except FileNotFoundError:
                    pass
                except UnboundLocalError:
                    pass
        if repo_name == 'holbertonschool-low_level_programming':
            for main_file_name_array in main_file_name_array:
                print(main_file_name_array)
                try:
                    lookup = 'gcc'
                    myFile = open(main_file_name_array)
                    for gcc_location, line in enumerate(myFile, 1):
                        if lookup in line:
                            location_minus1 = gcc_location - 1
                    lookup = '$ cat'
                    myFile = open(main_file_name_array)
                    for cat_location, line in enumerate(myFile, 1):
                        if lookup in line:
                            cat_line_number = cat_location
                    myFile = open(main_file_name_array, 'r+')
                    data = myFile.read().splitlines(True)
                    myFile = open(main_file_name_array, 'w')
                    myFile.writelines(data[cat_line_number:location_minus1])
                except FileNotFoundError:
                    pass
                except UnboundLocalError:
                    pass
            # if any(char.isdigit() for char in directory_search):
            # directory_name = directory_search
            # else:
            # pass
        print("----------------------------------------------------------------------------------------")
        print("GOOD LUCK WITH YOUR PROJECT")
        print('\n')
        print(directory_path)
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
                question_title_array_without_mandatory.append(remove_advanced)

        question_description_array = []
        for i in range(0, number_of_project_files + 1):
            try:
                question_description = self.driver.find_element_by_xpath(
                    '/html/body/main/article/section[2]/div[{:d}]/div/p[1]'.format(i)).text
                question_description_array.append(question_description)
            except NoSuchElementException:
                try:
                    question_description = self.driver.find_element_by_xpath(
                        '/html/body/main/article/section/div[{:d}]/div/p[1]'.format(i)).text
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
