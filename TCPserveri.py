import socket, threading
from random import seed
from random import sample
import datetime
from string import punctuation
import re

serverName = ''
serverPort = 13000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((serverName,serverPort))

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
    def run(self):
        msg = ''
        while True:
            data = self.csocket.recv(128)
            msg = data.decode()
            def ops(msg):
                if msg == 'IPADDRESS':
                    return Ipaddress()
                elif msg == 'PORT':
                    return Port()
                elif msg == 'PALINDROME':
                    return Palindrome()
                elif msg == 'REVERSE':
                    return Reverse()
                elif msg == 'GCF':
                    return Gcf()
                elif msg == 'GAME':
                    return Game()
                elif msg == 'TIME':
                    return Time()
                elif msg == 'COUNT':
                    return Count()
                elif msg == 'ANAGRAM':
                    return Anagram()
                elif msg == 'SENTENCE':
                    return Sentence()
                elif msg == 'CONVERT':
                    return Convert()
                else:
                    return print("This operation does not exist")

            def Palindrome():
                text = input("Text? ")
    
                text = text.lower()
                rev_str = reversed(text)
                if list(text) == list(rev_str):
                    print("Response: The given text is a palindrome ")
                else:
                    print("Response: The given text is not a palindrome ")

            def Ipaddress():
                print('Response: The client’s IP address is: %s ' % clientAddress[0])

            def Port():
                 print('Response: The client is using port %s ' % clientAddress[1])

            def Reverse():
                string = input("Text? ")
                string = string[::-1] 
                print("Response: ",string)

            def Gcf():
                a=int(input(''))
                b=int(input(''))
                def gcf(m,n):
                    z=abs(m-n)
                    if (m-n)==0:
                       return n
                    else:
                       return gcf(z,min(m,n))
                print ("Response: ", gcf(a,b))

            def Game():
                seed(1)
                sequence = [i for i in range(1,35)]
                subset = sample(sequence, 5)
                sequence = sorted(subset)
                print("Response: ",sequence, "These are 5 random numbers from 35 ")

            def Time():
                currentDT = datetime.datetime.now()
                print (currentDT.strftime("Response: %d.%m.%Y %H:%M:%S"))

            def Count():
                text = input ("Text? ")
    
                table = str.maketrans('', '', punctuation)
                text = text.translate(table).lower().replace(' ', '')
                vowels = set('aeiou')
    
                consonants = sum(i not in vowels for i in text)
                vowels = sum(i in vowels for i in text)
    
                print("Response: The received text contains",vowels,"vowels and",consonants,"consonants ")

            def Anagram():
                s1 = input("Text? ")
                s2 = input("Text? ")
                s1 = s1.lower()
                s2 = s2.lower()
                s1=list(s1);s1.sort()
                s2 = list(s2);s2.sort()
                if s1 == s2:
                    print ("Response: The words are anagrams")
                else:
                    print ("Response: The words are not anagrams")

            def Sentence():
                text = input("Text? ")
    
                punc_filter = re.compile('([.!?]\s*)')
                split_with_punctuation = punc_filter.split(text)
                final = ''.join([i.capitalize() for i in split_with_punctuation])
                print("Response: " ,final)

            def Convert():
    
                x = input("Text? ")
                def Convert(x):
                    if x == 'cmToFeet':
                        return ConvertCenti()
                    elif x == 'FeetToCm':
                        return ConvertFeet()
                    elif x == 'kmToMiles':
                        return ConvertKm()
                    elif x == 'MilesToKm':
                        return ConvertMiles()
                    else:
                        return print("!!!")
        
                def ConvertCenti():
                    def Conversion(centi): 
                        feet = 0.0328 * centi 
                        print ("Response: ",round(feet, 2),"ft") 
                    centi = int(input("Enter cm: "))
                    Conversion(centi)

                def ConvertFeet():
                    def Conversion(feet): 
                        centi = 30.48 * feet
                        print ("Response: ",round(centi, 2), "cm")
                    feet = int(input("Enter feet: "))
                    Conversion(feet)

                def ConvertKm():
                    def Conversion(km): 
                        miles = 0.621371 * km
                        print ("Response: ",round(miles, 2),"miles") 
                    km = int(input("Enter km: "))
                    Conversion(km)

                def ConvertMiles():
                    def Conversion(miles): 
                        km = 1.609 * miles
                        print ("Response: ",round(km, 2),"km") 
                    miles = int(input("Enter miles: "))
                    Conversion(miles)
                Convert(x)
            ops(msg)
            self.csocket.send(bytes(msg,'UTF-8'))  
while True:
    server.listen(5)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()