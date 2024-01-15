
import numpy as np
from tqdm import tqdm
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from keras.models import save_model
from keras.models import load_model
from functions import *
from keras.models import Sequential
from keras.layers import Dense, Dropout, Input


df = pd.read_csv('bdd/draft_data_all.csv')

df = df[df["Type"] == "Pick"]


num_champions = len(champion_names_without_pad)
champion_to_index = {champion: index for index, champion in enumerate(champion_names_without_pad)}
index_to_champion = {v: k for k, v in champion_to_index.items()}

X = []
Y = []


df = df.sort_values(by=['Match ID', 'Order'])
grouped = df.groupby('Match ID')

if 0 == 0 : 
    model = load_model("bdd/mon_modele2.h5")
else :
    for match_id, match_data in tqdm(grouped):


        for i in range(len(match_data)):


            list_champions = match_data["Champion"][:i].tolist()
            championToAim  = [match_data["Champion"].iloc[i]]

            xToAppend = list_champions_to_vector(list_champions)
            yToAppend = list_champions_to_vector(championToAim)

            X.append(xToAppend)
            Y.append(yToAppend)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


    #
    # Construction du modèle
    model = Sequential([
        Input(shape=(len(X_train[0]),)),
        Dense(128, activation='relu'),  # Augmentation du nombre de neurones
        Dense(128, activation='tanh'),
        Dropout(0.2),
        Dense(len(Y_train[0]), activation='softmax')
    ])
    # Compilez le modèle en spécifiant la fonction de perte et l'optimiseur
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Entraînez le modèle sur les données d'entraînement
    model.fit(np.array(X_train), np.array(Y_train), epochs=50, batch_size=8, validation_split=0.2)

    model.save("bdd/mon_modele2.h5")




input_champions = ['Renekton', 'Maokai','Arhi'] #APHELIOS , PYKE
predicted_champions = predict_top_5_champions(model, input_champions)
print(f"Top 5 champions prédits : {predicted_champions}")