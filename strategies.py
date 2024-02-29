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

def rebel(mymoves,opmoves): #uses the least popular move
    if(len(mymoves)==0): return "dove"
    hawk_count = 0

    for bird in opmoves:
        if(bird == "hawk"): 
            hawk_count += 1
    
    if(hawk_count > len(opmoves) / 2): return "dove"
    else: return "hawk"

def pushover(mymoves,opmoves): #always dove unless last 3 opponents moves were hawks
    for i in range(min(3,len(opmoves))):
        if(opmoves[len(opmoves)-1-i] == "dove"): return "dove"

    return "hawk"

def guardian(mymoves,opmoves): #always hawk unless last 3 opponents were dove
    for i in range(min(3,len(opmoves))):
        if(opmoves[len(opmoves)-1-i] == "hawk"): return "hawk"

    return "dove"     

def believer(my, op): #tiki praeitimi, renkasi ta move kuris anksciau geras jam buvo
    matrix = [[(5,5),(2,7)],[(7,2),(0,0)]]
    d={'dove':0,'hawk':1}
    if len(my)<10:
        return 'dove' if random.random()<0.5 else 'hawk'
    gains=[0,0]
    for i in zip(my,op):
        if d[i[0]]:
            gains[1]+=matrix[d[i[0]]][d[i[1]]][0]
        else:
            gains[0]+=matrix[d[i[0]]][d[i[1]]][0]
    if gains[1]>gains[0]:
        return 'hawk'
    else:
        return 'dove'

def alzheimer_conformist(mymoves,opmoves): #uses the most popular move in the last five moves
    if(len(mymoves)==0): return "dove"
    hawk_count = 0

    if(len(opmoves)>5):
        for i in range(1, 6):
            if(opmoves[len(opmoves)-i] == "hawk"):
                hawk_count += 1

    if(hawk_count >= 3): return "hawk"
    else: return "dove"
