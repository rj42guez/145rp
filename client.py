import socket
import argparse

def encodeMessage(m):
    M = m.encode('utf-8')
    return M

parser = argparse.ArgumentParser()
parser.add_argument('-a', type=str, default="10.0.5.69")
parser.add_argument('-s', type=int, default=9000)
parser.add_argument('-c', type=int, default=6734)
parser.add_argument('-i', type=str, default="6d93e931")

args = parser.parse_args()
  
iM = '6d93e9311010101080000000000000000000'
iD = args.i
portS = args.c
portR = args.s
ipR = args.a

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

M = encodeMessage(iM)
udpSocket.bind(('', portS))
udpSocket.settimeout(0.5)

udpSocket.sendto(M, (ipR, portR))

data, addr = udpSocket.recvfrom(1024)
transID = ''

if len(data) > 0:
	print(addr,'\n')
	transID = data.decode()

print("Transaction Number: ", transID)

exit()
