from fun import *
from ui import *
from strand import *

class DNAMapper:
    def __init__(self):
        DNAMapper.main()
    
    def main():
        strandsCollection = []
        sequnceTypes = []

        while (True):

            currentStrand, isRNA = Strand.create()

            if (currentStrand == "nill"):
                # get final analysis
                Strand.analyse(strandsCollection, sequnceTypes)

                # let the user pause and read analysis
                UI.pause()
                exit()
            else:
                # add to total collection of DNA strands
                strandsCollection.append(currentStrand)
                sequnceTypes.append(isRNA)

# call main class function
DNAMapper()