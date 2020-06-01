# Write a python program to get the path and name of the file that is currently executing.

import os
print("Path of File : ",os.path.realpath(__file__))


path = input("Please enter script name : ")
import subprocess
subprocess.run('python '+path, shell=True)
