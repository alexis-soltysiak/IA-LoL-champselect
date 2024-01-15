from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import os
import numpy as np

def extract_draft_data(driver, match_id, team1_name, team2_name):
    data = []
    order_counter = 1

    base_xpath_team1_bans = '/html/body/div[1]/main/div[2]/div/div[3]/div/div/div/div[1]/div/div/div[2]/div[1]/div[3]/div/div[1]/div[2]/'
    base_xpath_team1_picks = '/html/body/div[1]/main/div[2]/div/div[3]/div/div/div/div[1]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/'

    base_xpath_team2_bans = '/html/body/div[1]/main/div[2]/div/div[3]/div/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div/div[1]/div[2]/'
    base_xpath_team2_picks = '/html/body/div[1]/main/div[2]/div/div[3]/div/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div/div[2]/div[2]/'

    ##############################################################################################################################
    # 1st ban phase

    #1 - BAN 1 - TEAM 1
    data.append([match_id, team1_name,  driver.find_element(By.XPATH, f'{base_xpath_team1_bans}a[{1}]/img').get_attribute('alt'), 'Ban', order_counter])
    order_counter += 1

    #2 - BAN 1 - TEAM 2
    data.append([match_id, team2_name,  driver.find_element(By.XPATH, f'{base_xpath_team2_bans}a[{1}]/img').get_attribute('alt'), 'Ban', order_counter])
    order_counter += 1

    #3 - BAN 2 - TEAM 1
    data.append([match_id, team1_name,  driver.find_element(By.XPATH, f'{base_xpath_team1_bans}a[{2}]/img').get_attribute('alt'), 'Ban', order_counter])
    order_counter += 1
    
    #4 - BAN 2 - TEAM 2
    data.append([match_id, team2_name,  driver.find_element(By.XPATH, f'{base_xpath_team2_bans}a[{2}]/img').get_attribute('alt'), 'Ban', order_counter])
    order_counter += 1

    #5 - BAN 3 - TEAM 1
    data.append([match_id, team1_name,  driver.find_element(By.XPATH, f'{base_xpath_team1_bans}a[{3}]/img').get_attribute('alt'), 'Ban', order_counter])
    order_counter += 1
    
    #6 - BAN 3 - TEAM 2
    data.append([match_id, team2_name,  driver.find_element(By.XPATH, f'{base_xpath_team2_bans}a[{3}]/img').get_attribute('alt'), 'Ban', order_counter])
    order_counter += 1

    ##############################################################################################################################
    # 1st pick phase

    #7 - PICK 1 - TEAM 1
    data.append([match_id, team1_name,  driver.find_element(By.XPATH, f'{base_xpath_team1_picks}a[{1}]/img').get_attribute('alt'), 'Pick', order_counter])
    order_counter += 1

    #8 - PICK 1 - TEAM 2
    data.append([match_id, team2_name,  driver.find_element(By.XPATH, f'{base_xpath_team2_picks}a[{1}]/img').get_attribute('alt'), 'Pick', order_counter])
    order_counter += 1

    #9- PICK 2 - TEAM 2
    data.append([match_id, team2_name,  driver.find_element(By.XPATH, f'{base_xpath_team2_picks}a[{2}]/img').get_attribute('alt'), 'Pick', order_counter])
    order_counter += 1

    #10 - PICK 2 - TEAM 1
    data.append([match_id, team1_name,  driver.find_element(By.XPATH, f'{base_xpath_team1_picks}a[{2}]/img').get_attribute('alt'), 'Pick', order_counter])
    order_counter += 1
    
    #11 - PICK 3 - TEAM 1
    data.append([match_id, team1_name,  driver.find_element(By.XPATH, f'{base_xpath_team1_picks}a[{3}]/img').get_attribute('alt'), 'Pick', order_counter])
    order_counter += 1

    #12 - PICK 3 - TEAM 2
    data.append([match_id, team2_name,  driver.find_element(By.XPATH, f'{base_xpath_team2_picks}a[{3}]/img').get_attribute('alt'), 'Pick', order_counter])
    order_counter += 1

    ##############################################################################################################################
    # 2nd ban phase


    #13 - BAN 1 - TEAM 2
    data.append([match_id, team2_name,  driver.find_element(By.XPATH, f'{base_xpath_team2_bans}a[{4}]/img').get_attribute('alt'), 'Ban', order_counter])
    order_counter += 1

    #14 - BAN 2 - TEAM 1
    data.append([match_id, team1_name,  driver.find_element(By.XPATH, f'{base_xpath_team1_bans}a[{4}]/img').get_attribute('alt'), 'Ban', order_counter])
    order_counter += 1
    
    #15 - BAN 2 - TEAM 2
    data.append([match_id, team2_name,  driver.find_element(By.XPATH, f'{base_xpath_team2_bans}a[{5}]/img').get_attribute('alt'), 'Ban', order_counter])
    order_counter += 1

    #16 - BAN 3 - TEAM 1
    data.append([match_id, team1_name,  driver.find_element(By.XPATH, f'{base_xpath_team1_bans}a[{5}]/img').get_attribute('alt'), 'Ban', order_counter])
    order_counter += 1

    ##############################################################################################################################
    # 2nd pick phase

    #17 - PICK 4 - TEAM 2
    data.append([match_id, team2_name,  driver.find_element(By.XPATH, f'{base_xpath_team2_picks}a[{4}]/img').get_attribute('alt'), 'Pick', order_counter])
    order_counter += 1

    #18 - PICK 4 - TEAM 1
    data.append([match_id, team1_name,  driver.find_element(By.XPATH, f'{base_xpath_team1_picks}a[{4}]/img').get_attribute('alt'), 'Pick', order_counter])
    order_counter += 1
    
    #19 - PICK 4 - TEAM 1
    data.append([match_id, team1_name,  driver.find_element(By.XPATH, f'{base_xpath_team1_picks}a[{5}]/img').get_attribute('alt'), 'Pick', order_counter])
    order_counter += 1

    #20 - PICK 5- TEAM 2
    data.append([match_id, team2_name,  driver.find_element(By.XPATH, f'{base_xpath_team2_picks}a[{5}]/img').get_attribute('alt'), 'Pick', order_counter])
    order_counter += 1


    return data


def check_time_value(driver):

    element = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div/div[3]/div/div/div/div[1]/div/div/div[1]/div[2]/h1')

    if element.text == "0:00":
        return True
    else:
       return False
    
def delete_csv():
    # Specify the path to the CSV file you want to delete
    file_path = 'bdd/draft_data.csv'  # Replace 'your_file.csv' with the actual file path

    # Check if the file exists before attempting to delete it
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{file_path} has been deleted.")
    else:
        print(f"{file_path} does not exist.")
        
        
        
        
#########################################



champion_names = [
    "<PAD>","Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe",
    "Aurelion Sol", "Azir", "Bard", "Belveth", "Blitzcrank", "Brand", "Braum", "Briar", "Caitlyn",
    "Camille", "Cassiopeia", "Chogath", "Corki", "Darius", "Diana", "Draven", "Dr. Mundo", "Ekko",
    "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen",
    "Gnar", "Gragas", "Graves", "Gwen", "Hecarim", "Heimerdinger", "Hwei", "Illaoi", "Irelia", "Ivern",
    "Janna", "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx", "Kaisa", "Kalista", "Karma", "Karthus",
    "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "KhaZix", "Kindred", "Kled", "KogMaw", "KSante",
    "LeBlanc", "Lee Sin", "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar",
    "Maokai", "Master Yi", "Milio", "Miss Fortune", "Mordekaiser", "Morgana", "Naafiri", "Nami", "Nasus",
    "Nautilus", "Neeko", "Nidalee", "Nilah", "Nocturne", "Nunu", "Olaf", "Orianna", "Ornn",
    "Pantheon", "Poppy", "Pyke", "Qiyana", "Quinn", "Rakan", "Rammus", "RekSai", "Rell", "Renata Glasc",
    "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Samira", "Sejuani", "Senna", "Seraphine", "Sett",
    "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Sylas",
    "Syndra", "Tahm Kench", "Taliyah", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle",
    "Tryndamere", "Twisted Fate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "VelKoz", "Vex",
    "Vi", "Viego", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah", "Xerath", "Xin Zhao",
    "Yasuo", "Yone", "Yorick", "Yuumi", "Zac", "Zed", "Zeri", "Ziggs", "Zilean", "Zoe", "Zyra"
]

champion_names_without_pad = [
    "<PAD>","Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe",
    "Aurelion Sol", "Azir", "Bard", "Belveth", "Blitzcrank", "Brand", "Braum", "Briar", "Caitlyn",
    "Camille", "Cassiopeia", "Chogath", "Corki", "Darius", "Diana", "Draven", "Dr. Mundo", "Ekko",
    "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen",
    "Gnar", "Gragas", "Graves", "Gwen", "Hecarim", "Heimerdinger", "Hwei", "Illaoi", "Irelia", "Ivern",
    "Janna", "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx", "Kaisa", "Kalista", "Karma", "Karthus",
    "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "KhaZix", "Kindred", "Kled", "KogMaw", "KSante",
    "LeBlanc", "Lee Sin", "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar",
    "Maokai", "Master Yi", "Milio", "Miss Fortune", "Mordekaiser", "Morgana", "Naafiri", "Nami", "Nasus",
    "Nautilus", "Neeko", "Nidalee", "Nilah", "Nocturne", "Nunu", "Olaf", "Orianna", "Ornn",
    "Pantheon", "Poppy", "Pyke", "Qiyana", "Quinn", "Rakan", "Rammus", "RekSai", "Rell", "Renata Glasc",
    "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Samira", "Sejuani", "Senna", "Seraphine", "Sett",
    "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Sylas",
    "Syndra", "Tahm Kench", "Taliyah", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle",
    "Tryndamere", "Twisted Fate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "VelKoz", "Vex",
    "Vi", "Viego", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah", "Xerath", "Xin Zhao",
    "Yasuo", "Yone", "Yorick", "Yuumi", "Zac", "Zed", "Zeri", "Ziggs", "Zilean", "Zoe", "Zyra"
]


df = pd.read_csv('bdd/draft_data_all.csv')



num_champions = len(champion_names)
champion_to_index = {champion: index for index, champion in enumerate(champion_names)}
index_to_champion = {v: k for k, v in champion_to_index.items()}

def champion_to_one_hot(champion, is_pick):
    one_hot = np.zeros(num_champions + 3)  # +3 pour les dimensions pick et ban
    one_hot[champion_to_index[champion]] = 1
    if is_pick == "Pick":
        one_hot[-3] = 1
    elif is_pick == "Ban" : 
        one_hot[-2] = 1 
    else  : 
        one_hot[-1] = 1 
    return one_hot

def output_champion_to_one_hot(champion):
    one_hot = np.zeros(num_champions )  # +3 pour les dimensions pick et ban
    one_hot[champion_to_index[champion]] = 1
    return one_hot


def translate_to_champions(data, is_sequence=True):
    all_translations = []
    
    for item in data:
        if is_sequence:  # Si les données sont des séquences (comme X_train)
            champions_sequence = []
            for vector in item:
                if np.sum(vector[:-2]) == 0:  # Vérifie si le vecteur est un padding
                    champions_sequence.append('Padding')
                else:
                    champion_index = np.argmax(vector[:-2])
                    champion_name = index_to_champion[champion_index]
                    champions_sequence.append(champion_name)
            all_translations.append(champions_sequence)
        else:  # Si les données sont des vecteurs uniques (comme Y_train)
            if np.sum(item[:-2]) == 0:
                all_translations.append('Padding')
            else:
                champion_index = np.argmax(item[:-2])
                champion_name = index_to_champion[champion_index]
                all_translations.append(champion_name)
    
    return all_translations





def predict_next_champion(champion_list, model):
    
    input_sequence = [champion_to_one_hot("<PAD>", "None") for _ in range(20)]

    for j in range(len(champion_list)):

        previous_champion = champion_list['Champion']
        previous_type = "Ban"
        input_sequence[j] = champion_to_one_hot(previous_champion, previous_type)

    # Convertir en format requis par le modèle (1, 20, 170)
    sequence_input = np.array([input_sequence])


    predicted_vector = model.predict(sequence_input)[0]  # Prendre la première prédiction

    # Convertir le vecteur prédit en nom de champion
    predicted_champion_index = np.argmax(predicted_vector[:-2]) 
    predicted_champion = index_to_champion[predicted_champion_index]
    return predicted_champion

def predict_top_5_champions(champion_list, model):
    
    input_sequence = [champion_to_one_hot("<PAD>", "None") for _ in range(20)]

    for j in range(len(champion_list)):

        previous_champion = champion_list[j]
        previous_type = "ban"
        input_sequence[j] = champion_to_one_hot(previous_champion, previous_type)

    
    # Convertir en format requis par le modèle (1, 20, 170)
    sequence_input = np.array([input_sequence])

    # Faire la prédiction
    predicted_vector = model.predict(sequence_input)[0]

    # Trier les probabilités et prendre les 5 indices supérieurs
    top_5_indices = np.argsort(predicted_vector[:-2])[-5:]

    # Convertir les indices en noms de champions
    top_5_champions = [index_to_champion[index] for index in reversed(top_5_indices)]

    return top_5_champions



def list_champions_to_vector(liste_champions):
    num_champions = len(champion_to_index)
    one_hot = np.zeros(num_champions)

    # Parcourez la liste des champions et mettez 1 à l'index correspondant dans le vecteur
    for i,champion in enumerate(liste_champions):
        index = champion_to_index.get(champion, None)  # Obtenez l'index à partir du dictionnaire
        if index is not None:
            if i == 0 or i == 3 or i == 4 or i ==7 or i == 9 : 
                one_hot[index] = 1
            else :  
                one_hot[index] = 2

    return one_hot


def predict_top_5_champions(model, liste_champions):
    # Transformez la liste de champions en vecteur one-hot
    input_vector = list_champions_to_vector(liste_champions)
    
    # Effectuez une prédiction avec le modèle
    predictions = model.predict(np.array([input_vector]))  # Le modèle s'attend à une entrée de forme (1, num_champions)
    
    # Obtenez les indices des 5 champions prédits (les indices avec les plus hautes probabilités)
    top_5_indices = np.argsort(predictions[0])[-5:][::-1]
    
    # Trouvez les champions correspondants aux indices prédits dans le dictionnaire champion_to_index
    top_5_champions = []
    for index in top_5_indices:
        for champion, champ_index in champion_to_index.items():
            if champ_index == index:
                top_5_champions.append(champion)
                break
    
    return top_5_champions