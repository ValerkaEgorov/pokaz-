import socket

serv_sock = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
serv_sock.bind ()
serv_sock.listen (5)

client_sock, client_addr = serv_sock.accept()

while True:
    data = client_sock.recv ( 1024 )
    if not data:
        break
    client_sock.sendall ( data )

client_sock.close
