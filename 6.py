import hashlib

# Texto a ser criptografado
texto = input("Digite sua string: ")

# Cria um objeto sha256 e gera o hash
textohash = hashlib.sha256(texto.encode()).hexdigest()
textomd5 = hashlib.md5(texto.encode()).hexdigest()
textosha1 = hashlib.sha1(texto.encode()).hexdigest()

# Exibe o hash gerado
print(f"SENHA EM SHA256: {textohash}")
print(f"SENHA EM MD5: {textomd5}")
print(f"SENHA EM SHA-1: {textosha1}")