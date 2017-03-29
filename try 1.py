# -*- coding: utf-8 -*-
import socket
import select
import re

def fuction():
    with open("E:/tries in python/http parmeters/search/wiki.py", 'r+') as send_file:
        g = send_file.read()
        send_file.close()
    return g


def send_file(write, not_to):
    for massge in massge_to_send:
        (clien_soket, data) = massge
        if clien_soket in write and current_soket != not_to:
            print "send"
            clien_soket.send(data)
            massge_to_send.remove(massge)


def send_data(data, current_soket, pravat=0):
    if current_soket not in shut_up:
        if pravat == 0:
            for o in clients_names:
                socket_ = clients_names[o]
                if current_soket != socket_:
                    try:
                        if shut_up[o] == current_soket:
                            print "dont send"
                    except:
                        if current_soket in mangers:
                        #     n = re.search(" [a-z]+ ", data)
                        #     print n
                        #     name = n.group()[1:len(n)-1]
                        #     data.replace(name, "@" + name)
                        #     socket_.send(data)
                            socket_.send("@" + data)
                        else:
                            socket_.send(data)
        else:
            socket_ = clients_names[pravat]
            socket_.send(data)
    else:
        current_soket.send("you cant speak")




def name_to_send(data):
    data1 = re.findall(":[a-z]+", data)
    d = data1[0]
    back = d[1:len(d)]
    return back


def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 44))
server_socket.listen(3)
clients = []
mangers = []
massge_to_send = []
clients_names = {}
i = 0
receve = {}
shut_up = []
while True:
    read, write, eror = select.select([server_socket] + clients, clients, [], 20)
    for current_soket in read:
        #print server_socket
        if current_soket is server_socket:
            (new_socket, address) = server_socket.accept()
            #print current_soket, new_socket, server_socket
            if len(clients) == 0:
                mangers.append(new_socket)
            clients.append(new_socket)
            print clients_names
            i += 1
        else:
            data = current_soket.recv(1024)
            print data
            if "name:" in data:
                clients_names[data[5:]] = new_socket
            receve[i] = data
            if data == "":
                x = "no one"
                for name, soc in clients_names.items():
                    if soc == current_soket:
                        x = name
                clients.remove(current_soket)
                send_data(x + " has left the room", current_soket)
                print "##########"
            else:
                if "pravet:" in data:
                    send_data(data, clients_names, name_to_send(data))
                elif "shut_up:" in data and current_soket in mangers:
                    shut_up.append(clients_names[name_to_send(data)])
                    print shut_up
                elif "add:" in data:
                    if current_soket in mangers:
                        key = name_to_send(data)
                        print key
                        print clients_names
                        mangers.append(clients_names[key])
                        print mangers
                elif "go_away:" in data and current_soket in mangers:
                    clients.remove(clients_names[name_to_send(data)])
                    del clients_names[name_to_send(data)]

                else:
                    if "name:" not in data:
                        send_data(data, current_soket)



if __name__ == '__main__':
    main()