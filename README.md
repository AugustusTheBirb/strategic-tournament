# Strategic Tournament

If you want to contribute to this project create a branch and then create a pull request.

A simple program for running tournaments of different agents for 2 player non-sequential strategic games with finite actions.
The game setup here is Hawk-Dove, in it the players receive payoffs according to the following payoff matrix:

|                | Dove | Hawk |
| -------------- | ---- | ---- |
| **Dove** | 5;5  | 2;7  |
| **Hawk** | 7;2  | 0;0  |

## INTRO - what is this game

Where the number pairs show the payoffs for each action pair (left player, top player) - the amount of "coins" your strategy gains for that outcome.

The games are simultaneous - both strategies make the choice between the two actions at the same time>T, with their only knowledge being their previous history with each other.

The idea behind this game is that two animals are competing over some shared resource, and they have two options - fight or share (act like a hawk or like a dove).
If they both chose to fight, the cost of the resulting fight is greater than the value of the resource, if one fights and one shares, the one who shares will end up getting a smaller share of the resource, a lower payoff.
If they both share they’ll get an equal share of the resource.

|                | Hawk            | Dove    |
| -------------- | --------------- | ------- |
| **Hawk** | (V-C)/2;(V-C)/2 | V;0     |
| **Dove** | 0;V             | V/2;V/2 |

Its easier to understand the game from this matrix (which is equivalent in preferences to the one we use in this tournament just shifted a bit so that the values are positive), V is the value of the resource, C is the cost of a fight, C>V>0

## THE TOURNAMENT

I have made a little tournament program for this game, which you can see at the very bottom in its entirety. The tournament will work like this: it will consist of as many players as you create each playing each other for 100+-10 rounds (this will be a constant value throughout the tournament), and in each of those ~100 rounds they will earn "coins" according to the payoff matrix at the top. Each player's final score will be the sum of all of their scores (including against themselves!) /number of players - so their average score.

This does mean that there is no "objectively best" strategy, because your payoff depends on the strategies you're up against. (probably)

## STRATEGIES

I have already added 3 simple strategies and one more complex one that my brother submitted, so that testing your strategies is easier if you wish to do so.

If you know how to write python code, then the function should be in this format:

```python
def stratey_name(mymoves,opmoves):
    #logic
    return choice
```

For example, heres a strategy that outputs 50/50 hawk dove

```python
def randeris(mymoves,opmoves): #50/50 hawk/dove
    a = random.random() #returns a number 0>a>1
    if a>0.5:return "dove"
    else: return "hawk"
```

Mymoves and opmoves are lists of previous moves, they contain the words “dove” and “hawk”
On the first move both are empty.

> [!NOTE]
> If you don't know how to implement your strategy, you can describe it in text and send it to me, I’ll implement it to the best of my ability.

### STRATEGIES CREATED SO FAR

***Deterministic Algorithms***

- **allDove** - allways chooses dove
- **allHawk** - allways chooses hawk
- **copycat** - copies opponents last move
- **critic** - chooses opposite of opponents last move
- **conformist** - chooses the move that is the most frequently played by the opponent
- **rebel** - chooses the move that is the least frequently played by the opponent
- **pushover** - chooses hawk unless the last three moves of the opponent were hawk
- **predator** - chooses dove unless the last three moves of the opponent were dove
- **alzheimer_conformist** - chooses the move that is the most popular among the opponents last five moves
- **sore loser** - if it has fewer points its opponent it goes hawk, else dove
- **grudge** - plays dove until the opponent plays hawk and then plays only hawk
- **tit-for-tattat** - plays hawk if and only if the opponent played hawk for the last two turns
- **prod** - play hawk, if no hawks play hawk every third turn else tit-for-tat
- **smartHawk** - play hawk, if in the first 10 moves the opponent plays >7 hawks, becomes all dove, else stays all hawk
- **dumbBird** - a dumb bird, if the opponent chooses hawk >7 times in the first 10 moves, he becomes all hawk, else stays all dove
- **reverse-grudge** - plays hawk until the oponnent plays a dove then keeps playing dove
- **alternate** - alternates between dove and hawk

***Non-Deterministic Algorithms***
- **rando** - randomly chooses hawk/dove with 50/50 odds
- **believer** - chooses the move that has historically yielded the most points
- **intrusive thought** - will play tit-for-tat but randomly lash out if the enemy is too nice

## BASIC USAGE

To initiate the tournament run the example.py. The python script will generate an Excel file called `results.xlsx`. In this file you will be able to find the average scores of all the strategies and scores of all the strategy match ups.

example.py accepts these arguments:

-v verbose mode (will output the runtime and average scores of strategies)
