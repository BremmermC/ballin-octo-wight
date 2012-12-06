import socket
import struct
import sys
from thread import *

HOST = ''	# Anything Available
PORT = 3333	# Lucky numbered port
size = 4096
data = 0
#Create Server Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

#Bind and listen
try:
	s.bind((HOST, PORT))
except socket.error , msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
	
print 'Socket bind complete'

s.listen(1)
while True:
    print 'Socket listening'
    print 'waiting for connection...'
    client, address = s.accept()
    print '...connected from:', addr
    if data:
        data = client.recv(size)
        print 'sending data back to client'
        client.sendall('echoed', data)
    else:
        print 'no more data from', address
        break
client.close()
#Function for handling connections.
def clientthread(conn):
		
	#infinite loop to keep open connection
	while True:
		
		#Rx from client
		data = conn.recv(1024)
		reply = 'OK...' + data
		if not data: 
			break
	
		conn.sendall(reply)
	
	#Out of loop
	conn.close()


while 1:
    
	conn, addr = s.accept()
	print 'Connected with ' + addr[0] + ':' + str(addr[1])
	version, msg_type, length = struct.unpack("!BBH", data[:4])
	start_new_thread(clientthread ,(conn,))

s.close()
