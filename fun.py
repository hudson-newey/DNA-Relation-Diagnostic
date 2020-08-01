from difflib import SequenceMatcher

def checkNucleobase(base, RNA):
    print(RNA)

    if (not RNA or RNA == "unknown"):
        possabilities = ["A", "C", "T", "G"]
        for i in range(len(possabilities)):
            if (base == possabilities[i]):
                return True
    else:
        possabilities = ["A", "C", "U", "G"]
        for i in range(len(possabilities)):
            if (base == possabilities[i]):
                return True

    return False

def reverseString(string):
    return string[::-1]

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()