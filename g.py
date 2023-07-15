# TOKEN CONSTANTS

TT_PRINT = ["PRINT", "print"]
DIGITS = "0123456789"

from sys import argv

def open_file(filename):
    data = open(filename, "r").read()
    return data

def lex(filecontent):
    tok = ""
    expr_started = 0 # 0 --> Not in a number | 1 --> In a number
    state = 0 # 0 -- > Not in a string | 1 --> In a string
    string = ""
    tokens = []
    filecontent = list(filecontent)
    for char in filecontent:
        tok += char
        if tok in " \n" and state == 0: 
            tok = ""
        elif tok in TT_PRINT:
            tokens.append("PRINT")
            tok = ""
        elif tok in DIGITS:  
            expr_started = 1
            tok = ""
        elif tok == "\"":
            if state == 0:
                state = 1
            elif state == 1:
                tokens.append("STRING:" + string + "\"")
                string = ""
                state = 0
                tok = ""
        elif state == 1:
            string += tok
            tok = ""
    return tokens
    #print(tokens)

def parse(toks):
    i = 0
    while (i < len(toks)):
        if toks[i] + " " + toks[i+1][0:6] == "PRINT STRING":
            #print(toks[i+1][8:len(toks[i+1])-1])
            print(toks[i+1][7:])
            i+=2

def run():
    data = open_file(argv[1])
    toks = lex(data)
    parse(toks)

run()