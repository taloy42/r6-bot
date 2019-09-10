import random
import nicetables
names = ['אלרין','אביתר','אביחי','בן','לוי',]

def teamselect(names):
    names = list(names)
    random.shuffle(names)
    blue = []
    orange = []
    table = [['Blue Team','Orange Team']]
    limit = len(names)
    isblue = True
    for i in range(limit):
        if isblue:
            blue.append(names.pop())
        else:
            orange.append(names.pop())
        isblue = not isblue
    if len(blue)==len(orange):
        for i in range(len(blue)):
            table.append([blue[i],orange[i]])
    else:
        for i in range(len(orange)):
            table.append([blue[i],orange[i]])
        table.append([blue[len(blue)-1],''])
    return nicetables.nice_table(table)
