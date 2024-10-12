import hashlib

# Texto a ser criptografado
string1 = input("Digite primeira string: ")
string2 = input("Digite segunda string: ")

if hashlib.sha256(string1.encode()).hexdigest() == hashlib.sha256(string2.encode()).hexdigest():
    print("Hash's iguais!")
else:
    print("Hash's diferentes!")