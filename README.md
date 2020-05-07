## HIPPOSWEEPER
### Description
A selenium script that creates repositories, directory names, project files, and main.c/main.py files

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
For username enter your own username
```
InstaBot('1661@holbertonschool.com', password)
```
### Compilation
This code was compiled this way:
` $ python3 sweep.py 243 `
3rd Argument will choice what project you want. Project number is in the URL. Always a 3 digit number

###### Example usage

```
dtvan@dtvangogh:SWEEPER$ python3 sweep.py 243

"intranet.hbtn.io/projects/243"
IF DIRECTORY IS INCORRECT WRITE DIRECTORY NAME AS 4TH ARGUMENT
Foundations - Higher-level programming ― Python
0x04-python-more_data_structures
matrix
matrix
0x04-python-more_data_structures
/users/qpv2/holbertonschool-higher_level_programming/0x04-python-more_data_structures has been created
cd into /users/qpv2/holbertonschool-higher_level_programming/0x04-python-more_data_structures
Project files created:
['0-square_matrix_simple.py', '1-search_replace.py', '2-uniq_add.py', '3-common_elements.py', '4-only_diff_elements.py', '5-number_keys.py', '6-print_sorted_dictionary.py',
 '7-update_dictionary.py', '8-simple_delete.py', '9-multiply_by_2.py', '10-best_score.py', '11-mutiply_list_map.py', 'roman_string', '1-search_replace.py', '2-uniq_add.py',
 '3-common_elements.py', '4-only_diff_elements.py', '5-number_keys.py', '6-print_sorted_dictionary.py', '7-update_dictionary.py', '8-simple_delete.py', '9-multiply_by_2.py'
, '10-best_score.py', '11-mutiply_list_map.py', 'roman_string', '0-square_matrix_simple.py', 'search', 'search', '2-uniq_add.py', '3-common_elements.py', '4-only_diff_elements.py', '5-number_keys.py', '6-print_sorted_dictionary.py', 'value', '8-simple_delete.py', '9-multiply_by_2.py', 'None', '11-mutiply_list_map.py', 'roman_string']
README.md made
13 main.py files created
```
```



### Authors
DT Van
