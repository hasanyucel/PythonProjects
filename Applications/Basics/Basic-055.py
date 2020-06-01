# Write a Python to find local IP addresses using Python's stdlib

import socket
print(socket.gethostbyname(socket.gethostname()))