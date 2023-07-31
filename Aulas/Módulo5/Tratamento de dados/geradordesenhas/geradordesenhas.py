import random,string

tamanho = 30
alpha_caracteres = "!@#$%*()_ç+=£¢¬{[]}§"

chars = (string.ascii_letters + string.digits + alpha_caracteres)

rnd = random.SystemRandom() #os.urrandom --> senhas aleatorias baseadas pelo sistema operacional

print(f"caracteres = {chars}")

for x in range(30):
    if x == 0:
        print("senha das boas= ",end = "")
    print(f"{rnd.choice(chars)}",end ="")

print("\n")
for x in range(5):
    print(f"senha = {''.join(rnd.choice(chars) for i in range(tamanho))}")



