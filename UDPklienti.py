import socket

serverName = 'localhost'
serverPort = 13000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect((serverName,serverPort))
out_data = input("Operation (IPADDRESS, PORT, COUNT, REVERSE, PALINDROME, TIME, GAME, GCF, CONVERT, ANAGRAM, SENTENCE)? ")
client.sendall(bytes(out_data,'UTF-8'))

while True:
  in_data =  client.recvfrom(128)
  out_data = input("Operation (IPADDRESS, PORT, COUNT, REVERSE, PALINDROME, TIME, GAME, GCF, CONVERT, ANAGRAM, SENTENCE)? ")
  client.sendall(bytes(out_data,'UTF-8'))
client.close()