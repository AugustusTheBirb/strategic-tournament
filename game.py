from openpyxl import Workbook


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
        choice1 = player1(moves1, moves2)
        choice2 = player2(moves2, moves1)
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
        ws.cell(row=2, column=i + 2).value = players[i].__name__
        ws.cell(row=i + 3, column=1).value = players[i].__name__

    for i in range(length):
        for j in range(i, length):
            s1 = 0
            s2 = 0
            for times in range(retries):
                s = game(rounds, players[i], players[j], matrix)
                s1 += s[0]
                s2 += s[1]
            score1 = s1 / (retries * rounds)
            score2 = s2 / (retries * rounds)
            scores[i] += score1
            if i != j:
                scores[j] += score2
            table[i][j] = (score1, f'{players[i].__name__} vs {players[j].__name__}')
            ws.cell(row=j + 3, column=i + 2).value = score1
            table[j][i] = (score2, f'{players[j].__name__} vs {players[i].__name__}')
            ws.cell(row=i + 3, column=j + 2).value = score2

    scores = list(a / length for a in scores)
    final = []

    for p in range(length):
        final.append((players[p].__name__, round(scores[p], 5)))
    for i in range(length):
        ws.cell(row=1, column=i + 2).value = final[i][1]

    final.sort(key=lambda a: a[1], reverse=True)

    for i in range(length):
        print(f'{final[i][0]} earned {final[i][1]} per round')
    for j in table:
        print(j)

    wb.save("results.xlsx")
