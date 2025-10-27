import socket

serverName = ''
serverPort = 1200

serverS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverS.bind((serverName,serverPort))
print('The server has started on localhost at port: ' + str(serverPort))
serverS.listen(5)
print('The server is waiting for a request')

while True:
    clientS, address = serverS.accept()
    print('---------------------------------------')
    print('The client connected to %s on port %s' %address)
    sentence = clientS.recv(2048)
    print('Request from the client:' + str(sentence.decode("utf-8")))
    sentence1 = sentence.upper()
    print('Calculation from the server: ' + str(sentence1.decode("utf-8")))
    clientS.send(sentence1)
    clientS.close()
    print('Communication ended')

