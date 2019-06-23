import json
import random

def handle(req):
    with open('./function/idioms_dict.json', 'r') as f:
        words = json.load(f)
    try:
        req = str(req).strip()
        if req not in words[req[0]]:
            return 'the idiom not exist'
        next_words = words.get(req[-1], [])
        length = len(next_words)
        if length == 0:
            return "can't find the next idion"
        word = next_words[random.randint(0, length - 1)]
        return word
    except:
        return 'bad parameter'
