import json
import random


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


# data
data=[]
with open('PyBotConfig.json', 'r') as json_file:
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


def gameinfo(args):
    if not args:
        return "**All the Games are :** \n\n{}".format(
            ', '.join(games))
    final = games
    if args[0].lower().startswith('c'):
        category = args[1]
        if category.startswith('on'):
            final = onlinemp
        elif category.startswith('st'):
            final = story
        elif category.startswith('q'):
            final = quickfun
        elif category.startswith('sh'):
            final = shooters
        elif category.startswith('z'):
            final = zombies
        elif category.startswith('t'):
            final = topnotch
        elif category.startswith('op'):
            final = openworld
        elif category.startswith('m'):
            final = mpforfun
        return "**{} Games are :** \n\n{}".format(
            (category[0].upper()+category[1:].lower()), ', '.join(final))
    else:
        player = args[0]
        if player.lower().startswith('a'):
            final = avihay
        elif player.lower().startswith('ev'):
            final = evyatar
        elif player.lower().startswith('el'):
            final = eliran
        elif player.lower().startswith('g') or player.lower().startswith('to'):
            final = gadNtomer
        elif player.lower().startswith('s'):
            final = shlomo
        return "**{}'s Games are :** \n\n{}".format(player, ', '.join(final))
