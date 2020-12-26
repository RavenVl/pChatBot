import re, random
import nltk

BOT_CONFIG = {
    'intents': {
        'hello': {
            'examples': ['привет', 'добрый день', 'здравствуйте'],
            'response': ['привет человек', 'доброго времени суток']
        },
        'bay': {
            'examples': ['пока', 'досвидания', 'прощай'],
            'response': ['счастливо', 'если чего возвращайся', 'bay, bay', 'good bay']
        },
        'whatsup': {
            'examples': ['как дела', 'чо как', 'как ты'],
            'response': ['норм', 'все ок', 'пока живой', 'все отлично']
        }
    },
    'failure_phrases': ['Ничего не понятно', 'Чего, чего?']
}


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
    return random.choice(BOT_CONFIG['intents'][intent]['response'])


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
