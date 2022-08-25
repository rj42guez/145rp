import socket
import argparse
import time

def encodeMessage(m):
    M = m.encode()
    return M

parser = argparse.ArgumentParser()
parser.add_argument('-a', type=str, default='10.0.5.69')
parser.add_argument('-s', type=int, default=9000)
parser.add_argument('-c', type=int, default=6734)
parser.add_argument('-i', type=str, default='6d93e931')

args = parser.parse_args()

iD = args.i
portS = int(args.c)
portR = int(args.s)
ipR = args.a

student_id = iD
transaction_id = '99999999'
ty = '8'
pull_byte = '00000'
pull_size = '00000'
uin = '0000000'
uin_ans = '0'
sep = '/'
data = '0'

iM = '{}{}{}{}{}{}{}{}{}'.format(student_id, transaction_id, ty, pull_byte, pull_size, uin, uin_ans, sep, data)
print(iM,"\n")

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

M = encodeMessage(iM)
udpSocket.bind(('', portS))

udpSocket.sendto(M, (ipR, portR))

data, addr = udpSocket.recvfrom(1024)

transID = data.decode()

print("Transaction Number: ", transID)

print("Please wait until 120 seconds have passed.")
time.sleep(120)
print("Goodbye.")

exit()
