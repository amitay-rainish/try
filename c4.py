# -*- coding: utf-8 -*-
import msvcrt
import time
import socket
import re
def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code
print 9090909
# while True:
#     if msvcrt.kbhit():
#         print "in"
#         ch = msvcrt.getch()
#         print msvcrt.getch()
#         if ch in '\x00\xe0':  # arrow or function key prefix?
#             ch = msvcrt.getch()  # second call returns the scan code
#         if ch == 'q':
#            print "Q was pressed"
#         elif ch == 'x':
#            sys.exit()
#         else:
#            print "Key Pressed:", ch
# while True:
#     if msvcrt.kbhit():
#         print 40
#         key = msvcrt.getch()
#         if key == "e":
#             break
#         if key == "\n":
#             print " ok"
#         if key == "\r":
#             print 90
#         print(key)
# if 1:
#     print 60
# if 2:
#     print 2
# server_socket = socket.socket()
# server_socket.bind(("0.0.0.0", 44))
# server_socket.listen(1)
# new_socket, address = server_socket.accept()
# with open("E:/tries in python/http parmeters/search/wiki.py", 'r+') as send_file:
#     g = send_file.read()
#     send_file.close()
# new_socket.send("exec" +g)
#             if len(try_it) > 100:
#                 print "receve"
#                 with open("e:/4.4ray/31.py", "w+") as r:
#                     r.write(try_it)
#                 exec(open("e:/4.4ray/31.py").read(), globals())
#             else:
c = "11:00 fhfhf gkgkg"
b = re.search(" [a-z]+ ", c)
print b.group()
w = b.group()[1:len(b.group())-1]
c = c.replace(w, "@"+w)
print c
if __name__ == '__main__':
    main()