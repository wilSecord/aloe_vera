import random

# Defining spawn location
sly = random.randint(0, 9)
slx = random.randint(0, 9)

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

# Replacing any random float > 0.7 with '+'
for item in ar:
    for val in item:
        if val.__round__(3) >= .7:
            i = ar.index(item)
            e = item.index(val)
            fi[i][e] = '+'
fi[slx][sly] = '#'


# Drawing game board
def draw(gb):
    for item in gb:
        st = ' '.join(item)
        print(st)
draw(fi)