import os
from selenium import webdriver #Webdriver de Selenium qui permet de contrôler un navigateur
from selenium.webdriver.common.by import By #Permet d'accéder aux différents élements de la page web
from selenium.webdriver.common.keys import Keys # Importe les clefs pour les touches du clavier
from webdriver_manager.chrome import ChromeDriverManager #Assure la gestion du webdriver de Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep 
import time
import getpass
import glob
import pandas as pd
import os
import configparser
import numpy as np
import re
import datetime 

# utilisateurs
username = getpass.getuser()

# credentials planning
config = configparser.ConfigParser()
config.read('C:/Users/'+username+'/Imadis Téléradiologie/INTRANET - IMADIS/QUALITE/7- RHM/15 - DMA/GitHub/cred.ini')
user_value = config.get('Credentials', 'user_planning')
password_value = config.get('Credentials', 'mdp_planning')

# def scroll pour webscrapping
def scroll(value): #Définition d'une fonction pour scroller automatiquement
    for _ in range(20):
        driver.execute_script(f"window.scrollBy(0, {value})")
        time.sleep(0.1) #Temps entre chaque scroll


# Webscrpping du planning
chrome_options = Options()
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options) # Ouvrir une page Google Chrome

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

#PDS
excel=driver.find_element(By.CSS_SELECTOR, '#top > div > table > tbody > tr:nth-child(2) > td:nth-child(7) > button.excel.btn.btn-default.btn-outline.btn-sm')
excel.click()
time.sleep(1) 

pds=driver.find_element(By.XPATH, "//*[@id='excelDpt1']")
pds.click()
time.sleep(1)

generate=driver.find_element(By.ID, "generate")
generate.click()
time.sleep(2) 

download_folder = 'C:/Users/'+username+'/Downloads/'
excel_files = glob.glob(download_folder + 'export*.xlsx')
df_pds=pd.read_excel(excel_files[0], header=None)
df_pds.to_csv('C:/Users/'+username+'/Imadis Téléradiologie/INTRANET - IMADIS/QUALITE/7- RHM/15 - DMA/GitHub/data/df_pds.csv', index=False)

os.remove(excel_files[0])
print("Le fichier PDS a été téléchargé.")

#AO
ao=driver.find_element(By.XPATH, "//*[@id='excelDpt2']")
ao.click()
time.sleep(1)

generate=driver.find_element(By.ID, "generate")
generate.click()
time.sleep(2) 

download_folder = 'C:/Users/'+username+'/Downloads/'
excel_files = glob.glob(download_folder + 'export*.xlsx')
df_ao=pd.read_excel(excel_files[0], header=None)
df_ao.to_csv('C:/Users/'+username+'/Imadis Téléradiologie/INTRANET - IMADIS/QUALITE/7- RHM/15 - DMA/GitHub/data/df_ao.csv', index=False)

os.remove(excel_files[0])
print("Le fichier AO a été téléchargé.")

#CDS
cds=driver.find_element(By.XPATH, "//*[@id='excelDpt3']")
cds.click()
time.sleep(1)

generate=driver.find_element(By.ID, "generate")
generate.click()
time.sleep(2) 

download_folder = 'C:/Users/'+username+'/Downloads/'
excel_files = glob.glob(download_folder + 'export*.xlsx')
df_cds=pd.read_excel(excel_files[0], header=None)
df_cds.to_csv('C:/Users/'+username+'/Imadis Téléradiologie/INTRANET - IMADIS/QUALITE/7- RHM/15 - DMA/GitHub/data/df_cds.csv', index=False)

os.remove(excel_files[0])
print("Le fichier CDS a été téléchargé.")

#RRU
rru=driver.find_element(By.XPATH, "//*[@id='excelDpt4']")
rru.click()
time.sleep(1)

generate=driver.find_element(By.ID, "generate")
generate.click()
time.sleep(2) 

download_folder = 'C:/Users/'+username+'/Downloads/'
excel_files = glob.glob(download_folder + 'export*.xlsx')
df_rru=pd.read_excel(excel_files[0], header=None)
df_rru.to_csv('C:/Users/'+username+'/Imadis Téléradiologie/INTRANET - IMADIS/QUALITE/7- RHM/15 - DMA/GitHub/data/df_rru.csv', index=False)

os.remove(excel_files[0])
print("Le fichier RRU a été téléchargé.")

#ART
art=driver.find_element(By.XPATH, "//*[@id='excelDpt6']")
art.click()
time.sleep(1) 

generate=driver.find_element(By.ID, "generate")
generate.click()
time.sleep(2) 

download_folder = 'C:/Users/'+username+'/Downloads/'
excel_files = glob.glob(download_folder + 'export*.xlsx')
df_art=pd.read_excel(excel_files[0], header=None)
df_art.to_csv('C:/Users/'+username+'/Imadis Téléradiologie/INTRANET - IMADIS/QUALITE/7- RHM/15 - DMA/GitHub/data/df_art.csv', index=False)

os.remove(excel_files[0])
print("Le fichier ART a été téléchargé.")

#Fermer le générateur
close=driver.find_element(By.XPATH, "//*[@id='excel']/div/div/div[3]/button[1]")
close.click()
time.sleep(1) 

driver.close()

# Spécifiez le chemin complet du fichier CSV à supprimer
chemin_fichier = 'C:/Users/'+username+'/Imadis Téléradiologie/INTRANET - IMADIS/QUALITE/7- RHM/15 - DMA/GitHub/data/new_data.csv'

# Vérifiez si le fichier existe avant de le supprimer
if os.path.exists(chemin_fichier):
    os.remove(chemin_fichier)
    print("Le fichier CSV new_data.csv a été supprimé avec succès.")
else:
    print("Le fichier CSV new_data.csv n'existe pas.")

#Créer le nouveau fichier new_data
df1=pd.read_csv('C:/Users/'+username+'/Imadis Téléradiologie/INTRANET - IMADIS/QUALITE/7- RHM/15 - DMA/GitHub/data/df_ao.csv')
df2=pd.read_csv('C:/Users/'+username+'/Imadis Téléradiologie/INTRANET - IMADIS/QUALITE/7- RHM/15 - DMA/GitHub/data/df_cds.csv')
df3=pd.read_csv('C:/Users/'+username+'/Imadis Téléradiologie/INTRANET - IMADIS/QUALITE/7- RHM/15 - DMA/GitHub/data/df_rru.csv')
df4=pd.read_csv('C:/Users/'+username+'/Imadis Téléradiologie/INTRANET - IMADIS/QUALITE/7- RHM/15 - DMA/GitHub/data/df_art.csv')
df5=pd.read_csv('C:/Users/'+username+'/Imadis Téléradiologie/INTRANET - IMADIS/QUALITE/7- RHM/15 - DMA/GitHub/data/df_pds.csv')

correspondance_colonnes = {'0' : 'Date',
                          '1': 'Associé',
                          '2': 'Nom',
                          '3' : 'Prénom',
                          '4' : 'mail',
                          '5' : 'Site',
                          '6' : 'Jour/Nuit',
                          '7': 'Date_Heure_Début',
                          '8' : 'Date_Heure_Fin'}

df1 = df1.rename(columns=correspondance_colonnes)
df3 = df3.rename(columns=correspondance_colonnes)

correspondance_colonnes = {'0': 'Date',
                          '1': 'Associé',
                          '2': 'Nom',
                          '3' : 'Prénom',
                          '4' : 'mail',
                          '5' : 'Site',
                          '6' : 'Jour/Nuit',
                          '7': 'Date_Heure_Début',
                          '8' : 'Date_Heure_Fin',
                          '9' : 'Chef',
                          '10' : 'Formation'}

df2 = df2.rename(columns=correspondance_colonnes)
df4 = df4.rename(columns=correspondance_colonnes)
df5 = df5.rename(columns=correspondance_colonnes)

df1['Chef'] = np.nan
df3['Chef'] = np.nan
df4['Chef'] = np.nan

df1['Formation'] = np.nan
df2['Formation'] = np.nan
df3['Formation'] = np.nan
df4['Formation'] = np.nan

df1['Source'] = 'AO'
df2['Source'] = 'CDS'
df3['Source'] = 'RRU'
df4['Source'] = 'ART'
df5['Source'] = 'PDS'

df1['Nom_Prenom'] = df1['Nom']+' '+df1['Prénom']
df2['Nom_Prenom'] = df2['Nom']+' '+df2['Prénom']
df3['Nom_Prenom'] = df3['Nom']+' '+df3['Prénom']
df4['Nom_Prenom'] = df4['Nom']+' '+df4['Prénom']
df5['Nom_Prenom'] = df5['Nom']+' '+df5['Prénom']

df1 = df1.dropna(subset=['Nom_Prenom'])
df2 = df2.dropna(subset=['Nom_Prenom'])
df3 = df3.dropna(subset=['Nom_Prenom'])
df4 = df4.dropna(subset=['Nom_Prenom'])
df5 = df5.dropna(subset=['Nom_Prenom'])

df1['Date'] = df1['Date'].fillna(method='ffill')
df2['Date'] = df2['Date'].fillna(method='ffill')
df3['Date'] = df3['Date'].fillna(method='ffill')
df4['Date'] = df4['Date'].fillna(method='ffill')
df5['Date'] = df5['Date'].fillna(method='ffill')

df1=df1.drop(['Nom', 'Prénom'], axis=1)
df2=df2.drop(['Nom', 'Prénom'], axis=1)
df3=df3.drop(['Nom', 'Prénom'], axis=1)
df4=df4.drop(['Nom', 'Prénom'], axis=1)
df5=df5.drop(['Nom', 'Prénom'], axis=1)

df1['Date'] = pd.to_datetime(df1['Date'], format='%d/%m/%Y')
df1['Date'] = df1['Date'].dt.strftime('%Y-%m-%d')
df2['Date'] = pd.to_datetime(df2['Date'], format='%d/%m/%Y')
df2['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
df3['Date'] = pd.to_datetime(df3['Date'], format='%d/%m/%Y')
df3['Date'] = df3['Date'].dt.strftime('%Y-%m-%d')
df4['Date'] = pd.to_datetime(df4['Date'], format='%d/%m/%Y')
df4['Date'] = df4['Date'].dt.strftime('%Y-%m-%d')
df5['Date'] = pd.to_datetime(df5['Date'], format='%d/%m/%Y')
df5['Date'] = df5['Date'].dt.strftime('%Y-%m-%d')

df1['Date_Heure_Début'] = pd.to_datetime(df1['Date_Heure_Début'],format="%d/%m/%Y %H:%M:%S")
df2['Date_Heure_Début'] = pd.to_datetime(df2['Date_Heure_Début'],format="%d/%m/%Y %H:%M:%S")
df3['Date_Heure_Début'] = pd.to_datetime(df3['Date_Heure_Début'],format="%d/%m/%Y %H:%M:%S")
df4['Date_Heure_Début'] = pd.to_datetime(df4['Date_Heure_Début'],format="%d/%m/%Y %H:%M:%S")
df5['Date_Heure_Début'] = pd.to_datetime(df5['Date_Heure_Début'],format="%d/%m/%Y %H:%M:%S")

df1['Date_Heure_Fin'] = pd.to_datetime(df1['Date_Heure_Fin'],format="%d/%m/%Y %H:%M:%S")
df2['Date_Heure_Fin'] = pd.to_datetime(df2['Date_Heure_Fin'],format="%d/%m/%Y %H:%M:%S")
df3['Date_Heure_Fin'] = pd.to_datetime(df3['Date_Heure_Fin'],format="%d/%m/%Y %H:%M:%S")
df4['Date_Heure_Fin'] = pd.to_datetime(df4['Date_Heure_Fin'],format="%d/%m/%Y %H:%M:%S")
df5['Date_Heure_Fin'] = pd.to_datetime(df5['Date_Heure_Fin'],format="%d/%m/%Y %H:%M:%S")

df1['Heure_Début'] = df1['Date_Heure_Début'].dt.strftime('%H:%M:%S')
df2['Heure_Début'] = df2['Date_Heure_Début'].dt.strftime('%H:%M:%S')
df3['Heure_Début'] = df3['Date_Heure_Début'].dt.strftime('%H:%M:%S')
df4['Heure_Début'] = df4['Date_Heure_Début'].dt.strftime('%H:%M:%S')
df5['Heure_Début'] = df5['Date_Heure_Début'].dt.strftime('%H:%M:%S')

df1['Heure_Fin'] = df1['Date_Heure_Fin'].dt.strftime('%H:%M:%S')
df2['Heure_Fin'] = df2['Date_Heure_Fin'].dt.strftime('%H:%M:%S')
df3['Heure_Fin'] = df3['Date_Heure_Fin'].dt.strftime('%H:%M:%S')
df4['Heure_Fin'] = df4['Date_Heure_Fin'].dt.strftime('%H:%M:%S')
df5['Heure_Fin'] = df5['Date_Heure_Fin'].dt.strftime('%H:%M:%S')

df1['Horaire'] = df1['Heure_Début']+' - '+df1['Heure_Fin']
df2['Horaire'] = df2['Heure_Début']+' - '+df2['Heure_Fin']
df3['Horaire'] = df3['Heure_Début']+' - '+df3['Heure_Fin']
df4['Horaire'] = df4['Heure_Début']+' - '+df4['Heure_Fin']
df5['Horaire'] = df5['Heure_Début']+' - '+df5['Heure_Fin']

dfs = [df1, df2, df3, df4, df5]

# Concaténez les DataFrames de la liste en utilisant la fonction concat()
concatenated_df = pd.concat(dfs)

# Réinitialisez l'index du DataFrame concaténé
concatenated_df.reset_index(drop=True, inplace=True)

#concatenated_df['Date'] = pd.to_datetime(concatenated_df['Date'])
#concatenated_df['Date'] = concatenated_df['Date'].dt.strftime("%d/%m/%Y")

concatenated_df.to_csv('C:/Users/'+username+'/Imadis Téléradiologie/INTRANET - IMADIS/QUALITE/7- RHM/15 - DMA/GitHub/data/new_data.csv', index=False)
print("Le fichier new_data a été mis à jour.")

df_old=pd.read_csv('C:/Users/'+username+'/Imadis Téléradiologie/INTRANET - IMADIS/QUALITE/7- RHM/15 - DMA/GitHub/data/Concat_df.csv')
df_new=pd.read_csv('C:/Users/'+username+'/Imadis Téléradiologie/INTRANET - IMADIS/QUALITE/7- RHM/15 - DMA/GitHub/data/new_data.csv')

dfs = [df_old, df_new]

# Concaténez les DataFrames de la liste en utilisant la fonction concat()
data = pd.concat(dfs)

# Réinitialisez l'index du DataFrame concaténé
data.reset_index(drop=True, inplace=True)

data['Nom_Prenom']=data['Nom_Prenom'].str.upper()

data['Associé']=data['Associé'].fillna('Remplaçant')

data['Date_Heure_Fin'] = pd.to_datetime(data['Date_Heure_Fin'])
data['Date_Heure_Début'] = pd.to_datetime(data['Date_Heure_Début'])

data['Durée'] = data['Date_Heure_Fin'] - data['Date_Heure_Début']

data=data.drop_duplicates(subset=['Nom_Prenom', 'Date', 'Horaire'], keep='last')

data['Durée']=data['Durée'].astype(str)
data['Durée']=data['Durée'].str.split().str[2]
data['Durée'] = data['Durée'].str.replace("+", "", regex=False)
#data['Durée'] = data['Durée'].str.replace("+ ", "", regex=False)
data['Durée'] = pd.to_timedelta(data['Durée'])

# Calculez la durée en heures décimales
data['Durée'] = data['Durée'].dt.total_seconds() / 3600

data.to_csv('C:/Users/'+username+'/Imadis Téléradiologie/INTRANET - IMADIS/QUALITE/7- RHM/15 - DMA/GitHub/data/BDD.csv', index=False)
data.to_excel('C:/Users/'+username+'/Imadis Téléradiologie/INTRANET - IMADIS/QUALITE/7- RHM/15 - DMA/GitHub/data/BDD.xlsx', index=False)
print("La Base de Données du planning est désormais à jour.")

'''
#création du df indicateurs
df_planning=data.copy()
df_planning = df_planning[df_planning['Source'].isin(['PDS', 'CDS'])]
df_planning = df_planning[df_planning['Formation'].isna()]
df_planning=df_planning.drop(['mail', 'Chef'], axis=1)
df_planning['Date_Heure_Début'] = pd.to_datetime(df_planning['Date_Heure_Début'])
df_planning['Date_Heure_Fin'] = pd.to_datetime(df_planning['Date_Heure_Fin'])
df_planning['Date'] = pd.to_datetime(df_planning['Date'], format='%d/%m/%Y')
df_planning['Date'] = df_planning['Date'].dt.strftime("%d/%m/%Y")
heures = pd.date_range(start='00:00:00', end='23:00:00', freq='1H').time
colonnes_heures = []
for heure in heures:
    colonnes_heures.append(heure)
df_planning[colonnes_heures] = 0
for index, row in df_planning.iterrows():
    debut = row['Date_Heure_Début'].time()
    fin = row['Date_Heure_Fin'].time()
    if fin < debut:
        fin = datetime.time(23, 59, 59)  # Définir la fin sur 23h59:59
    for heure in heures:
        if debut <= heure <= fin:
            df_planning.at[index, heure] = 1

df_planning.to_csv('C:/Users/'+username+'/Imadis Téléradiologie/INTRANET - IMADIS/QUALITE/7- RHM/15 - DMA/GitHub/data/Indic.csv')
df_planning.to_excel('C:/Users/'+username+'/Imadis Téléradiologie/INTRANET - IMADIS/QUALITE/7- RHM/15 - DMA/GitHub/data/Indic.xlsx')

print("Le fichier Indic a été mis à jour.")
'''

df_old2=pd.read_csv('C:/Users/'+username+'/Imadis Téléradiologie/INTRANET - IMADIS/QUALITE/7- RHM/15 - DMA/GitHub/data/BDD.csv')
df_new2=pd.read_csv('C:/Users/'+username+'/Imadis Téléradiologie/INTRANET - IMADIS/QUALITE/7- RHM/15 - DMA/GitHub/data/new_data.csv')

dfs2 = [df_old, df_new]

# Concaténez les DataFrames de la liste en utilisant la fonction concat()
data = pd.concat(dfs2)

# Réinitialisez l'index du DataFrame concaténé
data.reset_index(drop=True, inplace=True)

data['Nom_Prenom']=data['Nom_Prenom'].str.upper()

data['Associé']=data['Associé'].fillna('Remplaçant')

data['Date_Heure_Fin'] = pd.to_datetime(data['Date_Heure_Fin'])
data['Date_Heure_Début'] = pd.to_datetime(data['Date_Heure_Début'])

data['Durée'] = data['Date_Heure_Fin'] - data['Date_Heure_Début']

data=data.drop_duplicates(subset=['Nom_Prenom', 'Date', 'Horaire'], keep='last')

data['Durée']=data['Durée'].astype(str)

data['Durée']=data['Durée'].str.split().str[2]

data['Durée'] = data['Durée'].str.replace("+", "", regex=False)
data['Durée'] = data['Durée'].str.replace("+ ", "", regex=False)

data['Durée'] = pd.to_timedelta(data['Durée'])

# Calculez la durée en heures décimales
data['Durée'] = data['Durée'].dt.total_seconds() / 3600

data.to_csv('C:/Users/'+username+'/Imadis Téléradiologie/INTRANET - IMADIS/QUALITE/7- RHM/15 - DMA/GitHub/data/data_increment.csv', index=False)
data.to_excel('C:/Users/'+username+'/Imadis Téléradiologie/INTRANET - IMADIS/QUALITE/7- RHM/15 - DMA/GitHub/data/data_increment.xlsx', index=False)
print("La Base de Données incrémentielle du planning est désormais à jour.")


print("FIN DU PROCESSSUS! :) ")