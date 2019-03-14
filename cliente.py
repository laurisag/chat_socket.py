import socket

s = socket.socket()

HOST = socket.gethostname()
PORT = 8080

s.connect((HOST, PORT))
print('Conectado al servidor')

message = s.recv(1024)
message = message.decode()
print('Mensaje del servidor: ', message)

while 1:
    message = s.recv(1024)
    message = message.decode()
    print('Servidor: ', message)
    new_message = input(str('>>'))
    new_message = new_message.encode()
    s.send(new_message)
    print('Mensaje enviado')
