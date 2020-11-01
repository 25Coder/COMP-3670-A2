import socket

#file name: client.py
#COMP 3670 Assignment 2 part 2
#Group members:
#Husin Sarhill
#Jalal Shabo
#Mohammad Khan
#Ethan Stewart

clientsock = socket.socket() #creating a client socket

name=socket.gethostname() #storing device name

ip=socket.gethostbyname(name) #storing IP address

clientsock.connect((ip,5555)) #attempting to connect

server_msg = clientsock.recv(1024).decode() #receiving data from server socket

print(server_msg)
data=input()

clientsock.send(data.encode())
server_msg2 = clientsock.recv(1024).decode()

if server_msg2 == "Server: Password is incorrect, terminating connection.":
    print(server_msg2)
    exit

else:
    while True:

        print("Enter a message to send to the server:")

        data=input() #message that will be sent to server will be in data

        clientsock.send(data.encode())    #sending the server our message

    
        ACK = clientsock.recv(1024).decode() #receiving any acknowledgement from server

        print(ACK) #printing acknowledgement from server

        if data=="bye": #"bye" is the message the client can use to terminate the connection
            print("Connection closed.")
            break
    
