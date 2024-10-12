from cryptography.fernet import Fernet

msg = "Esta mensagem esta criptografada"
chave = Fernet.generate_key()
fernet = Fernet(chave)
msg_cript = fernet.encrypt(msg.encode())
print(f"Mensagem criptografada: {msg_cript}\n")

print(f"Mensagem descriptografada: {fernet.decrypt(msg_cript.decode())}")
