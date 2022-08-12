import socket, threading, time
from os import system, name
sleep = time.sleep(3.0)
banner ="""
                   __ __      __                          
                  / //_/_  __/ /_  ___  _____             
                 / ,< / / / / __ \/ _ \/ ___/             
                / /| / /_/ / /_/ /  __/ /                 
               /_/ |_\__, /_.___/\___/_/                  
  ________________  /____/__ __________ _    ____________ 
 /_  __/ ____/ __ \   / ___// ____/ __ \ |  / / ____/ __ \\
  / / / /   / /_/ /   \__ \/ __/ / /_/ / | / / __/ / /_/ /
 / / / /___/ ____/   ___/ / /___/ _, _/| |/ / /___/ _, _/ 
/_/  \____/_/       /____/_____/_/ |_| |___/_____/_/ |_|  
"""

def clearScreen():
        # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

print(banner)
servIp = input("Enter an IP for your server: ")
servPort = int(input("Enter a port for the server: "))
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((servIp, servPort)) 
    server.listen(5)
    clearScreen()
    print(banner)
    print(f"\n[*] Listning on {servIp}:{servPort}")
    while True:
        client, address  = server.accept()
        print(f"[*] Accepted connection from {address[0]}:{address[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client, ))
        client_handler.start()
def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f"[*] Received: {request.decode()}")
        sock.send(b'\n\n\nWake up Neo....\nThe matrix has you...\nFollow the white rabbit...\n\n\n\n\nKnock knock Neo...\n\n')
main()                