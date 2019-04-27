import json


def reading_key(file_name, searched):
    with open('config/' + file_name + '.json', 'r') as f:
        cont = json.load(f)
        try:
            return cont[searched]
        except:
            return None


def read_config(searched):
    return reading_key("config", searched)