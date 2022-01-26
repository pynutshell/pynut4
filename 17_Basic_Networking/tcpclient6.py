# coding: utf-8
import socket
with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as sock:
    sock.connect(('localhost', 8881))
    print('Connected to server')
    data = u"""A few lines of text
including non-ASCII characters: €£
to test the operation
of both server
and client."""
    for line in data.splitlines():
        sock.sendall(line.encode('utf-8'))
        print('Sent:', line)
        response = sock.recv(1024)
        print('Recv:', response.decode('utf-8'))
sock.close()
print('Disconnected from server')
