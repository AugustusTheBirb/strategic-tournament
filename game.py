def conv(str):
    if(str =="dove"): return 0
    else: return 1

def convback(bit):
    if bit==0: return "dove"
    else: return "hawk"

def game(rounds,player1,player2,matrix): #runs one game of two specific players with a set number of rounds
    moves1 = []
    moves2 = []
    score1 = 0
    score2 = 0
    for i in range(rounds):
        choice1 = player1(moves1,moves2)
        choice2 = player2(moves2,moves1)
        score1 += matrix[conv(choice2)][conv(choice1)][1]
        score2 += matrix[conv(choice2)][conv(choice1)][0]
        moves1.append(choice1)
        moves2.append(choice2)
    return (score1, score2) 

def full_game(players,rounds,retries,matrix): #runs whole tourney
    length = len(players)
    scores = [ 0 ]*length
    table = [[0 for i in range(length)] for j in range(length)]
    # for i in range(length):
    #     table[i][i] = "O"
    for i in range(length):
        for j in range(i,length):
            s1 = 0
            s2 = 0
            for times in range(retries):
                 s = game(rounds, players[i], players[j],matrix)
                 s1 += s[0]
                 s2 += s[1]
            scores[i] += s1/retries
            if(i!=j):scores[j] += s2/retries
            table[i][j] = (s1/retries, f'{players[i].__name__} vs {players[j].__name__}')
            table[j][i] = (s2/retries, f'{players[j].__name__} vs {players[i].__name__}')
    scores = list(a/(length) for a in scores)
    final = []
    for p in range(length):
        final.append((players[p].__name__,round(scores[p],2)))
    final.sort(key=lambda a: a[1],reverse=True)
    for i in range(length):
        print(f'{final[i][0]} earned {final[i][1]}')
    for j in table:
        print(j) 
