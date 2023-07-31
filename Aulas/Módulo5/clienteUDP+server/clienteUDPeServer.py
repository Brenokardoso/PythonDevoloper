import socket
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print(f"socket = {s} conectado com sucesso\n")

host = "localhost"
porta = 5433
mensagem = "Olá servidor!Firmeza?"

try:
    print(f"Cliente : {mensagem}")
    s.sendto(mensagem.encode(),(host,porta))
    dados,servidor = s.recvfrom(4069) 
    dados = dados.decode()
    print(f"cliente : {dados}")

finally:
    print("Cliente : fechando a conexão")
    s.close()

  