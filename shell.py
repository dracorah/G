#########
# SHELL #
#########

import g

while True:
    text = input("G >>> ")
    result, error = g.run(text)

    if error: print(error.as_string())
    else: print(result)