import os

QUIT = ["QUIT", "quit", "EXIT", "exit"]

print("The G Programming Language")

while True:
    comm = input("\n>>> ")
    if comm in QUIT:
        break
    else:
        os.system("echo " + comm + " > shell.g")
        os.system("py g.py shell.g")
        os.system("echo . > shell.g")