#!/usr/bin/python
# test program to automatically run commands to conduct simulations

#### some basic commands
###########################################
###########################################
#print(os.getcwd())  # pwd
#print(os.listdir()) # ls
#os.chdir('../')    # cd ../
#os.mkdir('testdirectory')  # mkdir
#os.mkdirs('testdir/subtestdir')    # allow tree structures of directories
#os.rmdir('testdir')
#os.removedirs('testdir/subtestdir')   # delete all sub diretories
#os.rename('originalname.txt', 'targetname.txt')
#print(os.stat('target.txt').st_size)   # show file size in bytes
###########################################
###########################################

import os
import subprocess as subp


# define parameters
v_all = ['1', '2', '3', '4']


# create multiple directories
print(os.getcwd())  #eql. to pwd
print(os.listdir()) #eql. to ls
for v in v_all:
    new_directory_name = 'v'+v      #create directory names of the character v plus each value in v_all.
    os.mkdir(new_directory_name)    #create directories named by the created value "new_directory_name". Errors occur when the directory name has exsisted.
    os.rmdir(new_directory_name)   #delete directories named by the created value "new_directory_name".
print(os.listdir()) #eql. to ls

# shell=True necessary when the commands are built in shell
# shell=True allows input the entire command as a string and execute (eqvlt. to subp.run(['ls, -la']))
# subp.run('ls -la', shell=True)

