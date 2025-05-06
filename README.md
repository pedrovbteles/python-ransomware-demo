🛡️ Python Ransomware Demo
Este repositório contém dois scripts em Python que simulam, de forma educativa, o funcionamento básico de um ransomware, utilizando a criptografia AES no modo CTR com a biblioteca pyaes.

⚠️ Atenção: Este projeto é apenas para fins didáticos. Não use este código para atividades maliciosas ou ilegais.

📁 Conteúdo
criptografar.py: criptografa um arquivo de imagem (virus.jpg), apaga o original e gera um arquivo cifrado com extensão .pyransomware.
descriptragar.py: descriptografa o arquivo .pyransomware e restaura o arquivo original.

🔧 Como usar
Instale a biblioteca pyaes, se ainda não tiver:
pip install pyaes

Coloque o arquivo virus.jpg na mesma pasta dos scripts.

Execute o script de criptografia:
python criptografar.py

Para restaurar o arquivo original, execute:
python descriptragar.py

🔐 Como funciona
Os scripts utilizam uma chave de 16 bytes (AES‑128) em formato bytes.
O modo CTR (Counter) permite criptografia de fluxo, ideal para arquivos binários.
Após a leitura e processamento dos dados, o script apaga automaticamente o arquivo original para simular o comportamento típico de um ransomware.

📚 Aprendizados
Implementação prática de criptografia AES em Python
Manipulação segura de arquivos binários
Entendimento do fluxo básico de funcionamento de um ransomware
Práticas de organização e controle de versões com Git e GitHub

🛑 Aviso Legal
Este projeto tem fins puramente educacionais. O autor não se responsabiliza por qualquer uso indevido. Use com responsabilidade e ética.
