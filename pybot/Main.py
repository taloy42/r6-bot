from discord.ext.commands import Bot
import discord
import random
from PickGame import pickgame
from GameInfo import gameinfo
import time

import json
json_file = open('PlayerGameData.json', 'r')
data = json.load(json_file)
PERMITTED_USERS = data['permitted_users']


c = discord.Client()
BOT_PREFIX = ['.', '!', '?']
TOKEN=''
with open('TOKEN.txt) as f:
          TOKEN=f.read()
TOKEN = 'NTYxNzA3MjQ4NzM3NTgzMTI1.XKCSHg.kCvuJ0wyJoETfeIADN_kFeuJ2zY'

client = Bot(command_prefix=BOT_PREFIX)


@client.command(name='עץ או פלי',
                description="עוזר לבחירות קשות בין חברים",
                brief="אין מה להסביר",
                aliases=['עפ', 'עץ_או_פלי', 'ht','hot','headsortails'],
                pass_context=True)
async def heads_or_tails(ctx):
    possible_responses = [0,1]
    heads = random.choice(possible_responses)
    f = open('heads.png','r')
    m = await ctx.send(file=discord.File('headsortails.gif'))
    if heads:
        time.sleep(5)
        await m.delete()
        await ctx.send(file=discord.File('heads.png'))
    else:
        time.sleep(7.5)
        await m.delete()
        await ctx.send(file=discord.File('tails.png'))

##@client.command(name='בחירת-קבוצות',
##                description='מחלק את האנשים שרושמים ל2 קבוצות',
##                brief='מחלק לקבוצות',
##                aliases=['ts', 'teamselect', 'בחירת-קבוצה', 'בק']
##                )
##async def team_select(ctx, *names):
##    names = list(names)
##    random.shuffle(names)
##    msg = "**Blue Team :**\n\n"
##    limit = len(names)//2
##    for num in range(1, limit+1):
##        msg += '**[ {} ]**   {}\n'.format(num, names.pop())
##
##    msg += "\n\n**Orange Team :** \n\n"
##    limit = len(names)
##    for num in range(1, limit+1):
##        msg += '**[ {} ]**   {}\n'.format(num, names.pop())
##    await ctx.send(msg)

@client.command(name='בחירת-קבוצות',
                description='מחלק את האנשים שרושמים ל2 קבוצות',
                brief='מחלק לקבוצות',
                aliases=['ts', 'teamselect', 'בחירת-קבוצה', 'בק']
                )
async def team_select(ctx, *names):
    author = ctx.message.author
    if author.name in PERMITTED_USERS:
        print(author.name,'is in the Permitted Users')
        names = list(names)
        random.shuffle(names)
        msg = "**Blue Team :**\n\n"
        limit = len(names)//2
        for num in range(1, limit+1):
            msg += '**[ {} ]**   {}\n'.format(num, names.pop())

        msg += "\n\n**Orange Team :** \n\n"
        limit = len(names)
        for num in range(1, limit+1):
            msg += '**[ {} ]**   {}\n'.format(num, names.pop())
        await ctx.send(msg)
    else:
        await ctx.send("<@{}>\nאתה לא יכול להשתמש בפקודה הזאת בויה, סורי".format(author.id))

@client.command(name='בחירת-משחק',
                description='בוחר משחק אקראי, בהתאם לאנשים שמשחקים או לקטגוריה הרצויה',
                brief='בוחר משחק',
                aliases=['pg', 'pickgame', 'pickgames', 'אחשלי']
                )
async def pick_game(ctx, *players):
    await ctx.send(pickgame(players))


@client.command(name='מידע',
                description='נותן מידע על שחקן או משחק מסוים',
                brief='נותן מידע',
                aliases=['gi', 'gameinfo', 'gamesinfo']
                )
async def game_info(ctx, *args):
    await ctx.send(gameinfo(args))


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='Wit U Nigga'))
    print('Logged in as {}\non {} servers for {} users\n-----------------------------------'.format(
        client.user.name, len(client.guilds), len(client.users)))
@client.command(name='try')
async def ttry(ctx):
    print(ctx.message.author.name)
##    roles = ctx.message.author.id
##    for r in roles:
##        print(r.name)
        
client.run(TOKEN)
