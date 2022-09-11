import re

def pig_it(text):
    words = []
    pig = ""
    piggies = []
    sentence = ""
    i = 0
    words = text.split(" ")
    for word in words:
        if re.search(r"\w", word):
            pig = word[1:len(word)] + word[0] + "ay"
            piggies.append(pig)
        else:
            piggies.append(word)
    for piggy in piggies:
        sentence += piggy + " "
        
    return sentence.strip()