import os

ip_ou_host = input("Digite o ip ou host a ser verificado:\n")

os.system(f"ping {ip_ou_host}")