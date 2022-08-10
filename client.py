import socket
import struct
import hashlib
import sys

def encodeMessage(m):
    M = m.encode('utf-8')
    return M

iM = '6d93e9310000000080000000000000000000'
iD = '6d93e931'
portS = 6734
portR = 9000
ipR = 0
path = ''

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

args = sys.argv

for i in range(len(args)):
	if args[i] == '-a':
		ipR = args[i+1]
		print(ipR, '\n') 
	if args[i] == '-s':
		portR = int(args[i+1])
		print(portR, '\n') 
	if args[i] == '-c':
		portS = int(args[i+1])
		print(portS, '\n')
	if args[i] == '-i':
		iD = args[i+1] 
		print(iD, '\n')

M = encodeMessage(iM)
udpSocket.bind(('', portS))
udpsocket.settimeout(0.5)

udpSocket.sendto(M, (ipR, portR))

data, addr = udpSocket.recvfrom(1024)

if len(data) > 0:
	print(addr,'\n')
	transID = data.decode()

print("Transaction Number: ", transID)

break
