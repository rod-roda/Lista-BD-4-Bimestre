import hashlib

def calcular_hash(arquivo):
    sha256 = hashlib.sha256()
    with open(arquivo, 'rb') as f:
        # Lê o arquivo em blocos para evitar carregar tudo na memória
        for bloco in iter(lambda: f.read(4096), b''):
            sha256.update(bloco)
    return sha256.hexdigest()


arquivo = input("Digite o caminho do arquivo .txt para verificar a integridade: ")

hash_inicial = calcular_hash(arquivo)
print(f"Hash inicial: {hash_inicial}")

input("Faça uma alteração no arquivo e pressione Enter para continuar...")

hash_final = calcular_hash(arquivo)
print(f"Hash final: {hash_final}")

if hash_inicial == hash_final:
    print("O arquivo NÃO foi alterado.")
else:
    print("O arquivo FOI alterado.")


