import json


passwords = []

try:
    with open('users_ides.json', 'r') as f:
        users_ides = json.load(f)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    users_ides = {}
    fs = open('users_ides.json', 'w')
    fs.write(json.dumps(users_ides))
    fs.close()
    del fs
