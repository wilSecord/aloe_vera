import random
# This is the brains

co = 0

on = '\n' * 100

ar = [
    [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random()],
    [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random()],
    [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random()],
    [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random()],
    [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random()],
    [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random()],
    [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random()],
    [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random()],
    [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random()],
    [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random()]
]


fi = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def join(mer):
    st = ''
    for obj in mer:
        st += f'{str(obj)} '
        st = st.replace('0', '.')
        st = st.replace('1', '↑')
        st = st.replace('8', '█')
        st = st.replace('2', '|')
    print(st)


for item in ar:
    for val in item:
        if val.__round__(3) >= .7:
            i = ar.index(item)
            e = item.index(val)
            fi[i][e] = 1
ran = random.randint(0, 9)
ran1 = random.randint(0, 9)
o = 0
fi[ran][ran1] = 8
for item in fi:
    join(item)
print('''
''')


def mo_b():
    global on
    global co
    global o
    global fi
    mo1 = input('> ')
    mo2 = []
    for item in mo1:
        mo2.append(item)
    for mo in mo2:
        if mo == 's':
            for item in fi:
                if 8 in item:
                    # moves 8 and replaces its previous instance with the tile there before it
                    t = fi.index(item)
                    t2 = item.index(8)
                    o2 = fi[t + 1][t2]
                    if fi[t + 1][t2] == 1:
                        break
                    elif fi[t + 1][t2] == 2:
                        break
                    else:
                        fi[t + 1][t2] = 8
                        fi[t][t2] = o
                        o = o2
                        break
            print(on)
            for item in fi:
                join(item)
            print(co)
        elif mo == 'w':
            for item in fi:
                if 8 in item:
                    t = fi.index(item)
                    t2 = item.index(8)
                    o2 = fi[t - 1][t2]
                    if fi[t - 1][t2] == 1:
                        break
                    elif fi[t - 1][t2] == 2:
                        break
                    else:
                        fi[t - 1][t2] = 8
                        fi[t][t2] = o
                        o = o2
                        break
            print(on)
            for item in fi:
                join(item)
            print(co)
        elif mo == 'd':
            for item in fi:
                if 8 in item:
                    t = fi.index(item)
                    t2 = item.index(8)
                    o2 = fi[t][t2 + 1]
                    if fi[t][t2 + 1] == 1:
                        break
                    elif fi[t][t2 + 1] == 2:
                        break
                    else:
                        fi[t][t2 + 1] = 8
                        fi[t][t2] = o
                        o = o2
                        break
            print(on)
            for item in fi:
                join(item)
            print(co)
        elif mo == 'a':
            for item in fi:
                if 8 in item:
                    t = fi.index(item)
                    t2 = item.index(8)
                    o2 = fi[t][t2 - 1]
                    if fi[t][t2 - 1] == 1:
                        break
                    elif fi[t][t2 - 1] == 2:
                        break
                    else:
                        fi[t][t2 - 1] = 8
                        fi[t][t2] = o
                        o = o2
                        break
            print(on)
            for item in fi:
                join(item)
            print(co)
        # mo, i k l j breaks
        elif mo == 'i':
            for item in fi:
                if 8 in item:
                    # breaks item at the index associated with each input
                    t = fi.index(item)
                    t2 = item.index(8)
                    if fi[t - 1][t2] == 1:
                        fi[t - 1][t2] = 0
                        co += 1
                    elif fi[t - 1][t2] == 2:
                        fi[t - 1][t2] = 0
                        co += 1
                    else:
                        break
            print(on)
            for item in fi:
                join(item)
            print(co)
        elif mo == 'k':
            for item in fi:
                if 8 in item:
                    t = fi.index(item)
                    t2 = item.index(8)
                    if fi[t + 1][t2] == 1:
                        fi[t + 1][t2] = 0
                        co += 1
                    elif fi[t + 1][t2] == 2:
                        fi[t + 1][t2] = 0
                        co += 1
                    else:
                        break
            print(on)
            for item in fi:
                join(item)
            print(co)
        elif mo == 'j':
            for item in fi:
                if 8 in item:
                    t = fi.index(item)
                    t2 = item.index(8)
                    if fi[t][t2 - 1] == 1:
                        fi[t][t2 - 1] = 0
                        co += 1
                    elif fi[t][t2 - 1] == 2:
                        fi[t][t2 - 1] = 0
                        co += 1
                    else:
                        break
            print(on)
            for item in fi:
                join(item)
            print(co)
        elif mo == 'l':
            for item in fi:
                if 8 in item:
                    t = fi.index(item)
                    t2 = item.index(8)
                    if fi[t][t2 + 1] == 1:
                        fi[t][t2 + 1] = 0
                        co += 1
                    elif fi[t][t2 + 1] == 2:
                        fi[t][t2 + 1] = 0
                        co += 1
                    else:
                        break
            print(on)
            for item in fi:
                join(item)
            print(co)
        elif mo == 't':
            for item in fi:
                if 8 in item:
                    # breaks item at the index associated with each input
                    t = fi.index(item)
                    t2 = item.index(8)
                    if co >= 1 and fi[t - 1][t2] != 1:
                        fi[t - 1][t2] = 2
                        co -= 1
                    else:
                        break
            print(on)
            for item in fi:
                join(item)
            print(co)
        elif mo == 'g':
            for item in fi:
                if 8 in item:
                    t = fi.index(item)
                    t2 = item.index(8)
                    if co >= 1 and fi[t + 1][t2] != 1:
                        fi[t + 1][t2] = 2
                        co -= 1
                    else:
                        break
            print(on)
            for item in fi:
                join(item)
            print(co)
        elif mo == 'f':
            for item in fi:
                if 8 in item:
                    t = fi.index(item)
                    t2 = item.index(8)
                    if co >= 1 and fi[t][t2 - 1] != 1:
                        fi[t][t2 - 1] = 2
                        co -= 1
                    else:
                        break
            print(on)
            for item in fi:
                join(item)
            print(co)
        elif mo == 'h':
            for item in fi:
                if 8 in item:
                    t = fi.index(item)
                    t2 = item.index(8)
                    if co >= 1 and fi[t][t2 + 1] != 1:
                        fi[t][t2 + 1] = 2
                        co -= 1
                    else:
                        break
            print(on)
            for item in fi:
                join(item)
            print(co)
