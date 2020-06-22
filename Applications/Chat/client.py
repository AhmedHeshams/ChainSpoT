import socket
import select
import errno
import subprocess
import time
import sys

HEADER_LENGTH = 10
PORT = 1234

while True:
    cmd_output = subprocess.check_output("ipconfig", shell=True).decode()
    if "IPv4 Address. . . . . . . . . . . :" in cmd_output:
        break #need to check !
    time.sleep(1)
        
MY_IP=[]        
for i in cmd_output.split("\n"):
    if "IPv4 Address. . . . . . . . . . . :" in i:
        MY_IP.append(i.split(":")[1].strip())

if len(MY_IP) > 1:
    MY_IP = MY_IP[-1]
else:
    MY_IP = MY_IP[0] #need to be check !

while True:
    cmd_output = subprocess.check_output("ipconfig", shell=True).decode()
    if "Default Gateway" in cmd_output:
        break #need to check !
    time.sleep(1)
        
IP=[]

        
for i in cmd_output.split("\n"):
    if "Default Gateway . . . . . . . . . :" in i:
        IP.append(i.split(":")[1].strip())

for i in IP:
    if "." in i:
        IP = i

my_username = input("Username: ")

# Create a socket
# socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
# socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myself_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Connect to a given ip and port
client_socket.connect((IP, PORT))
myself_socket.connect((MY_IP, PORT))
myself_socket.setblocking(False)
# Set connection to non-blocking state, so .recv() call won't block, just return some exception we'll handle
client_socket.setblocking(False)

# Prepare username and header and send them
# We need to encode username to bytes, then count number of bytes and prepare header of fixed size, that we encode to bytes as well
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)
myself_socket.send(username_header + username)

while True:

    # Wait for user to input a message
    message = input(f'{my_username} > ')

    # If message is not empty - send it
    if message:

        # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)
        myself_socket.send(message_header + message)

    try:
        try:
            while True:
               
                # Receive our "header" containing username length, it's size is defined and constant
              
                prev_username_header = myself_socket.recv(HEADER_LENGTH)
             
                # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
                
                # Convert header to int value

                prev_username_length = int(prev_username_header.decode('utf-8').strip())
               
                # Receive and decode username
                
                prev_username = myself_socket.recv(prev_username_length).decode('utf-8')
                client_socket.send(prev_username_header + prev_username)
               
                # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any length)
                
                prev_message_header = myself_socket.recv(HEADER_LENGTH)
                
                prev_message_length = int(prev_message_header.decode('utf-8').strip())
                
                prev_message = myself_socket.recv(prev_message_length).decode('utf-8')
                myself_socket.send(prev_message_header + prev_message)
                

        except IOError as e:
            # This is normal on non blocking connections - when there are no incoming data error is going to be raised
            # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
            # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
            # If we got different error code - something happened
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error: {}'.format(str(e)))
                sys.exit()

        except Exception as e:
            # Any other exception - something happened, exit
            print('Reading error: '.format(str(e)))
            sys.exit()
        # Now we want to loop over received messages (there might be more than one) and print them
        while True:

            # Receive our "header" containing username length, it's size is defined and constant
            username_header = client_socket.recv(HEADER_LENGTH)
            #prev_username_header = myself_socket.recv(HEADER_LENGTH)
            
            # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()

            # Convert header to int value
            username_length = int(username_header.decode('utf-8').strip())
            #prev_username_length = int(prev_username_header.decode('utf-8').strip())
            
            # Receive and decode username
            username = client_socket.recv(username_length).decode('utf-8')
            #prev_username = myself_socket.recv(prev_username_length).decode('utf-8')
            #client_socket.send(prev_username_header + prev_username)
            
            # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any length)
            message_header = client_socket.recv(HEADER_LENGTH)
            #prev_message_header = myself_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            #prev_message_length = int(prev_message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')
            #prev_message = myself_socket.recv(prev_message_length).decode('utf-8')
            #myself_socket.send(prev_message_header + prev_message)
        
            # Print message
            print(f'{username} > {message}')

    except IOError as e:
        # This is normal on non blocking connections - when there are no incoming data error is going to be raised
        # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
        # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
        # If we got different error code - something happened
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()

        # We just did not receive anything
        continue

    except Exception as e:
        # Any other exception - something happened, exit
        print('Reading error: '.format(str(e)))
        sys.exit()
