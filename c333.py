# -*- coding: utf-8 -*-
import socket
import msvcrt
import select
import time
import sys


def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code
name = raw_input("what your name?")
my_socet = socket.socket()
print my_socet.connect(("127.0.0.1", 44))
my_socet.send("name:" + name)
while True:
    if msvcrt.kbhit():
        data = ""
        while True:
            x = msvcrt.getch()
            if x == "\r":
                break
            data += x
            sys.stdout.write(x)
            sys.stdout.flush()
        if data == "e":
            my_socet.send("")
            break
        print
        time_ = time.strftime("%H:%M")
        if data[0] == "1":
            my_socet.send(data[1:])
        elif data[0] == "5":
            my_socet.send(time_ + " " + name + " " + "pravet:" + data[1:])
        elif data[0] == "2":
            my_socet.send("add:" + data[1:])
        elif data[0] == "4":
            my_socet.send("shut_up:" + data[1:])
        elif data[0] == "3":
            my_socet.send("go_away:" + data[1:])
        else:
            my_socet.send(time_ + " " + name + " " + data)
    read, w, x = select.select([my_socet], [], [], 0)
    for r in read:
        if r == my_socet:
            try_it = my_socet.recv(4096)
            print try_it
if __name__ == '__main__':
    main()