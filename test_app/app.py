from flask import Flask, escape, request
import json
import random

app = Flask(__name__)

@app.route('/')
def get_idom():
    idom = request.args.get("idom", "人山人海")
    with open('./idioms_dict.json', 'r') as f:
        words = json.load(f)
    try:
        idom = str(idom).strip()
        if idom not in words[idom[0]]:
            return 'the idiom not exist'
        next_words = words.get(idom[-1], [])
        length = len(next_words)
        if length == 0:
            return "can't find the next idion"
        word = next_words[random.randint(0, length - 1)]
        return word
    except:
        return 'bad parameter'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)