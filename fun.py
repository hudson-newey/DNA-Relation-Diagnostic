def matchNucleobase(strand):
    corrosponding={
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

    return corrosponding.get(strand, "Invalid Nucleobase Base...")

def reverseString(string):
    return string[::-1]

def readFile(fileName):
    file1 = open(fileName,"r")
    print (file1.readlines())
    file1.close()