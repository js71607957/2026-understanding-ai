import pickle
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from hand_features import describe_hand

# 과제에서 제공한 학습 데이터
data = pd.read_csv("poker-hand-training.csv")
labels = data.iloc[:, -1]

# 공개된 카드가 3장일 때와 4장일 때의 모델을 각각 학습
for visible in (3, 4):
    rows = data.iloc[:, :visible * 2].itertuples(index=False, name=None)
    features = []

    for row in rows:
        cards = list(zip(row[::2], row[1::2]))
        features.append(describe_hand(cards))

    # Ch04 분류 강의자료에 분류 모델 예시로 제시된 Decision Tree 사용
    model = DecisionTreeClassifier(
        max_depth=10,
        min_samples_leaf=16,
        random_state=17
    )
    model.fit(features, labels)

    filename = f"poker-model{visible}.sav"
    with open(filename, "wb") as file:
        pickle.dump(model, file, protocol=4)

    print(f"{filename} saved.")
