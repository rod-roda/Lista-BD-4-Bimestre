from pymongo import MongoClient
from cryptography.fernet import Fernet

cliente = MongoClient('mongodb+srv://rodriguinhoroda:123@cluster0.lcpgi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = cliente['lista_bruno']
colecao = db['fernets']

msg = input("Digite sua mensagem:")
chave_dict = colecao.find_one({'chave_fernet': { "$exists" : True }})
chave = chave_dict['chave_fernet']
fernet = Fernet(chave)

msg_cript = fernet.encrypt(msg.encode())
print(f"Mensagem criptografada: {msg_cript.decode()}")

msg_descript = fernet.decrypt(msg_cript.decode())
print(f"Mensagem descriptografada: {msg_descript}")
