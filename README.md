# Strategic Tournament
A simple program for running tournaments of different agents for 2 player non-sequential strategic games with finite actions.
The game setup here is Hawk-Dove, in it the players receive payoffs according to the following payoff matrix:
|  | Dove | Hawk |
| --- | --- | --- |
| **Dove** | 5;5 | 2;7 |
| **Hawk** | 7;2 | 0;0 

## INTRO - what is this game 
Where the number pairs show the payoffs for each action pair (left player, top player) - the amount of "coins" your strategy gains for that outcome.

The games are simultaneous - both strategies make the choice between the two actions at the same time>T, with their only knowledge being their previous history with eachother.

The idea behind this game is that two animals are competing over some shared resource, and they have two options - fight or share (act like a hawk or like a dove).
If they both chose to fight, the cost of the resulting fight is greater than the value of the resource, if one fights and one shares, the one who shares will end up getting a smaller share of the resource, a lower payoff. 
If they both share they’ll get an equal share of the resource.

|  | Hawk | Dove |
| --- | --- | --- |
| **Hawk** | (V-C)/2;(V-C)/2 | V;0 |
| **Dove** | 0;V | V/2;V/2 |

Its easier to understand the game from this matrix (which is equivalent in preferences to the one we use in this tournament just shifted a bit so that the values are positive), V is the value of the resource, C is the cost of a fight, C>V>0

## THE TOURNAMENT

I have made a little tournament program for this game, which you can see at the very bottom in its entirety. The tournament will work like this: it will consist of as many players as you create each playing each other for 100+-10 rounds (this will be a constant value throughout the tournament), and in each of those ~100 rounds they will earn "coins" according to the payoff matrix at the top. Each players final score will be the sum of all of their scores (including against themselves!) /number of players - so their average score. 

This does mean that there is no objectively best strategy, because your payoff depends on the strategies you're up against. (probably)

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

If you want to contribute to my project create a branch and then create a pull request.

