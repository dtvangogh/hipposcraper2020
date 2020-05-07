Press a button and get the directories, project files, and main.c or main.c files made for your project of choice.
In the line that says  "choice project page" , just copy and paste the holberton project url you want on line 20 .
to access the intranet, you need a username and password so to run the files you need to create a separate file called

 "secrets" and inside the file write

password = "typepasswordhere"

for your username, remove mine and replace yours.

To use selenium

This part might be annoying for some of you.
Follow this tutorial to get started with selenium.
https://www.youtube.com/watch?v=d2GBO_QjRlo&t=302s

for mac type in terminal

pip3 install selenium

download chromedriver (if will be zipped file after it downloads unzip it so you have
something called chromedriver in your Downloads)

then move chromedriver to bin.
sudo mv ~/Downloads/chromedriver /usr/local/bin
if this doesn't work then instead of using ~ , write out the whole home directory.
go to the seleniumtest.py file and run with
python3 seleniumtest.py
if that works then move on
python3 makeAllfiles.py

I haven't tested all project urls and the biggest issue is the directory_path variable.

Sometimes the xpaths on holberton pages arent consistent so if you are experiencing an error,

find directory_path =

in makeAllfiles.py and you can type path yourself.

example: directory_path = 'holbertonschool-low-level/0x05sdfdas/'

The youtube video i posted guides you through the process.
main_file_array = ['0-main.c', '1-main.c', '2-main.c', '3-main.c', '4-main.c', '5-main.c', '6-main.c', '7-main.c', '8-main.c', '9-main.c', '10-main.c', '11-main.c', '12-main.c', '13-main.c', '14-main.c', '15-main.c', '16-main.c', '17-main.c', '18-main.c', '19-main.c']


main_file_array = []
		main_file_array.append('0-main.c')
		main_file_array.append('1-main.c')
		main_file_array.append('2-main.c')
		main_file_array.append('3-main.c')
		main_file_array.append('4-main.c')
		main_file_array.append('5-main.c')
		main_file_array.append('6-main.c')
		main_file_array.append('7-main.c')
		main_file_array.append('8-main.c')
		main_file_array.append('9-main.c')
		main_file_array.append('10-main.c')
		main_file_array.append('11-main.c')
		main_file_array.append('12-main.c')
		main_file_array.append('13-main.c')
		main_file_array.append('14-main.c')
		main_file_array.append('15-main.c')
		for main_file_array in main_file_array:
			try:
				lookup = 'gcc'
				myFile = open(main_file_array)
				for gcc_location, line in enumerate(myFile, 1):
						if lookup in line:
								location_minus1 = gcc_location - 1
				lookup = '$ cat'
				myFile = open(main_file_array)
				for cat_location, line in enumerate(myFile, 1):
						if lookup in line:
								cat_line_number = cat_location
				myFile = open(main_file_array, 'r+')
				data = myFile.read().splitlines(True)
				myFile = open(main_file_array, 'w')
				myFile.writelines(data[1:location_minus1])
			except FileNotFoundError:
				pass
			except UnboundLocalError:
				pass
