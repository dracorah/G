import clear
import shell

__version__ = "0.0"

# TOKEN CONSTANTS

TT_PRINT = ["PRINT", "print"]
TT_PRINTSTR = ["STR_PRINT", "str_print"]
TT_QUIT = ["QUIT", "quit", "EXIT", "exit"]
TT_CLEAR = ["CLEAR", "clear"]
DIGITS = list("0123456789.")
MATH_CHARS = list("+-/*()%")

from sys import argv

def open_file(filename):
    data = open(filename, "r").read()
    data += "<EOF>"
    return data

def lex(filecontent):
    tok = ""
    expr_started = 0 # 0 --> Not in a number | 1 --> In a number
    expr = ""
    isexpr = 0
    state = 0 # 0 -- > Not in a string | 1 --> In a string
    string = ""
    tokens = []
    filecontent = list(filecontent)
    for char in filecontent:
        tok += char
        if tok in " " and state == 0: 
            tok = ""
        if tok == "\n" and state == 0 or tok == "<EOF>" and state == 0: 
            if expr != "" and isexpr == 1:
                tokens.append("EXPR:" + expr)
                #print(expr + "EXPR")
                isexpr = 0
                expr = ""
            elif expr != "" and isexpr == 0:
                tokens.append("NUM:" + expr)
                #print(expr + "NUM")
                isexpr = 0
                expr = ""
            tok = ""
        elif tok in TT_PRINTSTR:
            tokens.append("PRINT_STR")
            tok = ""
        elif tok in TT_PRINT:
            tokens.append("PRINT")
            tok = ""
        elif tok in TT_QUIT:
            tokens.append("QUIT")
            tok = ""
        elif tok in TT_CLEAR:
            tokens.append("CLEAR")
            tok = ""
        elif tok in DIGITS :  
            expr_started = 1
            expr += tok
            tok = ""
        elif tok in MATH_CHARS:
            expr += tok
            isexpr = 1
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
    print(tokens)
    return tokens

def parse(toks):
    i = 0
    while (i < len(toks)):
        
        if toks[i] == "QUIT":
            break
            quit()
        
        elif toks[i] == "CLEAR":
            clear.clear()
        
        elif toks[i].startswith("NUM") or toks[i].startswith("EXPR"):
            i += 1

        else:
        
            try:
                
                
                if toks[i] + " " + toks[i+1][0:6] == "PRINT STRING":
                    print(toks[i+1][8:len(toks[i+1])-1])
                    #print(toks[i+1][7:])
                    i+=2

                elif toks[i] + " " + toks[i+1][0:3] == "PRINT NUM":
                    print(eval(toks[i+1][4:]))
                    i+=2
                
                elif toks[i] + " " + toks[i+1][0:4] == "PRINT EXPR":
                    print(eval(toks[i+1][5:]))
                    i+=2
                
                elif toks[i] + " " + toks[i+1][0:3] == "PRINT_STR NUM":
                    print(toks[i+1][4:])
                    i+=2
                
                elif toks[i] + " " + toks[i+1][0:4] == "PRINT_STR EXPR":
                    print(toks[i+1][5:])
                    i+=2
                
                elif toks[i] + " " + toks[i+1][0:6] == "PRINT_STR STRING":
                    print(toks[i+1][8:len(toks[i+1])-1])
                    #print(toks[i+1][7:])
                    i+=2
                else:
                    if toks[i][0:6] == "STRING":
                        print("AloneSTRError")
                        break
                        i+=1

            except IndexError:
                pass

def run():

    try:
        data = open_file(argv[1])
    except IndexError:
        shell.sh()

    toks = lex(data)
    parse(toks)

run()