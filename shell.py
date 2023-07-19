import os

__version__ = "1.0"

QUIT = ["QUIT", "quit", "EXIT", "exit"]

def sh():

    print("The G Programming Language")

    prompt = "\n╭──(v." + __version__ + ")\n│\n╰──🞂 "

    while True:
        comm = input(prompt)
        if comm in QUIT:
            quit()
        else:
            os.system("echo " + comm + " > shell.g")
            os.system("py g.py shell.g")
            os.system("echo . > shell.g")