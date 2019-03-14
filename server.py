import socket

s = socket.socket() #servidor
HOST = socket.gethostname()
PORT = 8080

s.bind((HOST, PORT))
s.listen(1) #escuchar mensaje
print('Esperando a compañerxs...')
connection, addr = s.accept() #conexión de otros usuarios
print('Se ha conectado un cliente')
connection.send('Bienvenido al servidor '.encode()) #enviar a los conectados que, efectivamente, se han conectado

while 1:
    message = input(str('>>')) #input para escribir mensaje
    message = message.encode() #codificamos el mensaje para que le aparezca al cliente
    connection.send(message)
    print('Mensaje enviado')
    recv_message = connection.recv(1024) #recv_mensaje = recibir mensaje
    print('Cliente: ', recv_message.decode())
