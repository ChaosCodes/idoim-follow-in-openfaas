import json
import random

def idoim_follow(w):
    with open('./idioms_dict.json', 'r') as f:
        words = json.load(f)
    try:
        if w not in words[w[0]]:
            print('the idiom not exist')
            return
        next_words = words.get(w[-1], [])
        length = len(next_words)
        if length == 0:
            print("can't find the next idion")
            return
        word = next_words[random.randint(0, length - 1)]
        print(word)
    except:
        print('bad parameter')

if __name__ == "__main__":
    word = input()
    idoim_follow(word.strip())