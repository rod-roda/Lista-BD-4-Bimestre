from cryptography.fernet import Fernet

arquivo = open('C:/Users/aluno/Desktop/RODA E THIGAS/arquivo.txt', 'w')
conteudo = input("Aperte enter para parar de digitar o conteudo a ser inserido no arquivo: ")
while conteudo != '':
    arquivo.writelines(conteudo)
    conteudo = input("Aperte enter para parar de digitar o conteudo a ser inserido no arquivo: ")
