import hashlib

# Texto a ser criptografado
senha = input("Digite sua senha: ")

# Cria um objeto sha256 e gera o hash
senhahash = hashlib.sha256(senha.encode()).hexdigest()

# Exibe o hash gerado
print(f"SENHA EM HASH: {senhahash}")