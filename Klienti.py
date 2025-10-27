import socket

serverName = 'localhost'
serverPort = 1200
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverName,serverPort))

var = input("You are connected to the server. Please enter your request: ")
s.sendall(str.encode(var))

message = ''
while True:
    data = s.recv(4)
    if len(data) <= 0:
        break
    message += data.decode("utf-8")
print('Data received from the server: ', message)
s.close()