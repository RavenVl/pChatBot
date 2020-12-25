import re


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
    if match(text) == match(example):
        return True
    else:
        return False


def get_intent(text):
    for intent, data in BOT_CONFIG['intents'].items():
        if text in data['examples']:
            return intent


if __name__ == '__main__':
    get_intent('здравствуйте')
    filter('здравствуйте q - !@#')
