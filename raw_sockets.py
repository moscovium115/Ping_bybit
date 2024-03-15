import socket
import struct

# Create a raw socket
raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800)) # AF_PACKET for raw packet access, SOCK_RAW for raw socket, 0x0800 for IP packets

# Set the interface to use (replace 'eth0' with your network interface)
interface = b'eth0'

# Create an Ethernet frame (replace the destination MAC address with the appropriate one)
dest_mac = b'\x00\x00\x00\x00\x00\x00'  # Destination MAC address
src_mac = b'\x00\x00\x00\x00\x00\x00'   # Source MAC address
ethertype = b'\x08\x00'  # EtherType (IPv4)
eth_header = dest_mac + src_mac + ethertype

# Create an IP packet
version_ihl = 69   # IPv4 version (4 bits) and Internet Header Length (4 bits)
tos = 0            # Type of Service (1 byte)
total_length = 0   # Total length (2 bytes)
identification = 0 # Identification (2 bytes)
flags_frag_offset = 0 # Flags (3 bits) and Fragment Offset (13 bits)
ttl = 255          # Time to Live (1 byte)
protocol = 6       # Protocol (1 byte, TCP = 6)
checksum = 0       # Header checksum (2 bytes)
src_ip = b'\x7f\x00\x00\x01' # Source IP address (127.0.0.1)
dest_ip = b'\x7f\x00\x00\x01' # Destination IP address (127.0.0.1)
ip_header = struct.pack('!BBHHHBBH4s4s', version_ihl, tos, total_length, identification, flags_frag_offset, ttl, protocol, checksum, src_ip, dest_ip)

# Combine Ethernet header and IP header
packet = eth_header + ip_header

# Send the packet
raw_socket.sendto(packet, (interface, 0))

# Receive packets
while True:
    packet_data, addr = raw_socket.recvfrom(65535)  # Adjust the buffer size as needed
    print('Received packet:', packet_data)
