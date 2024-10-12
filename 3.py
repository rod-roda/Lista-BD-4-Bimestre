from pymongo import MongoClient
import hashlib

cliente = MongoClient('mongodb+srv://rodriguinhoroda:123@cluster0.lcpgi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = cliente['lista_bruno']
colecao = db['hashs']
# Texto a ser criptografado
texto = input("Digite sua string: ")

# Cria um objeto sha256 e gera o hash
stringhash = hashlib.sha256(texto.encode()).hexdigest()
colecao.insert_one({'Hash_descript' : texto, 'hash_cript' : stringhash})