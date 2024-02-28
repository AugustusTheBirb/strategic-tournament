import random

def rando(mymoves,opmoves): #50/50 hawk/dove
    a = random.random()
    if a>0.5:return "dove"
    else: return "hawk"

def allDove(mymoves,opmoves): #always dove
    return "dove"

def allHawk(mymoves,opmoves): #always hawk
    return "hawk"

def copycat(mymoves,opmoves): #copies opponents last move
    if (len(mymoves)==0): return "dove"
    if (opmoves[len(opmoves)-1]=="hawk"): return "hawk"
    else: return "dove"

def conformist(mymoves,opmoves): #uses the most popular move
    if(len(mymoves)==0): return "dove"
    hawk_count = 0

    for bird in opmoves:
        if(bird == "hawk"): 
            hawk_count += 1
    
    if(hawk_count > len(opmoves) / 2): return "hawk"
    else: return "dove"

def critic(mymoves,opmoves): #reverses opponents last move
    if (len(mymoves)==0): return "dove"
    if (opmoves[len(opmoves)-1]=="hawk"): return "dove"
    else: return "hawk"

def rebel(mymoves,opmoves): #uses the most popular move
    if(len(mymoves)==0): return "dove"
    hawk_count = 0

    for bird in opmoves:
        if(bird == "hawk"): 
            hawk_count += 1
    
    if(hawk_count > len(opmoves) / 2): return "dove"
    else: return "hawk"