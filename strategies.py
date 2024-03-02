import random


# helper functions for making strategies easier to understand

def points(mymove, opmove):  # returns your score for a given interaction
    matrix = [[(5, 5), (2, 7)], [(7, 2), (0, 0)]]
    d = {'dove': 0, 'hawk': 1}
    return matrix[d[mymove]][d[opmove]][0]


def hawks_in_last_k_opmoves(opmoves, k):
    c = 0
    for i in opmoves[-k:]:
        if i == "hawk":
            c += 1
    return c


# strategies themselves
class randStrat:
    @staticmethod
    def rando(mymoves, opmoves):  # 50/50 hawk/dove | Augustas
        if random.random() > 0.5:
            return "dove"
        else:
            return "hawk"

    @staticmethod
    def believer(mymoves, opmoves):  # tiki praeitimi, renkasi ta move kuris anksciau geras jam buvo | Tomas
        matrix = [[(5, 5), (2, 7)], [(7, 2), (0, 0)]]
        d = {'dove': 0, 'hawk': 1}
        if len(mymoves) < 10:
            return 'dove' if random.random() < 0.5 else 'hawk'
        gains = [0, 0]
        c1 = 0
        c2 = 0
        if "dove" not in mymoves: return "dove"
        if "hawk" not in mymoves: return "hawk"
        for i in zip(mymoves, opmoves):
            if d[i[0]]:
                gains[1] += matrix[d[i[0]]][d[i[1]]][0]
                c1+=1
            else:
                gains[0] += matrix[d[i[0]]][d[i[1]]][0]
                c2+=1
        if(c1!=0 and c2!=0):
            if gains[1]/c1 > gains[0]/c2:
                return 'hawk'
            else:
                return 'dove'
    @staticmethod
    def intrusive_thought(mymoves,
                          opmoves):  # tit-for-tat but if it gets too quiet it will randomly punch | meow
        if len(mymoves) == 0:
            return "dove"
        if len(opmoves) > 3:
            if "hawk" not in opmoves[-2:] and random.random() < 0.2:
                return "hawk"
        return opmoves[-1]


class detStrat:
    @staticmethod
    def allDove(mymoves, opmoves):  # always dove | Augustas
        return "dove"

    @staticmethod
    def allHawk(mymoves, opmoves):  # always hawk | Augustas
        return "hawk"

    @staticmethod
    def copycat(mymoves, opmoves):  # copies opponents last move | Vasaris
        if len(mymoves) == 0:
            return "dove"
        return opmoves[-1]

    @staticmethod
    def conformist(mymoves, opmoves):  # uses the most popular move | Lukas
        if len(mymoves) == 0:
            return "dove"
        if hawks_in_last_k_opmoves(opmoves, len(opmoves)) > len(opmoves) / 2:
            return "hawk"
        else:
            return "dove"

    @staticmethod
    def critic(mymoves, opmoves):  # reverses opponents last move | Lukas
        if len(mymoves) == 0:
            return "dove"
        if opmoves[-1] == "hawk":
            return "dove"
        else:
            return "hawk"

    @staticmethod
    def rebel(mymoves, opmoves):  # uses the least popular move | Lukas
        if len(mymoves) == 0:
            return "dove"
        if hawks_in_last_k_opmoves(opmoves, len(opmoves)) > len(opmoves) / 2:
            return "dove"
        else:
            return "hawk"

    @staticmethod
    def pushover(mymoves, opmoves):
        if len(opmoves) < 3:
            return "hawk"
        if "dove" in opmoves[-3:]:
            return "hawk"
        return "dove"

    @staticmethod
    def predator(mymoves, opmoves):  # always dove unless last 3 opponents were doves | Lukas
        if len(opmoves) < 2:
            return "hawk"
        if "hawk" in opmoves[-3:]:
            return "dove"
        return "hawk"

    @staticmethod
    def alzheimer_conformist(mymoves,
                             opmoves):  # uses the most popular move in the last five moves | Mokslo gildija
        if len(opmoves) > 5:
            if hawks_in_last_k_opmoves(opmoves, 5) >= 3:
                return "hawk"
        return "dove"

    @staticmethod
    def sore_loser(mymoves, opmoves):  # if it has fewer points its opponent it goes hawk, else dove | Mykolas
        myscore = 0
        opscore = 0
        for i in range(len(mymoves)):
            myscore += points(mymoves[i], opmoves[i])
            opscore += points(opmoves[i], mymoves[i])
        if opscore > myscore:
            return "hawk"
        else:
            return "dove"

    @staticmethod
    def grudge(mymoves, opmoves):  # plays dove until the opponent plays a hawk then keeps playing hawk | meow
        if "hawk" in opmoves:
            return "hawk"
        return "dove"

    @staticmethod
    def reverse_grudge(mymoves, opmoves):  # plays dove until the opponent plays a dove then keeps playing hawk | meow
        if "dove" in opmoves[1:]:
            return "hawk"
        return "dove"

    @staticmethod
    def prod(mymoves, opmoves):  # play hawk, if no hawks play hawk every third turn else tit-for-tat | meow
        if len(mymoves) == 0:
            return "hawk"
        if len(mymoves) < 3:
            return "dove"
        assert len(opmoves) > 2  # yeah, fuck you im assertin
        if opmoves[-1] == "hawk":
            return "hawk"
        if "hawk" not in opmoves[:3] and len(mymoves) % 3 == 0:
            return "hawk"
        return "dove"

    @staticmethod
    def tit_for_tattat(mymoves, opmoves):  # smacks back if it gets smacked twice in a row | meow
        if len(opmoves) < 2:
            return "dove"
        if "dove" not in opmoves[-2:]:
            return "hawk"
        return "dove"

    @staticmethod
    def smartHawk(mymoves,
                  opmoves):  # a smart hawk, if the opponent chooses hawk >7 times in the first 10 moves, he becomes all dove, else stays all hawk | Vasaris
        if len(mymoves) < 10: return "hawk"
        count = 0
        for i in range(10):
            if opmoves[i] == "hawk":
                count += 1
        if count > 7:
            return "dove"
        return "hawk"

    @staticmethod
    def dumbBird(mymoves,
                  opmoves):  # a dumb bird, if the opponent chooses hawk >7 times in the first 10 moves, he becomes all hawk, else stays all dove | Vasaris
        if len(mymoves) < 10: return "hawk"
        count = 0
        for i in range(10):
            if opmoves[i] == "hawk":
                count += 1
        if count > 7:
            return "hawk"
        return "dove"


    @staticmethod
    def alternate(mymove, opmove):
        if len(mymove) % 2 == 0:
            return "hawk"
        return "dove"
    
    @staticmethod
    def beholder(mymoves,opmoves):
        teststrip = ['dove', 'dove', 'hawk', 'hawk', 'hawk', 'hawk', 'hawk', 'hawk', 'hawk', 'hawk', 'dove', 'dove']
        dict = {'dovedovedovedovedovedovedovedovedovedovedovedove': 'allDove',
        'hawkhawkhawkhawkhawkhawkhawkhawkhawkhawkhawkhawk': 'allHawk',
        'dovedovedovedovedovedovehawkhawkhawkhawkhawkhawk': 'alzheimer_conformist',
        'dovedovedovedovedovehawkhawkhawkhawkhawkhawkhawk': 'conformist',
        'dovedovedovehawkhawkhawkhawkhawkhawkhawkhawkdove': 'copycat',
        'dovehawkhawkdovedovedovedovedovedovedovedovehawk': 'critic',
        'dovedovedovehawkhawkhawkhawkhawkhawkhawkhawkhawk': 'grudge',
        'hawkhawkhawkdovedovedovedovedovedovedovedovedove': 'predator',
        'hawkdovedovehawkhawkhawkhawkhawkhawkhawkhawkdove': 'prod',
        'hawkhawkhawkhawkhawkdovedovedovedovedovedovehawk': 'pushover',
        'dovehawkhawkhawkhawkdovedovedovedovedovedovedove': 'rebel',
        'hawkhawkhawkhawkhawkhawkhawkhawkhawkhawkdovedove': 'smartHawk',
        'dovedovedovedovehawkhawkhawkhawkhawkhawkhawkdove': 'tit_for_tattat'}
        if(len(mymoves)<len(teststrip)):return teststrip[len(mymoves)]
        c = ""
        for i in opmoves[0:12]:
            c+=i
        if (dict.get(c,0)==0): return "hawk"
        o = getattr(detStrat, dict.get(c))
        if (o(opmoves,mymoves)=="hawk"):return"dove"
        if (o(opmoves,mymoves)=="dove"):return"hawk"
        
