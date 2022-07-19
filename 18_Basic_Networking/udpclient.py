# coding: utf-8
import socket
 
UDP_IP = 'localhost'
UDP_PORT = 8883
MESSAGE = u"""\
This is a bunch of lines, each
of which will be sent in a single
UDP datagram. No error detection
or correction will occur.
Crazy bananas! £€ should go through."""
 
sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
server = UDP_IP, UDP_PORT
for line in MESSAGE.splitlines():
    data = line.encode('utf-8')
    sock.sendto(data, server)
    print('SENT', repr(data), 'to', server)
    response, address = sock.recvfrom(1024)  # buffer size: 1024
    print('RCVD', repr(response.decode('utf-8')), 'from', address)
sock.close()
