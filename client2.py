import socket

client_sock = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
client_sock = connect (  )
client_sock.sendall ()
data = client_sock.recv ( 1024 )
client_sock.close ()
