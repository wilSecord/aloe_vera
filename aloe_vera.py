import random

# Defining spawn location
sly = random.randint(0, 9)
slx = random.randint(0, 9)
# Defining what the player spawns on
o = '.'

# Defining the random game board
ar = [
    [random.random(), random.random(), random.random(), random.random(), random.random(),
     random.random(), random.random(), random.random(), random.random(), random.random()],
    [random.random(), random.random(), random.random(), random.random(), random.random(),
     random.random(), random.random(), random.random(), random.random(), random.random()],
    [random.random(), random.random(), random.random(), random.random(), random.random(),
     random.random(), random.random(), random.random(), random.random(), random.random()],
    [random.random(), random.random(), random.random(), random.random(), random.random(),
     random.random(), random.random(), random.random(), random.random(), random.random()],
    [random.random(), random.random(), random.random(), random.random(), random.random(),
     random.random(), random.random(), random.random(), random.random(), random.random()],
    [random.random(), random.random(), random.random(), random.random(), random.random(),
     random.random(), random.random(), random.random(), random.random(), random.random()],
    [random.random(), random.random(), random.random(), random.random(), random.random(),
     random.random(), random.random(), random.random(), random.random(), random.random()],
    [random.random(), random.random(), random.random(), random.random(), random.random(),
     random.random(), random.random(), random.random(), random.random(), random.random()],
    [random.random(), random.random(), random.random(), random.random(), random.random(),
     random.random(), random.random(), random.random(), random.random(), random.random()],
    [random.random(), random.random(), random.random(), random.random(), random.random(),
     random.random(), random.random(), random.random(), random.random(), random.random()]
]

# Defining base game board
fi = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
]


# Drawing game board
def draw(gb):
    for thing in gb:
        st = ' '.join(thing)
        print(st)


# Replacing any random float > 0.7 with '+'
for item in ar:
    for val in item:
        if val.__round__(3) >= .7:
            i = ar.index(item)
            e = item.index(val)
            fi[i][e] = '+'
fi[slx][sly] = '#'
print('''
''')
while True:
    mo = input('> ')
    if mo == 's':
        for item in fi:
            if '#' in item:
                t = fi.index(item)
                t2 = item.index('#')
                o2 = fi[t + 1][t2]
                if fi[t + 1][t2] == 1:
                    break
                else:
                    fi[t + 1][t2] = '#'
                    fi[t][t2] = o
                    o = o2
                    break
        draw(fi)
        print('''
        ''')
    elif mo == 'w':
        for item in fi:
            if '#' in item:
                t = fi.index(item)
                t2 = item.index('#')
                o2 = fi[t - 1][t2]
                if fi[t +- 1][t2] == 1:
                    break
                else:
                    fi[t - 1][t2] = '#'
                    fi[t][t2] = o
                    o = o2
                    break
        draw(fi)
        print('''
        ''')
    elif mo == 'd':
        for item in fi:
            if '#' in item:
                t = fi.index(item)
                t2 = item.index('#')
                o2 = fi[t][t2 + 1]
                if fi[t][t2 + 1] == 1:
                    break
                else:
                    fi[t][t2 + 1] = '#'
                    fi[t][t2] = o
                    o = o2
                    break
        draw(fi)
        print('''
        ''')
    elif mo == 'a':
        for item in fi:
            if '#' in item:
                t = fi.index(item)
                t2 = item.index('#')
                o2 = fi[t][t2 - 1]
                if fi[t][t2 - 1] == 1:
                    break
                else:
                    fi[t][t2 - 1] = '#'
                    fi[t][t2] = o
                    o = o2
                    break
        draw(fi)
        print('''
        ''')
