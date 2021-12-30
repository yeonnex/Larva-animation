# Description : 한국어 챗봇 만들기 프로젝트 시작!!!
import random
import json
import pickle
import numpy as np
from konlpy.tag import Twitter

import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

intents = json.loads(open('intents.json',encoding='UTF8').read())

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
#print(documents) # 토큰화된 토큰들이 tag와 쌍을 맞추어 튜플 형태로 출력
words = sorted(set(words))

classes = sorted(set(classes))

pickle.dump(words,open('words.pkl', 'wb'))
pickle.dump(classes,open('classes.pkl', 'wb'))

training = []
output_empty = [0] * len(classes)

twitter = Twitter()
# malist = twitter.pos("흔들리는 꽃들 속에서 네 샴푸향이 느껴진거야", norm=True, stem=True)

for document in documents:
    bag = []
    word_patterns = document[0]
    print(word_patterns)
    #word_patterns = [twitter.pos(word) for word in word_patterns]
    #print(word_patterns)
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)
    print(word_patterns)
    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)

train_x = list(training[:,0])
train_y = list(training[:,1])

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)

# 컴파일
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('chatbotmodel.h5', hist)

print('Done')