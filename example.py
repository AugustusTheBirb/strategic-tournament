import sys
import game
from strategies import detStrat, randStrat
import time


def test(player,
         length):  # added test function, so you can see how a strategy performs against all possible games of length
    # k,for testing purposes
    # this does print out 3*2**len lines so id advise against setting length to more than 6
    a = [bin(x)[2:].zfill(length) for x in range(2 ** length)]
    b = []
    reward_matrix = [[(5, 5), (2, 7)], [(7, 2), (0, 0)]]
    d = {'dove': 0, 'hawk': 1}

    for i in a:
        b.append(list(game.convback(int(j)) for j in i))
    for gameBoard in b:
        moves = []
        points = 0
        for i in range(length):
            points += reward_matrix[d[player(moves, gameBoard[0:i])]][d[gameBoard[i]]][0]
            moves.append(player(moves, gameBoard[0:i]))
        print(gameBoard)
        print(moves, end=" ")
        print(points)
        print(" ")


def __main__():
    time_start = time.time()
    rands = ["$" + attribute for attribute in dir(randStrat) if callable(getattr(randStrat, attribute))
             and attribute.startswith('__') is False]
    players = [attribute for attribute in dir(detStrat) if callable(getattr(detStrat, attribute))
               and attribute.startswith('__') is False] + rands

    # add the strategies you want to play in the tournament to this list, top one runs every single method
    # players = [strat.allDove, strat.allHawk, strat.rando, strat.copycat, strat.conformist, strat.critic, strat.rebel,
    #                strat.pushover, strat.predator, strat.alzheimer_conformist, strat.believer,
    #                strat.grudge, strat.tit_for_tattat, strat.prod, strat.intrusive_thought
    #                ]
    print(players)

    rounds = 100  # numbers of rounds in one game
    retries = 100  # the retries are so that non-deterministic strategies' payoffs get averaged out
    matrix = [[(5, 5), (2, 7)],
              [(7, 2), (0, 0)]]

    for argument in sys.argv:
        if str(argument) in ["-v","-verbose"]:
            console = True
        else:
            console = False

    game.full_game(players, rounds, retries, matrix, console)
    if console:
        print(time.time() - time_start, "seconds")


__main__()