import os
from cryptography.fernet import Fernet

# Carregar chave de descriptografia
with open("filekey.key", "rb") as filekey:
    key = filekey.read()

# Definindo o diretório alvo
folder_path = r"c:\documentosteste"

# Listando arquivos no diretório (excluindo o script, chave e readme)
files = []
for root, dirs, filenames in os.walk(folder_path):
    for filename in filenames:
        if filename in ['filekey.key', 'ransomware.py', 'readme.txt']:
            continue
        filepath = os.path.join(root, filename)
        if os.path.isfile(filepath):
            files.append(filepath)

# Descriptografando arquivos
fernet = Fernet(key)
for file in files:
    with open(file, "rb") as f:
        encrypted_data = f.read()
    decrypted = fernet.decrypt(encrypted_data)
    with open(file, "wb") as f:
        f.write(decrypted)

print("Arquivos descriptografados com sucesso!")
