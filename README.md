# Socket Programming Project

This project contains several Python scripts demonstrating **socket programming** using TCP and UDP protocols.

## Files in the project

- **Klienti.py / Server.py** - Simple TCP client and server that send and receive messages.
- **TCPklienti.py / TCPserveri.py** - TCP client and multi-threaded server that support multiple operations like IPADDRESS, PORT, PALINDROME, REVERSE, GCF, GAME, TIME, COUNT, ANAGRAM, SENTENCE, CONVERT.
- **UDPklienti.py / UDPserver.py** - UDP client and server implementing similar operations as TCP server.
- **webServer.py** - Simple web server that listens on port 9999 and responds to HTTP GET requests.

## How to run

1. Start the server first (`Server.py`, `TCPserveri.py`, `UDPserver.py`, or `webServer.py` depending on which you want to test).
2. Run the corresponding client script (`Klienti.py`, `TCPklienti.py`, `UDPklienti.py`).
3. Follow the input prompts to test the operations.

## Notes

- Make sure the server and client use the same port.
- TCP servers are multi-threaded, UDP is connectionless.
- Python 3 is required.