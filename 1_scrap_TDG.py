import os
from selenium import webdriver #Webdriver de Selenium qui permet de contrôler un navigateur
from selenium.webdriver.common.by import By #Permet d'accéder aux différents élements de la page web
from selenium.webdriver.common.keys import Keys # Importe les clefs pour les touches du clavier
from webdriver_manager.chrome import ChromeDriverManager #Assure la gestion du webdriver de Chrome
from time import sleep 
import time
import configparser


config = configparser.ConfigParser()
config.read('Pole_Médical/PoleMed_BDD/cred.ini')
user_value = config.get('Credentials', 'user_planning')
password_value = config.get('Credentials', 'mdp_planning')


def scroll(value): #Définition d'une fonction pour scroller automatiquement
    for _ in range(20):
        driver.execute_script(f"window.scrollBy(0, {value})")
        time.sleep(0.1) #Temps entre chaque scroll

        
driver = webdriver.Chrome(ChromeDriverManager().install()) # Ouvrir une page Google Chrome
time.sleep(2) 
driver.get('https://www.planning-imadis.fr/planning_gestion.php?d=1&t=1548025200') # Ouvrir l'adresse du site web
try:
    driver.find_element(By.ID, 'W0wltc').click()# accepter les cookies
except:
    None
time.sleep(2) 

user=driver.find_element(By.ID, 'user_name')
user.send_keys(user_value)
user.send_keys(Keys.ENTER)
password=driver.find_element(By.ID, 'user_password')
password.send_keys(password_value)
password.send_keys(Keys.ENTER)
time.sleep(2) 
try:
    button=driver.find_element(By.XPATH, "//*[@id='wrapper']/nav/div/ul[1]/li/a")
    button.click()
except:
    None
time.sleep(2)    
admin=driver.find_element(By.XPATH, "//*[@id='side-menu']/li[7]/a")
admin.click()
time.sleep(2)
tdg=driver.find_element(By.XPATH, "//*[@id='side-menu']/li[7]/ul/li[3]/a")
tdg.click()
scroll(100)

#pour telecharger tous les excel du dernier TDG
excel=driver.find_element(By.CSS_SELECTOR, '#top > div > table > tbody > tr:nth-child(3) > td:nth-child(7) > button.excel.btn.btn-default.btn-outline.btn-sm')
excel.click()
time.sleep(1) 
pds=driver.find_element(By.XPATH, "//*[@id='excelDpt1']")
pds.click()
time.sleep(1)
generate=driver.find_element(By.ID, "generate")
generate.click()
time.sleep(1) 
ao=driver.find_element(By.XPATH, "//*[@id='excelDpt2']")
ao.click()
time.sleep(1)
generate=driver.find_element(By.ID, "generate")
generate.click()
time.sleep(1) 
cds=driver.find_element(By.XPATH, "//*[@id='excelDpt3']")
cds.click()
time.sleep(1)
generate=driver.find_element(By.ID, "generate")
generate.click()
time.sleep(1) 
rru=driver.find_element(By.XPATH, "//*[@id='excelDpt4']")
rru.click()
time.sleep(1)
generate=driver.find_element(By.ID, "generate")
generate.click()
time.sleep(1) 
art=driver.find_element(By.XPATH, "//*[@id='excelDpt6']")
art.click()
time.sleep(1) 
generate=driver.find_element(By.ID, "generate")
generate.click()
time.sleep(1) 

close=driver.find_element(By.XPATH, "//*[@id='excel']/div/div/div[3]/button[1]")
close.click()
time.sleep(1) 

driver.close()