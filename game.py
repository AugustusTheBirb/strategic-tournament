from openpyxl import Workbook
from strategies import detStrat,randStrat


def conv(choice):
    if choice == "dove":
        return 0
    else:
        return 1


def convback(bit):
    if bit == 0:
        return "dove"
    else:
        return "hawk"


def game(rounds, player1, player2, matrix):  # runs one game of two specific players with a set number of rounds
    moves1 = []
    moves2 = []
    scores = [0, 0]
    for i in range(rounds):
        if player1[0] == "$":
            choice1 = getattr(randStrat, player1[1:])(randStrat, moves1, moves2)
        else:
            choice1 = getattr(detStrat, player1)(detStrat, moves1, moves2)

        if player2[0] == "$":
            choice2 = getattr(randStrat, player2[1:])(randStrat, moves1, moves2)
        else:
            choice2 = getattr(detStrat, player2)(detStrat, moves1, moves2)
        scores[0] += matrix[conv(choice2)][conv(choice1)][1]
        scores[1] += matrix[conv(choice2)][conv(choice1)][0]
        moves1.append(choice1)
        moves2.append(choice2)
    return scores


def full_game(players, rounds, retries, matrix):  # runs whole tourney
    length = len(players)
    scores = [0] * length
    table = [[0 for i in range(length)] for j in range(length)]

    # Initiating excel sheet
    wb = Workbook()
    ws = wb.active
    ws.cell(row=1, column=1).value = "Average"
    for i in range(length):
        ws.cell(row=2, column=i + 2).value = players[i]
        ws.cell(row=i + 3, column=1).value = players[i]

    for i in range(length):
        for j in range(i, length):
            s1 = 0
            s2 = 0
            rand = False
            player1, player2 = players[i],players[j]
            if player1[0] == "$":
                rand = True
                player1 = player1[1:]
            if player2[0] == "$":
                rand = True
                player2 = player2[1:]
            if rand:
                for times in range(retries):
                    s = game(rounds, players[i], players[j], matrix)
                    s1 += s[0]
                    s2 += s[1]
            else:
                s = game(rounds, players[i], players[j], matrix)
                s1 += s[0]
                s2 += s[1]
            score1 = s1 / (retries * rounds)
            score2 = s2 / (retries * rounds)
            scores[i] += score1
            if i != j:
                scores[j] += score2
            table[i][j] = (score1, f'{player1} vs {player2}')
            ws.cell(row=j + 3, column=i + 2).value = score1
            table[j][i] = (score2, f'{player1} vs {player2}')
            ws.cell(row=i + 3, column=j + 2).value = score2

    scores = list(a / length for a in scores)
    final = []

    for p in range(length):
        final.append((players[p], round(scores[p], 5)))
    for i in range(length):
        ws.cell(row=1, column=i + 2).value = final[i][1]

    final.sort(key=lambda a: a[1], reverse=True)

    for i in range(length):
        print(f'{final[i][0]} earned {final[i][1]} per round')
    for j in table:
        print(j)

    wb.save("results.xlsx")
