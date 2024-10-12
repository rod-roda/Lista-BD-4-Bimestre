from pymongo import MongoClient
from cryptography.fernet import Fernet

cliente = MongoClient('mongodb+srv://rodriguinhoroda:123@cluster0.lcpgi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = cliente['lista_bruno']
colecao = db['fernets']

msg = input("Digite sua mensagem:")
chave = Fernet.generate_key()
fernet = Fernet(chave)
msg_cript = fernet.encrypt(msg.encode())

colecao.insert_one({'fernet_descript' : msg, 'fernet_cript' : msg_cript})