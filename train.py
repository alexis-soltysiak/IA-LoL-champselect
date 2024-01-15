import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
import numpy as np
import spacy
from tqdm import tqdm

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from keras.initializers import glorot_uniform
from keras.models import save_model
from keras.models import load_model
from keras.layers import LSTM, Dense, Dropout, Flatten, BatchNormalization, LeakyReLU


from functions import *


df = pd.read_csv('bdd/draft_data_all.csv')



num_champions = len(champion_names)
champion_to_index = {champion: index for index, champion in enumerate(champion_names)}
index_to_champion = {v: k for k, v in champion_to_index.items()}

X = []
Y = []


df = df.sort_values(by=['Match ID', 'Order'])
grouped = df.groupby('Match ID')

if 0 == 0 : 
    model = load_model("bdd/mon_modele.h5")
else :
    for match_id, match_data in tqdm(grouped):
        #print(f"Traitement du Match ID: {match_id}")
        
        for i in range(len(match_data)):
            row = match_data.iloc[i]
            champion = row['Champion']
            type = row['Type']

            input_sequence = [champion_to_one_hot("<PAD>", "None") for _ in range(20)]
            
            for j in range(i):
                previous_row = match_data.iloc[j]
                previous_champion = previous_row['Champion']
                previous_type = previous_row['Type']
                input_sequence[j] = champion_to_one_hot(previous_champion, previous_type)

                
            X.append(input_sequence)
            Y.append(output_champion_to_one_hot(champion))
            

    # Conversion des listes en arrays NumPy
    X_np = np.array(X)
    Y_np = np.array(Y)

    """
    translated_X_train = translate_to_champions(X_np, is_sequence=True)
    print(translated_X_train)

    translated_Y_train = translate_to_champions(Y_np, is_sequence=False)
    print(translated_Y_train)
    """

    X_train, X_test, y_train, y_test = train_test_split(X_np, Y_np, test_size=0.2, random_state=42)


    input_shape = X_train.shape[1:]
    output_shape = y_train.shape[1]  # Notez l'utilisation de y_train, pas Y_train


    weight_initializer = glorot_uniform(seed=42)

    model = Sequential()

    """
    #MODEL 1
    model.add(LSTM(units=64, return_sequences=True, input_shape=input_shape))
    model.add(LSTM(units=32))
    model.add(Dense(output_shape, activation='softmax'))
    """
    #MODEL 2 
    # Couche LSTM avec retour de séquence
    # Couche LSTM avec retour de séquence
    model.add(LSTM(units=64, return_sequences=True, input_shape=input_shape))
    model.add(Dropout(0.2))  # Ajouter une couche de dropout pour la régularisation

    # Une couche Flatten pour aplatir la sortie de la couche LSTM
    model.add(Flatten())

    # Couche Dense (complètement connectée) avec activation Leaky ReLU
    model.add(Dense(128))
    model.add(BatchNormalization())  # Ajouter la couche de batch normalization
    model.add(LeakyReLU(alpha=0.1))  # Ajouter l'activation Leaky ReLU
    model.add(Dropout(0.2))
    
  
    # Couche de sortie avec activation softmax
    model.add(Dense(output_shape, activation='softmax'))


    custom_lr = 0.01  # Modifiez ce taux d'apprentissage selon vos besoins
    optimizer = Adam(learning_rate=custom_lr)

    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

    model.summary()

    model.fit(X_train, y_train, epochs=20, batch_size=16, validation_data=(X_test, y_test))
    model.save("bdd/mon_modele.h5")


###########################
#PREDICT



champion_list = [] # Remplacez par votre liste de champions
top_5_champions = predict_top_5_champions(champion_list, model)
print("Top 5 champions prédits :", top_5_champions)