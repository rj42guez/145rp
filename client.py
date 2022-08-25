#Modules socket, argparse, and time are imported
import socket
import argparse
import time

#A function to encode the message is created
def encodeMessage(m):
    M = m.encode()
    return M

#
parser = argparse.ArgumentParser()
parser.add_argument('-a', '--address', type=str, default='10.0.5.69')
parser.add_argument('-s', '--server', type=int, default=9000)
parser.add_argument('-c', '--client', type=int, default=6734)
parser.add_argument('-i', '--identifier', type=str, default='6d93e931')

args = parser.parse_args()

iD = args.identifier
portS = int(args.client)
portR = int(args.server)
ipR = args.address

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
