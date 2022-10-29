import os

class UI:
    def getInput():
        # get input and convert to capitial
        return str(input()).upper()

    def clearScreen():
        os.system("cls")
        os.system("clear")
    
    def pause():
        input()
