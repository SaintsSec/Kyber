import socket
print("""
 ______________    ________          __ 
/_  __/ ___/ _ \  / ___/ (_)__ ___  / /_
 / / / /__/ ___/ / /__/ / / -_) _ \/ __/
/_/  \___/_/     \___/_/_/\__/_//_/\__/ 
            @cythesout
      """)
targetHost = input("What is the host (url or ip) you want to connect to:\n")
targetPort = int(input("What is the port number:\n"))
#create a socket object:
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to the client:
client.connect((targetHost, targetPort))
#send some data:
client.send(b'GET / HTTP/1.1\r\n\r\n')
#receive some data:
response = client.recv(4096)
print(response.decode('utf-8'))
client.close() 