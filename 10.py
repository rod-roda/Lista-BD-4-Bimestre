from pymongo import MongoClient
from cryptography.fernet import Fernet

cliente = MongoClient('mongodb+srv://rodriguinhoroda:123@cluster0.lcpgi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = cliente['lista_bruno']
colecao = db['fernets']

msg_cript = colecao.find_one({'fernet_cript': { "$exists" : True }})
print(msg_cript)