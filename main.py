from fun import *
from ui import *
from strand import *

class DNAMapper:
    def __init__(self):
        print("DNA Mapper\n")
        DNAMapper.main()
    
    def main():
        strandsCollection = []

        while (True):
            currentStrand = Strand.create()
            if (currentStrand == "nill"):
                # get final analysis
                Strand.analyse(strandsCollection)

                # let the user pause and read analysis
                UI.pause()
                exit()
            else:
                # add to total collection of DNA strands
                strandsCollection.append(currentStrand)

# call main class function
DNAMapper()