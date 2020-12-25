import re
import nltk

BOT_CONFIG = {
    'intents': {
        'hello': {
            'examples': ['привет', 'добрый день', 'здравствуйте'],
            'response': ['привет человек', 'доброго времени суток']
        },
        'bay': {
            'examples': ['пока', 'досвидания', 'прощай'],
            'response': ['счастливо', 'если чего возвращайся', ]
        }
    },
    'failure_phrases': ['Ничего не понятно', 'Чего, чего?']
}


def filter(text: str):
    text = text.lower()
    return ''.join(re.findall(r'\w|-| ', text))



def match(text, example):
    nltk.edit_distance(filter(text), filter(example))
    if nltk.edit_distance(filter(text), filter(example)) <= 2:
        return True
    else:
        return False


def get_intent(text):
    for intent, data in BOT_CONFIG['intents'].items():
        for ask in data['examples']:
            if match(text, ask):
                return intent


if __name__ == '__main__':
    print(get_intent('прощай'))

