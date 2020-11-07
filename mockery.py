import random

def memify(text):
    new = []
    for i in text:
        r = random.randint(0,1)
        if r == 1:
            new.append(i.upper())
        else:
             new.append(i.lower())
    new = ''.join(new)
    return new

