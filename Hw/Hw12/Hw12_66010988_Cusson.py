#Question 1
def textese(text):
    dict1 = {
        "be" : "b",
        "because" : "cuz",
        "see" : "c",
        "the" : "da",
        "okay" : "ok",
        "are" : "r",
        "you" : "u",
        "without" : "w/o",
        "why" : "y",
        "ate" : "8",
        "great" : "gr8",
        "mate" : "m8",
        "wait" : "w8",
        "later" : "l8r",
        "tomorrow" : "2mro",
        "for" : "4",
        "before" : "b4",
        "once" : "1ce",
        "and" : "&",
        "Your" : "ur",
        "your" : "ur",
        "Your're" : "ur",
        "your're" : "ur",
        "see you" : "cu",
        "At the moment" : "atm",
        "Be right back" : "brb",
        "By the way" : "btw",
        "For your information" : "FYI",
        "In my opinion" : "imo",
        "Oh my god" : "omg",
        "Laughing out loud": "lol",
        "As soon as possible" : "ASAP",
        "In my humble opinion" : "imho",
        "Talk to you later" : "ttyl",
        "As far as I know" : "afaik",
        "Rolling on the floor laughing" : "rofl"
        
    }
    words = text.split()
    result = []
    i = 0
    while i < len(words):
        for j in range(len(words), i, -1):
            joined_words = ' '.join(words[i:j])
            replacement = dict1.get(joined_words, None)
            if replacement:
                result.append(replacement)
                i = j
                break
        else:
            result.append(words[i])
            i += 1

    return ' '.join(result)

print(textese("be because Laughing out loud As soon as possible Rolling on the floor laughing"))

def untextese(text):
    dict1 = {
        "b": "be",
        "cuz": "because",
        "c": "see",
        "da": "the",
        "ok": "okay",
        "r": "are",
        "u": "you",
        "w/o": "without",
        "y": "why",
        "8": "ate",
        "gr8": "great",
        "m8": "mate",
        "w8": "wait",
        "l8r": "later",
        "2mro": "tomorrow",
        "4": "for",
        "b4": "before",
        "1ce": "once",
        "&": "and",
        "ur": "Your",
        "cu": "see you",
        "atm": "At the moment",
        "brb": "Be right back",
        "btw": "By the way",
        "FYI": "For your information",
        "imo": "In my opinion",
        "omg": "Oh my god",
        "lol": "Laughing out loud",
        "ASAP": "As soon as possible",
        "imho": "In my humble opinion",
        "ttyl": "Talk to you later",
        "afaik": "As far as I know",
        "rofl": "Rolling on the floor laughing"
    }

    splited = text.split()
    result = [dict1.get(word, None) for word in splited]

    return " ".join(result)
 
print(untextese("b cuz lol ASAP rofl"))


#Question 2
def composite(dict1, dict2):
    result = {}
    for key,value in dict1.items():
        value2 = dict2.get(value, None)
        if value2 == None:
            continue
        result[key] = value2
    return result

dict1 = {
    "a" : "p",
    "b" : "r",
    "c" : "q",
    "d" : "p",
    "e" : "s"
}

dict2 = {
    "p" : "1",
    "q" : "2",
    "r" : "3",
}

print(composite(dict1, dict2))


#Question 3
def cartesian_product(*sets):
    result = set()
    for element in sets[0]:
        if len(sets) == 1:
            result.add((element,))
        else:
            for product in cartesian_product(*sets[1:]):
                result.add((element,) + product)
    return result

s1 = set([1, 2, 3])
s2 = set(["p", "q"])
s3 = set(["a", "b", "c"])

print(cartesian_product(s1, s2))
print(cartesian_product(s1, s2, s3))


