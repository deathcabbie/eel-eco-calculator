import eel

eel.init(".")

score = 0

@eel.expose
def calculator(recycle):
    global score
    if recycle == "lots":
        score += 3 
        return "Awesome!"
    elif recycle == "some":
        score += 2 
        return "Okay..."
    elif recycle == "none":
        score += 1 
        return "That's not good!"

@eel.expose
def calculatorT(travel):
    global score
    if travel == "car":
        score += 1
        return "That's not good!"
    elif travel == "bus":
        score += 2
        return "Okay..."
    elif travel == "bike":
        score += 3 
        return "Awesome!"

@eel.expose
def calculatorM(meat):
    global score
    if meat == "always":
        score += 1
        return "That's not good!"
    elif meat == "sometimes":
        score += 2
        return "Okay..."
    elif meat == "never":
        score += 3 
        return "Awesome!"

@eel.expose
def outcome():
    global score
    if score >= 7:
        return "You are having a minimal impact on the environment."
    elif score <=3:
        return "You are having a terrible impact on the environment."
    else:
        return "You are having an average impact on the environment."

eel.start("landing.html")

