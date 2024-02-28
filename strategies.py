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
