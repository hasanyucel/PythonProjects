# Write a Python program to find files and skip directories of a given directory. 

import os
print([f for f in os.listdir('D:\PythonProjects\PythonProjects\Applications\Basics') if os.path.isfile(os.path.join('D:\PythonProjects\PythonProjects\Applications\Basics', f))])