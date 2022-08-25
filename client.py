import socket               # socket is imported -> for establishing connections
import argparse             # argparse is imported -> for command line input purposes
import time                 # time is imported -> for making the program sleep for 120s

def encodeContent(c):                   # A function to encode the content is created.
    C = c.encode()
    return C

# The next five lines are included so that the command line arguments can be parsed.
parser = argparse.ArgumentParser()                                                  # parser is initialized as an ArgumentParser object
parser.add_argument('-a', '--address', type=str, default='10.0.5.69')               # An optional argument is added; this is for the IP address of the receiver.
parser.add_argument('-s', '--server', type=int, default=9000)                       # An optional argument is added; this is for the port used by the receiver. 
parser.add_argument('-c', '--client', type=int, default=6734)                       # An optional argument is added; this is for the port used by the sender.
parser.add_argument('-i', '--identifier', type=str, default='6d93e931')             # An optional argument is added; this is for the unique ID assigned per student.

args = parser.parse_args()              # The arguments are parsed via parse_args()         

iD = args.identifier                    # The value of args.identifier is stored in iD.
portS = int(args.client)                # The integer value of args.client is stored in portS.
portR = int(args.server)                # The integer value of args.server is stored in portR.
ipR = args.address                      # The value of args.address is stored in ipR.

# The next 9 lines are included so that the Initiate Packet can be created.
student_id = iD                         # The value of iD is stored in student_id
transaction_id = '99999999'             # transaction_id is initialized with '99999999'
ty = '8'                                # ty is initialized with '8'
pull_byte = '00000'                     # pull_byte is initialized with '00000'
pull_size = '00000'                     # pull_size is initialized with '00000'
uin = '0000000'                         # uin is initialized with '0000000'
uin_ans = '0'                           # uin_ans is initialized with '0'
sep = '/'                               # sep is initialized with '/'
data = '0'                              # data is initialized with '0'

# iP is initialized using the values of the variables from lines 24 to 32
iP = '{}{}{}{}{}{}{}{}{}'.format(student_id, transaction_id, ty, pull_byte, pull_size, uin, uin_ans, sep, data)  
print("Initiate Packet: ", iP)          # The initiate packet is printed as output.

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # A UDP connection is set up.

M = encodeContent(iP)                   # iP is encoded via encodeContent(); the resulting value is stored in the variable M
udpSocket.bind(('', portS))             # The program listens from the sender port.

udpSocket.sendto(M, (ipR, portR))       # The initiate packet is sent to the receiver.

data, addr = udpSocket.recvfrom(1024)   # The program aims to receive from the server.

transID = data.decode()                 # The transaction number is gotten via decode() and stored in the variable transID.

print("Transaction Number: ", transID)  # The transaction number is printed as output.

print("Please wait until 120 seconds have passed.")     # The program then makes the user wait.
time.sleep(120)                                         # The program then sleeps for 120 seconds.
print("Goodbye.")                                       # The program then prints "Goodbye."

exit()                                                  # The program terminates.
