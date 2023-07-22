import os



QUIT = ["QUIT", "quit", "EXIT", "exit", "END", "end"]

def sh(): 
    import g as g
    print("The G Programming Language")
    prompt = "\n╭──(v." + g.__version__ + ")\n│\n╰──🞂 "

    while True:
        
        comm = input(prompt)
        
        if comm in QUIT:
            quit()
        else:
            sh_toks = g.lex(comm)
            sh_toks.append("QUIT")
            g.parse(sh_toks)