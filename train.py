import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
import numpy as np

champion_names = [
    "Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe",
    "Aurelion Sol", "Azir", "Bard", "Belveth", "Blitzcrank", "Brand", "Braum", "Briar", "Caitlyn",
    "Camille", "Cassiopeia", "Chogath", "Corki", "Darius", "Diana", "Draven", "Dr.Mundo", "Ekko",
    "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen",
    "Gnar", "Gragas", "Graves", "Gwen", "Hecarim", "Heimerdinger", "Hwei", "Illaoi", "Irelia", "Ivern",
    "Janna", "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx", "Kaisa", "Kalista", "Karma", "Karthus",
    "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Khazix", "Kindred", "Kled", "Kogmaw", "KSante",
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


    
df = pd.read_csv('bdd/draft_data.csv')

# Créer le tokenizer et ajuster sur les noms des champions
tokenizer = Tokenizer()
tokenizer.fit_on_texts(champion_names)

# Convertir les noms des champions en séquences numériques
champion_sequences = tokenizer.texts_to_sequences(df['Champion'])

# Créer les vecteurs one-hot
num_champions = len(tokenizer.word_index) + 1
one_hot_sequences = np.zeros((len(champion_sequences), num_champions))


print(one_hot_sequences)
for i, seq in enumerate(champion_sequences):
    if len(seq) > 0:  # Vérifiez que la séquence n'est pas vide
        one_hot_sequences[i, seq[0]] = 1
    else:
        print(f"Aucune correspondance trouvée pour : {df['Champion'].iloc[i]}")



# Préparer les séquences d'entrée (X) et de sortie (y)
sequence_length = 20
X = []
y = []

for i in range(len(one_hot_sequences) - sequence_length):
    X.append(one_hot_sequences[i:i+sequence_length])
    y.append(one_hot_sequences[i+sequence_length])

X = np.array(X)
y = np.array(y)

# Diviser les données
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Construction du modèle LSTM
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(sequence_length, num_champions)),
    LSTM(50),
    Dense(num_champions, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=20, batch_size=1, validation_data=(X_test, y_test))


##TEST
champions = ['Renata Glasc', 'Draven', 'Ashe', 'Kalista']

sequences = tokenizer.texts_to_sequences(champions)
one_hot_sequences = pad_sequences(sequences, maxlen=20)


input_sequence = np.zeros((1, 20, len(tokenizer.word_index) + 1))
for i, sequence in enumerate(one_hot_sequences):
    for j, value in enumerate(sequence):
        if value != 0:
            input_sequence[0, i, value] = 1


predicted = model.predict(input_sequence)
predicted_champion_index = np.argmax(predicted, axis=-1)[0]
predicted_champion = tokenizer.index_word[predicted_champion_index]

print("Le cinquième champion prédit est :", predicted_champion)


