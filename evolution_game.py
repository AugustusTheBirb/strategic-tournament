import random
from game import game
import time
from strategies import randStrat, detStrat
from matplotlib import pyplot as plt

# todo: get plotting
# todo: figure out why the randoms really dont want to die
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
            if bird.strategy in data.keys():
                data[bird.strategy] += 1
            else:
                data[bird.strategy] = 1
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
            if random.random() < bird.points / 7:
                self.population.append(Bird(bird.strategy, bird.generation + 1))
                bird.children_made += 1
            if random.random() < 1 - bird.points / 7:
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
                    s1 += s[0]/self.retries
                    s2 += s[1]/self.retries
                    bird1.points, bird2.points = s1, s2

        print(self.getData())
        self.tick()
        self.cull()
        print(len(self.population))


def __main__():
    time_start = time.time()
    rands = ["$" + attribute for attribute in dir(randStrat) if callable(getattr(randStrat, attribute))
             and attribute.startswith('__') is False]
    players = [attribute for attribute in dir(detStrat) if callable(getattr(detStrat, attribute))
               and attribute.startswith('__') is False] + rands
    matrix = [[(5, 5), (2, 7)],
              [(7, 2), (0, 0)]]

    evo_game = Evolution(100, players, matrix, 100, 100)
    print(evo_game.hashtable)
    for i in range(100):
        evo_game.playRound()


__main__()
