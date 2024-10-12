from cryptography.fernet import Fernet

msg = input("Digite sua mensagem: ")
chave = Fernet.generate_key()
fernet = Fernet(chave)
print(f"Mensagem criptografada: {fernet.encrypt(msg.encode())}")
