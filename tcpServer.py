import socket, threading
print("""
 ______________    ____                    
/_  __/ ___/ _ \  / __/__ _____  _____ ____
 / / / /__/ ___/ _\ \/ -_) __/ |/ / -_) __/
/_/  \___/_/    /___/\__/_/  |___/\__/_/ 
""")
servIp = input("Enter an IP for your server: ")
servPort = int(input("Enter a port for the server: "))
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((servIp, servPort)) 
    server.listen(5)
    print(f"[*] Listning on {servIp}:{servPort}")
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