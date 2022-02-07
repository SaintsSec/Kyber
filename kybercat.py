# Individually lined so that a reasoning for each import can be given.
import argparse
import socket # Used for networking.
import shlex
import subprocess # Used to initalize subprocessing abilities of python.
import sys # Used for system interaction.
import textwrap
import threading # Used for threading processes.


# Primary program.
class KyberCat: # Defines NetCat
    s = socket.socket
    def __init__(self, args, buffer='None'):
        self.args = args
        self.buffer = buffer
        self.s = s(s.AF_INET, s.SOCK_STREAM)
        self.s.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
    def execute(cmd):
        cmd = cmd.strip()
        if not cmd:
            return
        output = subprocess.check_output(shlex.split(cmd),
        stderr = subprocess.STDOUT)
        return output.decode()           
    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()

    def send(self):
        self.socket.connect((self.args.target, self.args.port))
        if self.buffer:
            self.s.send(self.buffer)

        try:
            while True:
                recv_len = 1
                response = ''
                while recv_len:
                    data = self.s.recv(4096)
                    recv_len = len(data)
                    response += data.decode()
                    if recv_len < 4096:
                        break
                    if response:
                        print(response)
                        buffer = input('> ')
                        buffer += '\n'
                        self.s.send(buffer.encode())

        except KeyboardInterrupt:
            print("User terminated")
            self.s.close()
            sys.exit()

    def listen(self): # Changed indentation by 1, as it was blanked out otherwise | Lines 56/98.
        s.socket.bind(self.args.target, self.args.port)
        self.s.listen(5)
        while True:
            client_socket, _= self.socket.accept()
            client_thread = threading.Thread(
                target=self.handle, args=(client_socket,)
            )
            client_thread.start()
            
    def handle(self, client_socket):
        if self.args.execute:
            output = execute(self.args.execute)
            client_socket.send(output.encode())
                
        elif self.args.upload:
            file_buffer = b''
            while True:
                data = client_socket.recv(4096)
                if data:
                    file_buffer += data
                else:
                    break
            with open(self.args.upload, 'wb') as f:
                f.write(file_buffer)
            message = f'saved file {self.args.upload}'
            client_socket.send(message.encode())
                
        elif self.args.command:
            cmd_buffer = b''
            while True:
                try:
                    client_socket.send(b'MCT: #> ')
                    while '\n' not in cmd_buffer.decode():
                        cmd_buffer += client_socket.recv(64)
                    response = execute(cmd_buffer.decode())
                    if response:
                        client_socket.send(response.encode())
                    cmd_buffer = b''
                except Exception as e:
                    print(f"server killed {e}")
                    self.socket.close()
                    sys.exit()

if __name__ == '__main__': # Prints fine in terminal | Lines 100/116.
    parser = argparse.ArgumentParser(
        description='''
           __  ___                _____    _                _   __ __     __          
          /  |/  /__  ___ _____  / ___/___(_)__ _______    (_) / //_/_ __/ /  ___ ____
         / /|_/ / _ \/ _ `/ __/ / /__/ __/ (_-</ __/ _ \  _   / ,< / // / _ \/ -_) __/
        /_/  /_/\___/\_,_/_/    \___/_/ /_/___/\__/\___/ (_) /_/|_|\_, /_.__/\__/_/   
                                                                  /___/  
        ''',
        formatter_class= argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''example:
            kybercat.py -t 192.168.1.108 -p 5555 -l -c # creates a command shell server
            kybercat.py -t 192.168.1.108 -p 5555 -l -u mytext.txt # upload to file
            kybercat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" # execute a command
            echo 'Moar Crisco' | ./netcat.py -t 192.168.1.108 -p 135 # echo text to server port 135
            kybercat.py -t 192.168.1.108 -p 5555 # connect to the command shell server\n\n
        '''))
    parser.add_argument('-c', '--command', action='store_true', help='command shell')
    parser.add_argument('-e', '--execute', help='execute a specific command')
    parser.add_argument('-l', '--listen', action='store_true', help='listen')
    parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')
    parser.add_argument('-t', '--target', default='192.168.1.203', help='specified target IP')
    parser.add_argument('-u', '--upload', help='upload file')
    
    args = parser.parse_args()
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read() # Prints this as an error if keyboard interupts using CTRL+C, though it shouldn't.
kc = KyberCat(args, buffer.encode())
kc.run()