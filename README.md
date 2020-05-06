Press a button and get the directories, project files, and main.c or main.py files made for your project of choice.
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
