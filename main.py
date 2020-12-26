import re, random
import nltk
from bot_config import get_bot_config
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

BOT_CONFIG = get_bot_config()
x_input = []
y = []
for intent, data in BOT_CONFIG['intents'].items():
    for el in data['examples']:
        x_input.append(el)
        y.append(intent)
tfidf_vectorizer = TfidfVectorizer(analyzer='char_wb', ngram_range=(2, 4))
X = tfidf_vectorizer.fit_transform(x_input)
lin_svc = LinearSVC(penalty='l2')
lin_svc.fit(X, y)

def filter(text: str):
    text = text.lower()
    return ''.join(re.findall(r'\w|-| ', text))


def match(text, example):
    nltk.edit_distance(filter(text), filter(example))
    distance = nltk.edit_distance(filter(text), filter(example)) / len(example)
    if distance < 0.4:
        return True
    else:
        return False


def get_intent(text):
    for intent, data in BOT_CONFIG['intents'].items():
        for ask in data['examples']:
            if match(text, ask):
                return intent

def get_intent_predictive_model(text):

    return lin_svc.predict(tfidf_vectorizer.transform([text]))[0]



def get_answer_by_intent(intent):
    return random.choice(BOT_CONFIG['intents'][intent]['responses'])


def bot(text):
    # понять намерение
    intent = get_intent(text)

    if not intent:
        intent = get_intent_predictive_model(text)

    if intent:
        print(intent)
        return get_answer_by_intent(intent)

    # вернуть случайную фразу
    return random.choice(BOT_CONFIG['failure_phrases'])


if __name__ == '__main__':
    req = ''
    while True:
        req = input('--')
        if req in ['выход', 'достал']:
            break
        print(bot(req))
    # use_mo()
