import re, random
import nltk
from bot_config import get_bot_config
BOT_CONFIG = get_bot_config()


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


def get_answer_by_intent(intent):
    return random.choice(BOT_CONFIG['intents'][intent]['responses'])


def bot(text):
    # понять намерение
    intent = get_intent(text)
    if intent:
        return get_answer_by_intent(intent)
    # сгененерить ответ по контесксту
    # TODO mashin learning

    # вернуть случайную фразу
    return random.choice(BOT_CONFIG['failure_phrases'])


if __name__ == '__main__':
    # print(bot('прощяй!'))
    # print(bot('ыфвфывфв'))
    req = ''
    while True:
        req = input('--')
        if req in ['выход', 'достал']:
            break
        print(bot(req))
