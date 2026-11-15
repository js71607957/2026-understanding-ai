PROJECT 2 - POKER HAND PREDICTION BY CLASSIFICATION
제출용 파일 안내

[구성]
- poker.py: 과제에서 제공한 Pygame 게임 구조와 predict_call() 구현
- train.py: 3장/4장 카드 분류 모델 학습 및 저장
- hand_features.py: 카드 정보에서 학습용 특징을 추출
- poker-model3.sav, poker-model4.sav: 학습된 모델
- poker-hand-training.csv: 학습 데이터
- poker-hand-testing.csv: 테스트 데이터 및 게임용 데이터
- cards.jpg, flipcard.wav: 게임 이미지 및 효과음

[실행 순서]
1. 필요한 패키지 설치
   py -m pip install pandas scikit-learn pygame-ce
2. 모델 학습
   py train.py
3. 테스트 데이터 평가 (선택)
   py evaluate.py
4. 게임 실행
   py poker.py

[구현 설명]
- 지도학습 분류 모델로 DecisionTreeClassifier를 사용합니다.
- Ch04 분류 강의자료에서 Decision Tree가 지도학습 분류 모델의 예시로 언급됩니다.
- Ch03 Feature Engineering 강의의 특징 추출 개념을 적용해 카드의 숫자 중복, 문양 중복, 스트레이트 가능성을 특징으로 변환합니다.
- 3장 모델과 4장 모델을 각각 학습합니다.
- predict_proba() 결과로 포커 점수의 기댓값을 계산하고, 상대방 점수보다 높으면 CALL을 반환합니다.

[테스트 결과]
별도 테스트 데이터에서 확인한 정확도:
- 3장 모델: 0.6302
- 4장 모델: 0.7739

정확도는 해당 테스트 데이터에서 계산한 값이며, 모든 게임 상황에서의 승률을 보장하지는 않습니다.
