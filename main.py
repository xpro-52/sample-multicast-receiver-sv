import socket
import struct

# network interface of receiver
receiver_address = '192.168.8.20'

# address and port of multicast group
multicast_group = '224.1.1.1'
port = 5004

# buffer size
buffer_size = 4096

# finally close
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', port))
    sock.setsockopt(socket.IPPROTO_IP,  # ipv4
                    socket.IP_ADD_MEMBERSHIP,  # member of multicast group
                    socket.inet_aton(multicast_group) + socket.inet_aton(receiver_address))

    while True:
      print(sock.recv(buffer_size).decode())
