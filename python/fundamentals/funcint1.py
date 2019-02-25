import random
def randInt(min='', max=''):
    a = random.random() * ((randInt(max='')) - (randInt(min='')) + (randInt(min=''))
    b = random.random() * (100 - (randInt(min='')) + (randInt(min=''))
    c = random.random() * (randInt(max=''))
    d = random.random()
    if randInt(min='', max=''):
        return a
    elif randInt(min=''):
        return b
    elif randInt(max=''):
        return c
    elif randInt():
        return d
#print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500