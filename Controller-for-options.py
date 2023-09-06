import pyautogui
import pyautogui as escolha_opcao
import time

time.sleep(3)
opcao = pyautogui.confirm('clique no botão com a opção desejada', buttons = ["Excel", "Word", "Notepad"])
