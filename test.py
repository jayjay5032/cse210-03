cLives = int(input("Lives: "))
cAGive = list(input("Answer: "))
guess = str
playing = True


tList = [" ___", "/___\\", "\\   /", " \\ /"]
nList = []
clist = []
cAns = cAGive.copy()

for i in range(len(cAns)):
    cAns[i] = "_ "

while playing == True:

    nList = []

    guess = str(input("Guess: "))

    if guess in cAGive:
        for i, elem in enumerate(cAGive):
            if elem == guess:
                print(f"{guess} found at {i}")
                cAns[i] = f"{guess} "
            elif elem != "_ ":
                print(f"{guess} not found at {i}")
                
        elem = ""

    gLine = "".join(cAns)

    nList.append(gLine)

    nList.append("")

    if (cLives < 4):
        for i in tList[4 - cLives:]:
            nList.append(i)
    else:
        for i in range(4):
            nList.append(tList[i])

    
    if (cLives == 0):
        clist = ["  x", " /|\\", " / \\"]     
    else:
        clist = ["  o", " /|\\", " / \\"]  

    for i in clist:
        nList.append(i)

    nList.append("^^^^^^")

    for i in nList:
        print(i)

    pStatus = input("Keep playing? ")
    if pStatus == "n":
        playing = False