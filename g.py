from sys import argv

def open_file(filename):
    data = open(filename, "r").read()
    return data

def lex(filecontent):
    tok = ""
    state = 0
    string = ""
    filecontent = list(filecontent)
    for char in filecontent:
        tok += char
        if tok == " ": tok = ""
        elif tok == "PRINT":
            print("FOUND A PRINT")
            tok = ""
        elif tok == "\"":
            if state == 0:
                state = 1
            elif state == 1:
                print("FOUNT STRING")
                string = ""
                state = 0
        elif state == 1:
            string += char
            tok = ""

def run():
    data = open_file(argv[1])
    lex(data)

run()