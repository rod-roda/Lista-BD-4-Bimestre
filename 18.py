import hashlib
from pymongo import MongoClient

# Função para gerar o hash da senha
def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# Conexão com o MongoDB
def conectar_mongodb():
    client = MongoClient("mongodb+srv://thiago:123@cluster0.bz0hk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client["BancoDeDados"]
    return db["ListaDeExercicios"]

# Armazenar o hash da senha no MongoDB
def armazenar_senha(senha):
    collection = conectar_mongodb()
    senha_hash = gerar_hash(senha)
    collection.insert_one({"senha_hash": senha_hash})
    print("Senha armazenada com sucesso!")

# Validar a senha do usuário
def validar_senha(senha):
    collection = conectar_mongodb()
    senha_hash = gerar_hash(senha)
    resultado = collection.find_one({"senha_hash": senha_hash})

    if resultado:
        print("Senha válida!")
    else:
        print("Senha inválida!")

while True:
    acao = input("Você deseja (1) armazenar uma nova senha ou (2) validar uma senha? (0 para sair): ")
    
    if acao == '1':
        senha = input("Digite a senha a ser armazenada: ")
        armazenar_senha(senha)
    elif acao == '2':
        senha = input("Digite a senha para validar: ")
        validar_senha(senha)
    elif acao == '0':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

