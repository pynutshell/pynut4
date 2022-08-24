# coding: utf-8
import socket

UDP_IP = 'localhost'
UDP_PORT = 8883
MESSAGE = """\
This is a bunch of lines, each
of which will be sent in a single
UDP datagram. No error detection
or correction will occur.
Crazy bananas! £€ should go through."""

server = UDP_IP, UDP_PORT
with socket.socket(socket.AF_INET6,    # IPv6
                   socket.SOCK_DGRAM,  # UDP
                   ) as sock:
    for line in MESSAGE.splitlines():
        data = line.encode('utf-8')
        bytes_sent = sock.sendto(data, server)
        print(f'SENT {data!r} ({bytes_sent}/{len(data)}) to {server}')
        response, address = sock.recvfrom(1024)  # buffer size: 1024
        print(f'RCVD {response.decode("utf-8")!r} ({len(response)}) from {address}')

print('Disconnected from server')
