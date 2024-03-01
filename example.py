import game
import strategies as str


def test(player,
         length):  # added test function so you can see how a strategy performs against all possible games of length
    # k,for testing purposes
    # this does print out 3*2**len lines so id advise against setting length to more than 6
    a = [bin(x)[2:].zfill(length) for x in range(2 ** length)]
    b = []
    matrix = [[(5, 5), (2, 7)], [(7, 2), (0, 0)]]
    d = {'dove': 0, 'hawk': 1}

    for i in a:
        b.append(list(game.convback(int(j)) for j in i))
    for game in b:
        mymoves = []
        mypoints = 0
        for i in range(length):
            mypoints += matrix[d[player(mymoves, game[0:i])]][d[game[i]]][0]
            mymoves.append(player(mymoves, game[0:i]))
        print(game)
        print(mymoves, end=" ")
        print(mypoints)
        print(" ")


players = [str.allDove, str.allHawk, str.rando, str.copycat, str.conformist, str.critic, str.rebel,
           str.pushover, str.predator, str.alzheimer_conformist, str.believer,
           str.grudge, str.tit_for_tattat, str.prod
           ]  # add the strategies you want to play in the tournament to this list

rounds = 100  # numbers of rounds in one game
retries = 100  # the retries are so that non-deterministic strategies's payoffs get averaged out
matrix = [[(5, 5), (2, 7)],
          [(7, 2), (0, 0)]]

game.full_game(players, rounds, retries, matrix)
