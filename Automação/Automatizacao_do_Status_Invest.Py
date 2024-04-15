import webbrowser
import pyautogui
import os
import subprocess

# Definir a URL da página e o caminho do Chrome
url = "colocar o local do site que deseja acessar"
chrome_path = "colocar o local de onde se encontra o endereço do google chrome"

# Abrir a página no Chrome usando webbrowser
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open(url)

# Esperar um momento para a página carregar completamente
pyautogui.sleep(9)

# Clicar no botão "buscar" usando as coordenadas específicas
pyautogui.click(x=650, y=710)

#Time antes de ir clicar no botão para baixar o arquivo
pyautogui.sleep(6)

#click no botão baixar
pyautogui.click(x=1200, y=320)

pyautogui.sleep(6)

#abrir pasta downloads
def open_downloads_folder():
    # Obtenha o diretório de downloads
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')

    # Verifique se o diretório existe
    if os.path.isdir(downloads_path):
        # Abra o diretório de downloads no sistema operacional específico
        if os.name == 'nt':  # Windows
            subprocess.run(['explorer', downloads_path])
        elif os.name == 'posix':  # Linux ou macOS
            subprocess.run(['xdg-open', downloads_path])
        else:
            print("Sistema operacional não suportado.")
    else:
        print("O diretório de downloads não foi encontrado.")

# Chamada da função para abrir a pasta de downloads
open_downloads_folder()

#click para abrir excel
pyautogui.sleep(3)

pyautogui.click(x=300, y=240)

pyautogui.press('enter')

#click para selecionar linha 1
pyautogui.sleep(5)

pyautogui.click(x=5, y=280)

#clicar no filtro
pyautogui.click(x=1100, y=80)
pyautogui.sleep(2)

#Clicar filtro
pyautogui.click(x=1100, y=235)
