import socket
import struct
import sys

size = 4096
#Create socket
try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' +str(msg[0]) + ' . Eror message : ' + msg[1]
    sys.exit()

print 'Socket Created'

host = '127.0.0.1'  #Local host for testing
port = 3333         #Lucky numbered port

try:
    remote_ip = socket.gethostbyname( host )

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

print 'IP address of ' + host + ' is ' + remote_ip
#Make connection
s.connect((remote_ip , port))

version = 1
msg_type = 1
length = 4
amount_received = 0

#Send data to server
header = struct.pack("!BBH", version, msg_type, length)
amount_expected = len(header)
while 1:
    data = s.recv(size)
    payload = data[4:]
    s.sendall(header + payload)
print 'Received:', data
s.close()

print 'Socket Connected to ' + host + ' on ip ' + remote_ip


