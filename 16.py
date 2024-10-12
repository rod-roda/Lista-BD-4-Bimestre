import hashlib

def gerar_hashes(strings):
    hashes = {}
    for s in strings:
        md5_hash = hashlib.md5(s.encode()).hexdigest()
        sha1_hash = hashlib.sha1(s.encode()).hexdigest()
        sha256_hash = hashlib.sha256(s.encode()).hexdigest()
        
        hashes[s] = {
            'MD5': md5_hash,
            'SHA-1': sha1_hash,
            'SHA-256': sha256_hash
        }
    return hashes

def comparar_tamanhos(hashes):
    tamanhos = {}
    for string, hash_dict in hashes.items():
        tamanhos[string] = {
            'MD5': len(hash_dict['MD5']),
            'SHA-1': len(hash_dict['SHA-1']),
            'SHA-256': len(hash_dict['SHA-256'])
        }
    return tamanhos

strings = [input("Apenas Enter para encerrar o programa:\n")]

while(strings[-1] != ""):
    hashes = gerar_hashes(strings)

    tamanhos = comparar_tamanhos(hashes)

    for string, tamanho in tamanhos.items():
        print(f"String: '{string}'")
        print(f"Tamanhos dos hashes: MD5 = {tamanho['MD5']} caracteres, SHA-1 = {tamanho['SHA-1']} caracteres, SHA-256 = {tamanho['SHA-256']} caracteres")
        print("-" * 60)

    strings.append(input("Apenas Enter para encerrar o programa:\n"))
