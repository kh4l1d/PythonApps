import random,string

def generator():
    letter1 = random.choice(string.ascii_letters)
    letter2 = random.choice(string.ascii_letters)
    letter3 = random.choice(string.ascii_letters)
    word = letter1 + letter2 + letter3
    return word

print(generator())
