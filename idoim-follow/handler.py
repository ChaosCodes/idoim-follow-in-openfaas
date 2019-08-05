import json
import random

def handle(req):
    r = req
    with open('./function/idioms_dict.json', 'r') as f:
        words = json.load(f)

    return r
