class myClass:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input()

    def printString(self):
        print(self.string.upper())

string1 = myClass()
string1.getString()
string1.printString()
