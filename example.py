import game
import strategies

players = [str.allDove,str.allHawk,str.rando,str.copycat,str.critic] #add the strategies you want to play in the tournament to this list

rounds = 100 #numbers of rounds in one game
retries = 100 #the retries are so that non-deterministic strategies's payoffs get averaged out
matrix  = [[(5,5),(2,7)],
          [(7,2),(0,0)]]

full_game(players,rounds,retries,matrix)
