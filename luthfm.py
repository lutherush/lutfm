# This is simple file manager writen in python.
# I made it during selection process as python developer, had no idea
# what to make in 30 minutes. 
#
#


import os
import shutil

print("Please enter your command: (See Below for the commands)")
print("HINT:\nCreate file - file_create <FNAME>")
print("Delete file - file_delete <FNAME>")
print("Copy file - file_copy <FNAME> <FNAME>")
print("Move file - file_move <FNAME> <DESTINATION>")
print("Create directory - create_dir <FNAME>")
print("Delete directory - delete_dir <FNAME>")
print("Copy directory - copy_dir <FNAME> <FNAME>")
print("Move directory - move_dir <FNAME> <DESTINATION>")

str = input().split()
if str == []:
    print("Something wrong with command and arguments")
    exit(1)
try:
    str[1]
except:
    print("Something wrong with command and arguments")
if str[0] == "file_create":
    fname = str[1]
    open(fname, 'a')
elif str[0] == "file_delete":
    A = os.listdir()
    if str[1] in A:
        os.remove(str[1])
        print(str[1])
    else:
        print("No such file")
elif str[0] == "create_dir":
    A = os.listdir()
    try:
        os.mkdir(str[1])
    except:
        print("There is a directory with such name")
elif str[0] == "delete_dir":
    try:
        shutil.rmtree(str[1])
    except:
        print("There is no such directory")
elif str[0] == "file_copy":
    try:
        shutil.copy(str[1], str[2])
    except:
        print("Something went wrong")
elif str[0] == "file_move":
    try:
        shutil.move(str[1], str[2])
    except:
        print("Something went wrong")
elif str[0] == "copy_dir":
    try:
        shutil.copytree(str[1], str[2])
    except:
        print("Something went wrong")
elif str[0] == "move_dir":
    try:
        if str[1] == str[2]:
            print("No need for moving the directory")
        else:
            shutil.copytree(str[1], str[2])
            shutil.rmtree(str[1])
    except:
        print("Something went wrong")
else:
    print("Wrong command")

