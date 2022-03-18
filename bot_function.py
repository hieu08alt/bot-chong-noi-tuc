import json


def config_bot():
    with open('config.json', 'r') as f:
        config = json.load(f)
        return config


def get_badword():
    with open("bad_word.txt", 'r', encoding="utf8") as f:
        temp = f.read()
    return temp.split('\n')
