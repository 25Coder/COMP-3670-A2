import socket

#file name: server.py
#COMP 3670 Assignment 2 part 2
#Group members:
#Husin Sarhill
#Jalal Shabo
#Mohammad Khan
#Ethan Stewart


serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a server socket

name = socket.gethostname() #storing device name

print("Name of host device:"+name)

ip = socket.gethostbyname(name) #storing IP address

print("IP address of host:"+ip)

port = 5555

print("Ip Address:",ip," Port:",port)

adrs = (ip,port) #setting adrs with real IP and port number 5555

serversock.bind(adrs)   #binding our socket to adrs
print("Binding ok.")

serversock.listen(1)    #listening for client
print("Listening ok.")

clientsock,addr = serversock.accept()   #accepting client
print("Client accepted, connection ok.")

print("Authenticating client...")

msg1 = "Server: Please enter the password (1111): " #password is 1111
clientsock.send(msg1.encode())   

data = clientsock.recv(1024) #receiving password data from client socket
data = data.decode()
if data == "1111": #checking if password is correct
    print("Authentication ok.")
    msg2 = "Server: Password ok."
    clientsock.send(msg2.encode())   
    while True: #loops until client sends "bye"

        data = clientsock.recv(1024)    #receiving data from client socket

        data = data.decode()    #decoding data

        print("Client sent: '",data,"'")

        if data=="bye":         #checking for termination message
            bye = "Goodbye!"
            clientsock.send(bye.encode())   #sending Goodbye! to client
        
        if data=="bye": #new if statement is necessary as Goodbye! message wouldn't have been sent in time otherwise
            clientsock.close()  #closing the socket
            print("Closed connection to client.")
            break


        else : #if no termination message "bye"

            ACK = "Server: Your message was recieved, waiting for new message. Send 'bye' to close connection."

            clientsock.send(ACK.encode()) #sending acknowledgement to client
            
else: #if client enters wrong password
    msg3 = "Server: Password is incorrect, terminating connection."
    clientsock.send(msg3.encode())
    clientsock.close() #closing the socket
    print("Authentication failed, terminating connection.")
