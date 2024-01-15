from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException
from tqdm import tqdm
from functions import *

driver = webdriver.Chrome()


listAllData = []

df = pd.DataFrame(columns=['Match ID', 'Team', 'Champion', 'Type', 'Order'])

driver = webdriver.Chrome()

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

    try : 
        match_data = extract_draft_data(driver, matchString, team1Name, team2Name)
        # Ajoutez les données du match au DataFrame existant
        df = df.append(match_data, ignore_index=True)
    except : 
        continue 
    
    
# Fermez le navigateur lorsque vous avez terminé
driver.quit()

# Enregistrez le DataFrame dans un fichier CSV
csvFile = 'bdd/draft_data.csv'

delete_csv()
df.to_csv(csvFile, header=True, index=False)

print(f"Les données de draft ont été ajoutées au fichier {csvFile}.")