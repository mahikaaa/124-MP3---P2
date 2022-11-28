"""
    Pilpa, Myka Marie Jean L.        
    Machine Problem 3
    Problem #2
"""

"""
Second Problem Grammar:
<expr> ::= +<num> | -<num> | <num>
<num> ::= <digits><num> | .<digits> | <digit>
<digits> := <digit> | <digit><digits>
<digit> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 

"""


# Second Grammar Parser
class MultiDigitDecimalParser:
    def __init__(self):
        self.index = 0
        self.input = None
        self.token = None
        self.len = 0
        self.decimals = 0

    def Next(self):
        return Lex(self.input[self.index + 1])

    def digitInDecimalCount(self):
        for i in self.input:
            if i == ".":
                self.decimals +=1
    
    def Consume(self):
        if self.index < self.len:
            self.index += 1
            self.token = Lex(self.input[self.index])

    def Digit(self):
        if self.token.getType() == "Number":
            self.Consume()
        else:
            self.index-=1  
            return

    def Digits(self):
        if self.token.getType() == "Number":
            self.Digit()
            self.Digits()
        
    def Number(self):
        if self.token.getType() == "Number" and self.Next().getValue() != "$":
            self.Consume()
            self.Digits()
            self.Number()
        elif self.token.getValue() == ".":
            self.Consume()
            if(self.token.getType() != "Number"):
                self.index-=1
            else:
                self.Digits()
        elif self.token.getType() == "Number" and self.Next().getValue() == "$":
            self.Digit()
        else:
            self.index-=1 

    def Expression(self):
        if self.token.getValue() == "+" or self.token.getValue() == "-":
            self.Consume()
        self.Number()


    def Parse(self):
        self.index = 0
        self.decimals = 0
        self.input = input("Input a string: ")
        self.input.replace(" ", "")
        self.len = len(self.input)
        self.digitInDecimalCount()
        if self.decimals > 1:
            print("\nInvalid input, please try again.")
            return
        else:
            self.token = Lex(self.input[self.index])
            if self.input[self.len-1] == '$':
                self.Expression()
                if self.index == self.len-1: 
                    print("\nValid Input")
                else:
                    print("\nInvalid Input")
            else:
                print("\nInvalid input, please try again.") 
                return


class Token:
    def __init__(self, token, value):
        self.__token = token
        self.__value = value

    # Getter functions
    def getType(self):
        return self.__token
    def getValue(self):
        return self.__value

    # For checking purposes
    def printToken(self):
        print(self.getType() + " : " + self.getValue())

def Lex(character):
    if character.isdigit() == True:
        newToken = Token("Number", character)
    elif character == "+" or character == "-" or character == "/" or character == "*":
        newToken = Token("Operation", character)
    elif character == "$":
        newToken = Token("Terminate", character)
    elif character == "(":
        newToken = Token("OpenParenthesis", character)
    elif character == ")":
        newToken = Token("ClosedParenthesis", character)
    elif character == ".":
        newToken = Token("Decimal", character)
    else:
        newToken = Token("Invalid", character)
    return newToken


#Test
MDP = MultiDigitDecimalParser()
MDP.Parse()
