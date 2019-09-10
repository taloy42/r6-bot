import random

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


# data
import json
json_file = open('PlayerGameData.json', 'r')
data = json.load(json_file)

avihay = data['avihay']
eliran = data['eliran']
evyatar = data['evyatar']
gadNtomer = data['gadNtomer']
shlomo = data['shlomo']

onlinemp = data['onlinemp']
story = data['story']
quickfun = data['quickfun']
shooters = data['shooters']
zombies = data['zombies']
topnotch = data['topnotch']
openworld = data['openworld']
mpforfun = data['mpforfun']

games = data['games']


def pickgame(players):
    players = list(players)

    if not players:
        return random.choice(games)
    elif players[0].lower().startswith('c'):
        category = players[1]
        players = players[2:]
        final = games
        for p in players:
            if p.startswith('a'):
                final = intersection(final, avihay)
            elif p.startswith('ev'):
                final = intersection(final, evyatar)
            elif p.startswith('el'):
                final = intersection(final, eliran)
            elif p.startswith('g') or p.startswith('to'):
                final = intersection(final, gadNtomer)
            elif p.startswith('s'):
                final = intersection(final, shlomo)
        if len(final) == 0:
            return 'no games matching settings'
        else:
            if category.startswith('on'):
                final = intersection(final, onlinemp)
            elif category.startswith('st'):
                final = intersection(final, story)
            elif category.startswith('q'):
                final = intersection(final, quickfun)
            elif category.startswith('sh'):
                final = intersection(final, shooters)
            elif category.startswith('z'):
                final = intersection(final, zombies)
            elif category.startswith('t'):
                final = intersection(final, topnotch)
            elif category.startswith('op'):
                final = intersection(final, openworld)
            elif category.startswith('m'):
                final = intersection(final, mpforfun)
        return random.choice(final)

    else:
        final = games
        for p in players:
            if p.startswith('a'):
                final = intersection(final, avihay)
            elif p.startswith('ev'):
                final = intersection(final, evyatar)
            elif p.startswith('el'):
                final = intersection(final,)
            elif p.startswith('g') or p.startswith('to'):
                final = intersection(final, gadNtomer)
            elif p.startswith('s'):
                final = intersection(final, shlomo)
        return random.choice(final)


if __name__ == '__main__':
    print(pickgame([]))
