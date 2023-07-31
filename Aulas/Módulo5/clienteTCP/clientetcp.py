import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    
    except socket.error as e:
        print(f"A conexão falhou! pois:\n erro: {e}")
        sys.exit()

    print(f"sockeck criado com sucesso: {s}")

    host_alvo = input("Digite o host ou ip a ser conectado\n")
    porta_alvo = int(input("Digite a porta a ser conectada\n"))

    try:
        s.connect((host_alvo, int(porta_alvo))) # (aceita string,não aceita string )
        print(f"Cliente TCP conectado com sucesso no host {host_alvo} na porta {porta_alvo}")
        # socket.socket.shutdown() # tempo de conexão

    except socket.error as e:
        print(f"A conexão falhou!\n não foi possivel conectar no host {host_alvo} pelo erro de {e}")
        sys.exit()

if __name__ == "__main__" :
    print("entrou")
    main()