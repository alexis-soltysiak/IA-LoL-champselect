from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException
from tqdm import tqdm
from functions import *

driver = webdriver.Chrome()


listAllData = []

delete_csv()

df = pd.DataFrame(listAllData, columns=['Match ID', 'Team', 'Champion', 'Type', 'Order'])

for matchId in tqdm(range(50000, 53790)):

    url = f'https://gol.gg/game/stats/{matchId}/page-game/'
    
    try:
        driver.get(url)
        if check_time_value(driver):
            #print(f"[INFO] - Skipping match number {matchId} due to time check")
            continue
    except:
        continue

    matchString = str(matchId)


    team1Name = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div/div[3]/div/div/div/div[1]/div/div/div[2]/div[1]/div[1]/div/a').text
    team2Name = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div/div[3]/div/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div/a').text

    #print(f"[INFO] - working on match number {matchId} with {team1Name} vs {team2Name}")

    #time.sleep(0.1)

    try : 
        match_data = extract_draft_data(driver, matchString, team1Name, team2Name)
        listAllData.extend(match_data)
    except : 
        continue 

# Fermez le navigateur lorsque vous avez terminé
driver.quit()

# Créez un DataFrame à partir de la liste listAllData

# Enregistrement des données dans un fichier CSV (mode 'a' pour ajouter)
csvFile = 'bdd/draft_data.csv'

df = pd.DataFrame(listAllData, columns=['Match ID', 'Team', 'Champion', 'Type', 'Order'])

df.to_csv(csvFile, mode='a', header=True, index=False)

print(f"Les données de draft ont été ajoutées au fichier {csvFile}.")