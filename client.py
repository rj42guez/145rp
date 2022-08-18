import socket
import sys

def encodeMessage(m):
    M = m.encode('utf-8')
    return M

iM = '6d93e931XXXXXXxx80000000000000000000'
iD = '6d93e931'
portS = 6734
portR = 9000
ipR = '10.0.5.69'

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

args = sys.argv

for i in range(len(args)):
	if args[i] == '-a' and args[i+1] == '10.0.5.69':
		ipR = args[i+1]
		print(ipR, '\n') 
	if args[i] == '-s' and args[i+1] == '9000':
		portR = int(args[i+1])
		print(portR, '\n') 
	if args[i] == '-c' and args[i+1] == '6734':
		portS = int(args[i+1])
		print(portS, '\n')
	if args[i] == '-i' and args[i+1] == '6d93e931':
		iD = args[i+1] 
		print(iD, '\n')

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
