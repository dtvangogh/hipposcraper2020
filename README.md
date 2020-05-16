## HIPPOSWEEPER
### Description
A selenium script that creates repositories, directories, project files, and main.c/main.py files, and very pretty README files
This script doesn't just create files...it fills the file with an include header line, comment bullets, and the prototype(if its a C project)

Example:
```
dtvan@dtvangogh:0x04-more_functions_nested_loops$ ls
0                      2-main.c               7-main.c
0-isupper.c            2-mul.c                7-print_diagonal.c
0-main.c               3-main.c               8-main.c
1-isdigit.c            3-print_numbers.c      8-print_square.c
1-main.c               4-main.c               9-fizz_buzz.c
10-main.c              4-print_most_numbers.c 9-main.c
10-print_triangle.c    5-main.c               README.md
100-prime_factor.c     5-more_numbers.c       holberton.h
101-print_number.c     6-main.c
12-main.c              6-print_line.c
dtvan@dtvangogh:0x04-more_functions_nested_loops$ cat 10-print_triangle.c
#include holberton.h

/**
*print_triangle-
*
*
*
*Return:
**/

void print_triangle(int size);
dtvan@dtvangogh:0x04-more_functions_nested_loops$
```
This script is going to open up chrome or a differnt webdriver or your choice, go to the intranet site, log in for you, go to the project page, and get the information it needs.

### Prerequisites
Pip3 install selenium
download chromedriver from http://chromedriver.storage.googleapis.com/index.html?path=78.0.3904.105/
unzip chromedriver so that file appears in downloads folder
```
sudo mv ~/Downloads/Chromedriver /usr/local/bin
```
if this doesn't work try typing out the ~ with the full path
if you get stuck watch this video:

 https://www.youtube.com/watch?v=d2GBO_QjRlo&t=302s

if you aren't on a mac sorry :n(

### File Contents
This repository contains the following files:

|   **File**   |   **Description**   |
| -------------- | --------------------- |
|sweep.py | the main file. Run by using python3 sweep.py |
|secrets.py | this is where you should store your password. Enter your password for password = 'insertPasswordHere'
|seleniumtest.py | just to test if your selenium is even working. compile with: python3 seleniumtest.py

### Usage and Installation
Clone the repository, compile with compilation flags, listed below, then run the executable.
```
$ git clone https://github.com/dtvangogh/hipposweeper
```
For username enter your own username. Find this line at the last line of the sweep.py file
```
InstaBot('1661@holbertonschool.com', password)
```
### Compilation
This code was compiled this way:
` $ python3 sweep.py 243 `
3rd Argument will choice what project you want. Project number is in the URL. Always a 3 digit number

###### Example usage

```
dtvan@dtvangogh:SWEEPER$ python3 sweep.py 241


Welcome to the HippoSweeper, Holberton's #1 Project Creator


You have selected "intranet.hbtn.io/projects/241"
0x03-python-data_structures
cd into /users/qpv2/holbertonschool-higher_level_programming/0x03-python-data_structures
Project files created:


0-print_list_integer.py
1-element_at.py
2-replace_in_list.py
3-print_reversed_list_integer.py
4-new_in_list.py
5-no_c.py
6-print_matrix_integer.py
7-add_tuple.py
8-multiple_returns.py
9-max_integer.py
10-divisible_by_2.py
11-delete_at.py
12-switch.py
100-print_python_list_info.c
13-is_palindrome.c, lists.h


15 main.py files created


GOOD LUCK WITH YOUR PROJECT


/users/qpv2/holbertonschool-higher_level_programming/0x03-python-data_structures
```



### Authors
[DT Van](github.com/dtvangogh)
