from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import os

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