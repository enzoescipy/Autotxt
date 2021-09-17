import os
import time
import shutil

with open("PUT_TXT_HERE/log_puttxthere.txt","w") as file:
    path = "./PUT_TXT_HERE"
    file_list = os.listdir(path)
    log = "\n".join(file_list)
    file.write(log)


os.system("Notepad.lnk")

newtxt_name = ""

with open("PUT_TXT_HERE/log_puttxthere.txt","r") as file:
    log = file.read()
    file_list = set(log.split("\n"))
    path = "./PUT_TXT_HERE"
    file_list_Now = set(os.listdir(path))
    new = file_list_Now - file_list
    newtxt_name = new.pop()

filedirectory_now = "PUT_TXT_HERE/{}".format(newtxt_name)
newtitle = ""
directory = ""

with open(filedirectory_now,"r") as file: ##readwritemode must be corrected NOW!:
    log = file.read()
    command_start = log.find("[[[") + 3
    command_end = log.find("]]]")
    log = log[command_start:command_end] # ex) "doc/is/name "i am dog" "
    title_start = log.find(" \"")
    directory = log[0:title_start]
    newtitle = log[title_start + 2:-1]
    directory = "MAIN/" + directory

try:
    if not os.path.exists(directory):
        os.makedirs(directory)
except OSError:
    print ('Error: Creating directory. ' +  directory)

newtxt_name = newtitle + ".txt"
    
shutil.move(filedirectory_now , directory + "/" +newtxt_name)