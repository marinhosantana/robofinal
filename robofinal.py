from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait


#Criando Pasta
caminho = "C:\\Users\\USUARIO\\Downloads"
destino = "C:\\testerobo\\00689700000135\\"
os.chdir(caminho)
os.listdir()
competecia = (input("DIGITE A COMPETENCIA:"))
print("O mes de competencia está conrreta?" + competecia)

acao = int(input("digite '1' para sim e '2' para nao:"))

while acao!=1:
        print('Digite a competencia correta')
        competecia = (input("DIGITE A COMPETENCIA:"))
        acao = int(input("digite '1' para sim e '2' para nao:"))

else:
    try:
     os.makedirs(destino + competecia)
     print("Pasta cr1ada com sucesso")
    except:
        pass