import pickle
import pandas as pd
from hand_features import describe_hand

data = pd.read_csv("poker-hand-testing.csv")
labels = data.iloc[:, -1]

for visible in (3, 4):
    rows = data.iloc[:, :visible * 2].itertuples(index=False, name=None)
    features = [describe_hand(list(zip(row[::2], row[1::2]))) for row in rows]
    with open(f"poker-model{visible}.sav", "rb") as file:
        model = pickle.load(file)
    predictions = model.predict(features)
    accuracy = (predictions == labels).sum() / labels.count()
    print(f"{visible}-card test accuracy: {accuracy:.4f}")
