def value(colors):
    sumNum = 0
    for i in range(len(colors)-1, -1, -1):
        index = colorsArr().index(colors[i])
        print(f'index: {index} * 10**{i}')
        sumNum += index*(10**i)
    print(sumNum)
    return sumNum

def colorsArr():
    return[
        'black',
        'brown',
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'violet',
        'grey',
        'white'
    ]

