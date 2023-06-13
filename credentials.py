import json

data = json.load(open('creds.json'))


def id():
    return data['id']

def secret():
    return data['secret']

def url():
    return data['url']
