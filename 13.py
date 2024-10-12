from pymongo import MongoClient
from cryptography.fernet import Fernet

cliente = MongoClient('mongodb+srv://rodriguinhoroda:123@cluster0.lcpgi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = cliente['lista_bruno']
colecao = db['fernets']

arquivo = open('C:/Users/aluno/Desktop/RODA E THIGAS/arquivotexto.txt', 'r')
chave = arquivo.readline()
colecao.insert_one({'chave_fernet' : chave})
