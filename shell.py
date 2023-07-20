import os



QUIT = ["QUIT", "quit", "EXIT", "exit", "END", "end"]

def sh(): 
    import g
    print("The G Programming Language")
    prompt = "\n╭──(v." + g.__version__ + ")\n│\n╰──🞂 "

    while True:
        
        comm = input(prompt)
        
        if comm in QUIT:
            quit()
        else:
            sh_toks = g.lex(comm)
            g.parse(sh_toks)