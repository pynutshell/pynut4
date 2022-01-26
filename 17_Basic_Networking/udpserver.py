import socket
 
UDP_IP = 'localhost'
UDP_PORT = 8883
 
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
print('Serving at', UDP_IP, UDP_PORT)
while True:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    print('RCVD', repr(data), 'from', addr)
    sock.sendto(data, addr)
    print('SENT', repr(data), 'to', addr)
