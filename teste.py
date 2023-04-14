from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

time.sleep(10)
print(pyautogui.position())
pyautogui.moveTo(480, 480)
pyautogui.click()

driver.find_element(By.XPATH,'/html/body/app-root/main/app-financeiro/div/div/div[1]/app-card-o-que-recebi/div/app-modal-download-extrato/div[1]/div/div[2]/div[1]/div[1]/div/app-date-picker-line/div[1]/button/span').click()