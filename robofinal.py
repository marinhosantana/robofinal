from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

#------------------------------------------------------Data inicial e final ---------------------------------------------------------------------
datainicio = (input("Digite data inicial da consulta:"))
print(" A data está conrreta?" + datainicio)

inicio = int(input("digite '1' para sim e '2' para nao:"))

while(inicio!=1):
        print("Digite data inicial Correta:")
        datainicio = (input("Digite data inicial da consulta:"))
        inicio= int(input("digite '1' para sim e '2' para nao:"))

else:

     print("Data Aceita")


datafinal = (input("Digite data final da consulta:"))
print("A data final está conrreta?" + datafinal)

final= int(input("digite '1' para sim e '2' para nao:"))

while(final!=1):
        print("Digite data final Correta:")
        datafinal = (input("Digite data final da consulta:"))
        final= int(input("digite '1' para sim e '2' para nao:"))

else:

     print("Data Aceita")
#--------------------------------------------------Cham------------------------------------------------------------
options = webdriver.FirefoxOptions()
options.add_argument("start-maximized");
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
# Setando  cainho do driver
driver = webdriver.Firefox()
driver.get("https://minhaconta.getnet.com.br/login")
time.sleep(10)
# Enviando usuario
driver.find_element(By.XPATH,'//*[@id="loginField"]').send_keys('02939385807')
#Enviando Senha
driver.find_element(By.XPATH,'//*[@id="passField"]').send_keys('palmeiras10')
# Clicando para entrar
driver.find_element(By.XPATH,'//*[@id="btnEntrarContinuar"]').click()
time.sleep(4)
#--------------------o que recebi-----------------
#Clicando em financeiro

#Clicando em eportar
element=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/main/app-financeiro/div/div/div[1]/app-card-o-que-recebi/div/div[2]/button[2]')))
element.location_once_scrolled_into_view
time.sleep(5)
element.click()
#Clicando  para colocar a data
driver.find_element(By.XPATH,'/html/body/app-root/main/app-financeiro/div/div/div[1]/app-card-o-que-recebi/div/app-modal-download-extrato/div[1]/div/div[2]/div[1]/div[1]/div/app-date-picker-line/div[1]/button/span').click()
#Percorrendo  ate a data
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
#colocando  data inicial com  variavel
pyautogui.typewrite(datainicio)
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
#variavel data final
pyautogui.typewrite(datafinal)
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('down')
time.sleep(0.5)
pyautogui.press('down')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
#Clicando em atualizar
atualizar=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/main/app-downloads/div/div/div[2]/button')))
atualizar.location_once_scrolled_into_view
time.sleep(10)
atualizar.click()