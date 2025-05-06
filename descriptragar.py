import os
import pyaes

# Nome do arquivo criptografado
file_name = "virus.jpg.pyransomware"  # Nome do arquivo a ser descriptografado
file = open(file_name, "rb")  # Abre o arquivo em modo de leitura binária
file_data = file.read()  # Lê o conteúdo cifrado
file.close()  # Fecha o arquivo

# Mesma chave usada na criptografia (em formato bytes)
key = b"0123456789abcdef"  # Chave de 16 bytes para descriptografia AES
aes = pyaes.AESModeOfOperationCTR(key)  # Configura AES-CTR com a chave
cryptodata = aes.decrypt(file_data)  # Descriptografa os dados lidos

# Remove o arquivo criptografado
os.remove(file_name)  # Remove o arquivo original cifrado

# Grava o arquivo restaurado
new_file_name = "virus.jpg"  # Nome do novo arquivo descriptografado
new_file = open(new_file_name, "wb")  # Abre o novo arquivo em modo de escrita binária
new_file.write(cryptodata)  # Escreve os dados descriptografados no novo arquivo
new_file.close()  # Fecha o novo arquivo