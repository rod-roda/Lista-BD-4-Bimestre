import hashlib

def gerar_hash(algoritmo, senha):
    if algoritmo == 'md5':
        return hashlib.md5(senha.encode()).hexdigest()
    elif algoritmo == 'sha1':
        return hashlib.sha1(senha.encode()).hexdigest()
    elif algoritmo == 'sha256':
        return hashlib.sha256(senha.encode()).hexdigest()
    else:
        raise ValueError("Algoritmo desconhecido.")

senha = input("Digite sua senha: ")
algoritmo = input("Escolha o algoritmo (md5, sha1, sha256): ").lower()

try:
    senhahash = gerar_hash(algoritmo, senha)
    print(f"SENHA EM HASH ({algoritmo.upper()}): {senhahash}")
except ValueError as e:
    print(e)
