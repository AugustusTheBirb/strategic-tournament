import random
from game import game
import time
from strategies import randStrat, detStrat
import matplotlib

matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import numpy as np


# todo: maybe optimise?
class Bird:
    def __init__(self, strategy, generation=0, children_made=0):
        self.points = 0
        self.strategy = strategy
        self.generation = generation
        self.children_made = children_made
        self.isalive = True

    def dumpAll(self):
        print(f"points {self.points}")
        print(f"strat {self.strategy}")
        print(f"generation {self.generation}")
        print(f"children {self.children_made}")
        print(f"isalive {self.isalive}")


class Evolution:
    def __init__(self, starting_populations, strategies, matrix, rounds, retries):
        self.population = [Bird(i) for i in strategies for j in range(starting_populations)]
        self.rounds = rounds
        self.retries = retries
        self.matrix = matrix
        self.strategies = strategies
        self.hashtable = self.compute_deterministic_hashes(rounds, matrix)

    def getData(self):
        data = {}
        for bird in self.population:
            if bird.strategy in data:
                data[bird.strategy] += 1
            else:
                data[bird.strategy] = 1
        for strat in self.strategies:
            if strat not in data:
                data[strat] = 0
        return data

    def compute_deterministic_hashes(self, rounds, matrix):
        # this is assuming that all players going in are deterministic
        hashtable = {}
        players = [i for i in self.strategies if i[0] != "$"]
        length = len(players)
        for i in range(length):
            for j in range(i, length):
                s = game(rounds, players[i], players[j], matrix)  # todo: rewrite this using a faster game
                hashtable[players[i] + players[j]] = s[0] / rounds
                hashtable[players[j] + players[i]] = s[1] / rounds
        return hashtable

    def tick(self):
        for bird in self.population:
            if random.random() < bird.points / 5:
                self.population.append(Bird(bird.strategy, bird.generation + 1))
                bird.children_made += 1
            if random.random() < 1 - bird.points / 5:
                bird.isalive = False
            bird.points = 0

    def cull(self):
        self.population = list(filter(lambda a: a.isalive, self.population))

    def playRound(self):
        random.shuffle(self.population)
        groups = zip(*[iter(self.population)] * 2)
        for bird1, bird2 in groups:
            if bird1.strategy[0] != "$" and bird2.strategy[0] != "$":
                bird1.points = self.hashtable[bird1.strategy + bird2.strategy]
                bird2.points = self.hashtable[bird2.strategy + bird1.strategy]
            else:
                s1 = 0
                s2 = 0
                for times in range(self.retries):
                    s = game(self.rounds, bird1.strategy, bird2.strategy, self.matrix)
                    s1 += s[0] / (self.retries * self.rounds)
                    s2 += s[1] / (self.retries * self.rounds)
                    bird1.points, bird2.points = s1, s2
        self.tick()
        self.cull()
        return self.getData()


# todo: this actually lies to you and mixes the data up. when i append all the data lits to allData the order is
#  actually the order that it comes in. I need to both figure out a cleaner way to display this graph and also stop
#  lying.
def __main__():
    time_start = time.time()
    rands = ["$" + attribute for attribute in dir(randStrat) if callable(getattr(randStrat, attribute))
             and attribute.startswith('__') is False]
    players = [attribute for attribute in dir(detStrat) if callable(getattr(detStrat, attribute))
               and attribute.startswith('__') is False] + rands
    matrix = [[(5, 5), (2, 7)],
              [(7, 2), (0, 0)]]

    rounds = 100

    evo_game = Evolution(10, players, matrix, rounds, 100)
    allData = []
    x = np.arange(0, len(players))
    for i in range(rounds):
        evo_game.playRound()
        roundData = evo_game.playRound()
        print(roundData)
        for j in x:
            allData.append(list(roundData.values()))
    np.array(allData).transpose()
    y = np.vstack(allData)

    fig, ax = plt.subplots()

    polys = ax.stackplot(x, y)
    legendProxies = []
    for poly in polys:
        legendProxies.append(plt.Rectangle((0, 0), 1, 1, fc=poly.get_facecolor()[0]))

    plt.legend(legendProxies, list(roundData.keys()))

    ax.set(xlim=(0, rounds / 2), xticks=np.arange(0, rounds / 2, 10),
           ylim=(0, 400), yticks=np.arange(0, 400, 100))
    plt.show()


__main__()
