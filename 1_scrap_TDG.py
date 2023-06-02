import os
from selenium import webdriver #Webdriver de Selenium qui permet de contrôler un navigateur
from selenium.webdriver.common.by import By #Permet d'accéder aux différents élements de la page web
from selenium.webdriver.common.keys import Keys # Importe les clefs pour les touches du clavier
from webdriver_manager.chrome import ChromeDriverManager #Assure la gestion du webdriver de Chrome
from time import sleep 
import time
import configparser
import getpass
import os
import glob
import pandas as pd

config = configparser.ConfigParser()
config.read('cred.ini')
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

username = getpass.getuser()

#pour telecharger tous les excel du dernier TDG

#PDS
excel=driver.find_element(By.CSS_SELECTOR, '#top > div > table > tbody > tr:nth-child(3) > td:nth-child(7) > button.excel.btn.btn-default.btn-outline.btn-sm')
excel.click()
time.sleep(1) 

pds=driver.find_element(By.XPATH, "//*[@id='excelDpt1']")
pds.click()
time.sleep(1)

generate=driver.find_element(By.ID, "generate")
generate.click()
time.sleep(1) 

download_folder = 'C:/Users/'+username+'/Downloads/'
excel_files = glob.glob(download_folder + 'export*.xlsx')
df_pds=pd.read_excel(excel_files[0], header=None)
df_pds.to_csv('df_pds.csv', index=False)

os.remove(excel_files[0])

#AO
ao=driver.find_element(By.XPATH, "//*[@id='excelDpt2']")
ao.click()
time.sleep(1)

generate=driver.find_element(By.ID, "generate")
generate.click()
time.sleep(1) 

download_folder = 'C:/Users/'+username+'/Downloads/'
excel_files = glob.glob(download_folder + 'export*.xlsx')
df_ao=pd.read_excel(excel_files[0], header=None)
df_ao.to_csv('df_ao.csv', index=False)

os.remove(excel_files[0])

#CDS
cds=driver.find_element(By.XPATH, "//*[@id='excelDpt3']")
cds.click()
time.sleep(1)

generate=driver.find_element(By.ID, "generate")
generate.click()
time.sleep(1) 

download_folder = 'C:/Users/'+username+'/Downloads/'
excel_files = glob.glob(download_folder + 'export*.xlsx')
df_cds=pd.read_excel(excel_files[0], header=None)
df_cds.to_csv('df_cds.csv', index=False)

os.remove(excel_files[0])

#RRU
rru=driver.find_element(By.XPATH, "//*[@id='excelDpt4']")
rru.click()
time.sleep(1)

generate=driver.find_element(By.ID, "generate")
generate.click()
time.sleep(1) 

download_folder = 'C:/Users/'+username+'/Downloads/'
excel_files = glob.glob(download_folder + 'export*.xlsx')
df_rru=pd.read_excel(excel_files[0], header=None)
df_rru.to_csv('df_rru.csv', index=False)

os.remove(excel_files[0])

#ART
art=driver.find_element(By.XPATH, "//*[@id='excelDpt6']")
art.click()
time.sleep(1) 

generate=driver.find_element(By.ID, "generate")
generate.click()
time.sleep(1) 

download_folder = 'C:/Users/'+username+'/Downloads/'
excel_files = glob.glob(download_folder + 'export*.xlsx')
df_art=pd.read_excel(excel_files[0], header=None)
df_art.to_csv('df_art.csv', index=False)

os.remove(excel_files[0])

#Fermer le générateur
close=driver.find_element(By.XPATH, "//*[@id='excel']/div/div/div[3]/button[1]")
close.click()
time.sleep(1) 

driver.close()