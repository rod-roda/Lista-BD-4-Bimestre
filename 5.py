import hashlib

# Texto a ser criptografado
senha = input("Digite sua senha: ")

# Cria um objeto sha256 e gera o hash
senhamd5 = hashlib.md5(senha.encode()).hexdigest()

# Exibe o hash gerado
print(f"SENHA EM MD5: {senhamd5}")