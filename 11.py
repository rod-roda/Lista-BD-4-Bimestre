from cryptography.fernet import Fernet

chave = Fernet.generate_key()
fernet = Fernet(chave)

arquivo = open('C:/Users/aluno/Desktop/RODA E THIGAS/arquivotexto.txt', 'w')
arquivo.write(chave.decode())
