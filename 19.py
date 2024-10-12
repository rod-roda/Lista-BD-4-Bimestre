from cryptography.fernet import Fernet
from pymongo import MongoClient

def gerar_chave():
    return Fernet.generate_key()

def criptografar_mensagem(mensagem, chave):
    fernet = Fernet(chave)
    mensagem_encriptada = fernet.encrypt(mensagem.encode())
    return mensagem_encriptada

def conectar_mongodb():
    client = MongoClient("mongodb+srv://thiago:123@cluster0.bz0hk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client["BancoDeDados"]
    return db["ListaDeExercicios"]

def armazenar_mensagem(mensagem_encriptada):
    collection = conectar_mongodb()
    collection.insert_one({"mensagem_encriptada": mensagem_encriptada})
    print("Mensagem armazenada com sucesso!")


chave = gerar_chave()
print(f"Chave de criptografia: {chave.decode()}")  

while True:
    mensagem = input("Digite a mensagem a ser criptografada (ou 'sair' para encerrar): ")
    if mensagem.lower() == 'sair':
        print("Saindo...")
        break
    
    mensagem_encriptada = criptografar_mensagem(mensagem, chave)
    armazenar_mensagem(mensagem_encriptada)

