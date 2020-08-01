from ui import *
from fun import *

class Strand:
    def create():
        currentStrand = ""
        
        # TRUE = RNA composition
        # FALSE = DNA composition
        # assumption is it is DNA
        RNA = "unknown"

        # conformation to start new DNA strand,
        # if no (n), show analysis
        print("Create new DNA Strand? (y/n)")
        if (input() == "n"): return "nill", False

        currentRead = " "
        while (currentRead != ""):
            # read and add
            print("\nAdd Nucleobase,")
            currentRead = UI.getInput()

            # check if it's DNA or RNA
            if ("T" in currentRead and RNA == "unknown"):
                RNA = False
            elif ("U" in currentRead and RNA == "unknown"):
                RNA = True

            # confirm it's a possible base
            # append if it is a possible base
            if (checkNucleobase(currentRead, RNA)):
                currentStrand += currentRead

            # UI output
            UI.clearScreen()
            print(currentStrand) # 3' to 5'

            # don't print out corrosponding double helix strand if RNA
            if (not RNA or RNA == "unknown"):
                print(currentStrand[::-1]) # 5' to 3'
        
        # RETURN

        # assume strand is DNA
        if (RNA == "unknown"): RNA = False
        return currentStrand, RNA
    
    def analyse(sequences, isRNA):
        for i in range(len(sequences)):
            # show sequences
            print("\n=====DNA Strand " + str(i) + "=====")
            print("3\' " + sequences[i] + " 5\'")

            # only print out if DNA
            if (not isRNA[i]):
                print("5\' " + reverseString(sequences[i]) + " 3\'")
            print

            # compare to others
            for comparisonI in range(len(sequences)):
                if (comparisonI == i): continue
                similarity = similar(sequences[i], sequences[comparisonI]) * 100
                print(str(similarity) + " percent similar to DNA Strand: " + str(comparisonI))