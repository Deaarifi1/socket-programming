import socket
import codecs

serverName = ''
serverPort = 9999

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(10)
print(f'The server is running on port {serverPort}')

while True:
    clientSocket, address = serverSocket.accept()
    receive = clientSocket.recv(1024)

    request = receive.decode("utf-8")

    get = request[0:3]
    if get != 'GET': 
        break

    index = int(request.index('HTTP/1.'))

    path = request[4:index]
    folderCheck = path.count('/')
    folder = ''
    file = ''
    if folderCheck > 1:

        folder = path[path.find('/'):path.rfind('/')+1]

        file = path[path.rfind('/')+1:]
    else: 
        file = path[1:]
    
    if file.strip() == 'index.html':
        f = codecs.open(file, 'r', 'utf-8-sig')
        script = f.read()
        response = b + script.encode("utf-8")

    else:
         response = b
         
    clientSocket.sendall(response)
    clientSocket.close()