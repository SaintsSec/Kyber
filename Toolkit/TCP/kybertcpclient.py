import socket
print("""
                   __ __      __                         
                  / //_/_  __/ /_  ___  _____            
                 / ,< / / / / __ \/ _ \/ ___/            
                / /| / /_/ / /_/ /  __/ /                
               /_/ |_\__, /_.___/\___/_/                 
  ________________  /____/_____    ___________   ________
 /_  __/ ____/ __ \   / ____/ /   /  _/ ____/ | / /_  __/
  / / / /   / /_/ /  / /   / /    / // __/ /  |/ / / /   
 / / / /___/ ____/  / /___/ /____/ // /___/ /|  / / /    
/_/  \____/_/       \____/_____/___/_____/_/ |_/ /_/    
                  @ssgcythes
      """)
targetHost = input("Host IP or URL: ")
targetPort = int(input("Host port: "))
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