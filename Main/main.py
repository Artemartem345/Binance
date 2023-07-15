
import undetected_chromedriver as uc
from undetected_chromedriver import By
import time
from auth_data import *
import pickle
import json
from pathlib import Path
driver = uc.Chrome()
time.sleep(3)
driver.get( 'https://accounts.binance.com/ru/login')
username = driver.find_element('id', 'username')
username.send_keys(auth_username)
driver.find_element('id','click_login_submit').click()
time.sleep(5)
driver.get('https://accounts.binance.com/ru/login-password?isNewLogin=true&loginChannel=homepage&return_to=aHR0cHM6Ly93d3cuYmluYW5jZS5jb20vcnUvbXkvZGFzaGJvYXJk')
password = driver.find_element('name','password')
password.send_keys(auth_password)
driver.find_element('id','click_login_submit').click()
time.sleep(50)
driver.find_element('id','onetrust-accept-btn-handler').click()
time.sleep(10)
driver.get('https://www.binance.com/ru/my/wallet/account/main/withdrawal/crypto/BTS')
time.sleep(10)


adress = driver.find_element('id', 'withdraw-address-selection-input')
time.sleep(3)
adress.send_keys('binance-bts-1-start')
time.sleep(15)
#driver.find_element(By.CLASS_NAME, "css-59tupe").click()

# Не видит сука всплывающее окно с подтверждением. Поправить, чтобы видел
# driver.find_element(By.CLASS_NAME, "css-59tupe").click()
    
    


memo_adress = driver.find_element('name', 'memo')
time.sleep(3)
memo_adress.send_keys(108802181)


amount_withdraw = driver.find_element('id','withdraw-amount-input')
time.sleep(5)
amount_withdraw.send_keys(amount_BTS)


time.sleep(5)
withdraw_button = driver.find_element('id','withdraw-submit-btn').click()
time.sleep(7)
confirm_button = driver.find_element('id','crypto_withdraw_confitm_btn').click()
time.sleep(50)
    
