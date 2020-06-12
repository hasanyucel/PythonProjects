# Write a Python program to find the available built-in modules.

help('modules') 

#w3sources answer
import sys
import textwrap
module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=70))