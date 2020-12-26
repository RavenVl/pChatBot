import json


def get_bot_config():
    with open('big_bot_config.json') as f:
        BOT_CONFIG = json.load(f)
    return BOT_CONFIG
