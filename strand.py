from ui import *
from fun import *

class Strand:
    def create():
        currentStrand = ""

        # conformation to start new DNA strand,
        # if no (n), show analysis
        print("Create new DNA Strand? (y/n)")
        if (input() == "n"): return "nill"

        currentRead = " "
        while (currentRead != ""):
            print(currentStrand) # 3' to 5'
            print(currentStrand[::-1]) # 5' to 3'

            # read and add
            print("\nAdd Nucleobase,")
            currentRead = UI.getInput()
            currentStrand += currentRead
            UI.clearScreen()
        
        return currentStrand
    
    def analyse(sequences):
        for i in range(len(sequences)):
            # show sequences
            print("\n=====DNA Strand " + str(i) + "=====")
            print("3\' " + sequences[i] + " 5\'")
            print("5\' " + reverseString(sequences[i]) + " 3\'")