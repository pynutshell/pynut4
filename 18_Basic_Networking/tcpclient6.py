import socket

IP_ADDR = 'localhost'
IP_PORT = 8881
MESSAGE = """\
A few lines of text
including non-ASCII characters: €£
to test the operation
of both server
and client."""

with socket.socket(socket.AF_INET6,    # IPv6
                   socket.SOCK_STREAM  # TCP
                   ) as sock:
    sock.connect((IP_ADDR, IP_PORT))
    print(f'Connected to server {IP_ADDR}:{IP_PORT}')
    for line in MESSAGE.splitlines():
        data = line.encode('utf-8')
        sock.sendall(data)
        print(f'SENT {data!r} ({len(data)})')
        response, address = sock.recvfrom(1024)  # buffer size: 1024
        print(f'RCVD {response!r} ({len(response)}) from {address}')

print('Disconnected from server')
