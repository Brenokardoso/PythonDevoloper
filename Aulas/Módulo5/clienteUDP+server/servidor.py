import socket
import sys 

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print(f"Socket criado com sucesso:\n")

host = "localhost"
porta = 5432

s.bind((host,porta))

mensagem = "Servidor : Activate!\n"

while True:
    dados,endereco = s.recvfrom(4096)

    if dados:
        print("Servidor enviando mensagem...")

        s.sendto(f"{(dados + (mensagem.encode()),endereco)}")