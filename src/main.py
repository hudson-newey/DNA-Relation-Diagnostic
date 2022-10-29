import sys

from fun import *
from ui import *
from strand import *

class DNAMapper:
    def __init__(self):
        if len(sys.argv) > 1:
            DNAMapper.main_file()
        else:
            DNAMapper.main()
    
    def main_file():
        sequenceTypes = []
        strandsCollection = []

        fileName = sys.argv[1]
        
        with open(fileName, 'r') as f:
            for line in f:
                adjustedLine = line.rstrip()
                strandsCollection.append(str(adjustedLine))
                sequenceTypes.append(False)
        
        Strand.analyse(strandsCollection, sequenceTypes)

    
    def main():
        strandsCollection = []
        sequenceTypes = []

        while (True):

            currentStrand, isRNA = Strand.create()

            if (currentStrand == "nill"):
                # get final analysis
                Strand.analyse(strandsCollection, sequenceTypes)

                # let the user pause and read analysis
                UI.pause()
                exit()
            else:
                # add to total collection of DNA strands
                strandsCollection.append(currentStrand)
                sequenceTypes.append(isRNA)

# call main class function
DNAMapper()
