import random
false = False

co1 = 0
co2 = 0

cur = ''
cur += str(co1)
cur += ','
cur += str(co2)

co = 0

on = '\n' * 100

fi = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]


def join(mer):
    st = ''
    for obj in mer:
        st += f'{str(obj)} '
        st = st.replace('0', '.')
        st = st.replace('1', '↑')
        st = st.replace('8', '█')
        st = st.replace('9', '░')
        st = st.replace('2', '|')
    print(st)


def spawn():
    global o
    global false
    global cur
    cu = 0
    fc = open(f'{cur}.txt', 'r+')
    fcc = fc.readlines()
    while True:
        try:
            for item in fcc:
                item = item.rstrip('\n')
                item = item.replace('8', '0')
                item = item.replace('9', '0')
                lst = item.split(' ')
                del lst[0]
                for i in range(len(lst)):
                    lst[i] = int(lst[i])
                fi[cu] = lst
                cu += 1
        except IndexError:
            break
    ran = random.randint(0, 9)
    ran1 = random.randint(0, 9)
    fi[ran][ran1] = 8
    o = 0
    for item in fi:
        join(item)


def new():
    global t
    global t2
    global o
    global ar
    global fi
    global red
    global cur
    ar = [
        [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(),
         random.random(), random.random(), random.random(), random.random()],
        [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(),
         random.random(), random.random(), random.random(), random.random()],
        [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(),
         random.random(), random.random(), random.random(), random.random()],
        [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(),
         random.random(), random.random(), random.random(), random.random()],
        [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(),
         random.random(), random.random(), random.random(), random.random()],
        [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(),
         random.random(), random.random(), random.random(), random.random()],
        [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(),
         random.random(), random.random(), random.random(), random.random()],
        [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(),
         random.random(), random.random(), random.random(), random.random()],
        [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(),
         random.random(), random.random(), random.random(), random.random()],
        [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(),
         random.random(), random.random(), random.random(), random.random()]
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
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
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


def mo_b():
    global co1
    global co2
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
                    try:
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
                    except IndexError:
                        try:
                            t2 = item.index(8)
                            cu = 0
                            co1 -= 1
                            cur = ''
                            cur += str(co1)
                            cur += ','
                            cur += str(co2)
                            fc = open(f'{cur}.txt', 'r+')
                            fcc = fc.readlines()
                            while True:
                                try:
                                    for item in fcc:
                                        item = item.rstrip('\n')
                                        item = item.replace('8', '0')
                                        item = item.replace('9', '0')
                                        lst = item.split(' ')
                                        del lst[0]
                                        for i in range(len(lst)):
                                            lst[i] = int(lst[i])
                                        fi[cu] = lst
                                        cu += 1
                                except IndexError:
                                    break
                            fi[0][t2] = 8
                            o = 0
                        except FileNotFoundError:
                            new()
                            fil = open('files.txt', 'a')
                            fil.writelines(f'{str(co1)},{str(co2)}\n')

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
                    if t == 0:
                        try:
                            t2 = item.index(8)
                            cu = 0
                            co1 += 1
                            cur = ''
                            cur += str(co1)
                            cur += ','
                            cur += str(co2)
                            fc = open(f'{cur}.txt', 'r+')
                            fcc = fc.readlines()
                            while True:
                                try:
                                    for item in fcc:
                                        item = item.rstrip('\n')
                                        item = item.replace('8', '0')
                                        item = item.replace('9', '0')
                                        lst = item.split(' ')
                                        del lst[0]
                                        for i in range(len(lst)):
                                            lst[i] = int(lst[i])
                                        fi[cu] = lst
                                        cu += 1
                                except IndexError:
                                    break
                            fi[9][t2] = 8
                            o = 0
                        except FileNotFoundError:
                            new()
                            fil = open('files.txt', 'a')
                            fil.writelines(f'{str(co1)},{str(co2)}\n')
                    elif fi[t - 1][t2] == 2:
                        break
                    elif fi[t - 1][t2] == 1:
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
                    try:
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
                    except IndexError:
                        try:
                            for item in fi:
                                if 8 in item:
                                    t = fi.index(item)
                            cu = 0
                            co2 += 1
                            cur = ''
                            cur += str(co1)
                            cur += ','
                            cur += str(co2)
                            fc = open(f'{cur}.txt', 'r+')
                            fcc = fc.readlines()
                            while True:
                                try:
                                    for item in fcc:
                                        item = item.rstrip('\n')
                                        item = item.replace('8', '0')
                                        item = item.replace('9', '0')
                                        lst = item.split(' ')
                                        del lst[0]
                                        for i in range(len(lst)):
                                            lst[i] = int(lst[i])
                                        fi[cu] = lst
                                        cu += 1
                                except IndexError:
                                    break
                            fi[t][0] = 8
                            o = 0
                        except FileNotFoundError:
                            new()
                            fil = open('files.txt', 'a')
                            fil.writelines(f'{str(co1)},{str(co2)}\n')

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
                    print(t2)
                    if t2 == 0:
                        try:
                            for item in fi:
                                if 8 in item:
                                    t = fi.index(item)
                            cu = 0
                            co2 -= 1
                            cur = ''
                            cur += str(co1)
                            cur += ','
                            cur += str(co2)
                            fc = open(f'{cur}.txt', 'r+')
                            fcc = fc.readlines()
                            while True:
                                try:
                                    for item in fcc:
                                        item = item.rstrip('\n')
                                        item = item.replace('8', '0')
                                        item = item.replace('9', '0')
                                        lst = item.split(' ')
                                        del lst[0]
                                        for i in range(len(lst)):
                                            lst[i] = int(lst[i])
                                        fi[cu] = lst
                                        cu += 1
                                except IndexError:
                                    break
                            fi[t][9] = 8
                            o = 0
                        except FileNotFoundError:
                            new()
                            fil = open('files.txt', 'a')
                            fil.writelines(f'{str(co1)},{str(co2)}\n')
                    elif fi[t][t2 - 1] == 2:
                        break
                    elif fi[t][t2 - 1] == 1:
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
                    # places item at the index associated with each input
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
        cf = open(f'{co1},{co2}.txt', 'w+')
        for row in fi:
            for item in row:
                cf.write(f' {str(item)}')
            cf.write('\n')


def enemy_s():
    ran1 = random.randint(0, 9)
    ran2 = random.randint(0, 9)
    while True:
        if fi[ran1][ran2] == 8:
            pass
        elif fi[ran1][ran2] == 1:
            pass
        else:
            fi[ran1][ran2] = 9
            break


for item in fi:
    if 8 in item:
        p1 = fi.index(item)
        p2 = item.index(8)
for item in fi:
    if 9 in item:
        e1 = fi.index(item)
        e2 = item.index(9)


def enemy_m():
    for item in fi:
        if 8 in item:
            p1 = fi.index(item)
            p2 = item.index(8)
            for item in fi:
                if 9 in item:
                    e1 = fi.index(item)
                    e2 = item.index(9)
                    if p2 < e2:
                        if fi[e1][e2 - 1] == 1:
                            try:
                                fi[e1 - 1][e2] = 9
                                fi[e1][e2] = 0
                                break
                            except IndexError:
                                fi[e1 + 1][e2] = 9
                                fi[e1][e2] = 0
                                break
                        elif fi[e1][e2 - 1] == 2:
                            try:
                                fi[e1 - 1][e2] = 9
                                fi[e1][e2] = 0
                                break
                            except IndexError:
                                fi[e1 + 1][e2] = 9
                                fi[e1][e2] = 0
                                break
                        else:
                            try:
                                fi[e1][e2 - 1] = 9
                                fi[e1][e2] = 0
                                break
                            except IndexError:
                                fi[e1][e2 + 1] = 9
                                break
                    elif p2 > e2:
                        if fi[e1][e2 + 1] == 1:
                            try:
                                fi[e1 - 1][e2] = 9
                                fi[e1][e2] = 0
                                break
                            except IndexError:
                                fi[e1 + 1][e2] = 9
                                fi[e1][e2] = 0
                                break
                        elif fi[e1][e2 + 1] == 2:
                            try:
                                fi[e1 - 1][e2] = 9
                                fi[e1][e2] = 0
                                break
                            except IndexError:
                                fi[e1 + 1][e2] = 9
                                fi[e1][e2] = 0
                                break
                        else:
                            fi[e1][e2 + 1] = 9
                            fi[e1][e2] = 0
                            break
                    elif p1 < e1:
                        if fi[e1 - 1][e2] == 1:
                            try:
                                fi[e1][e2 - 1] = 9
                                fi[e1][e2] = 0
                                break
                            except IndexError:
                                fi[e1][e2 + 1] = 9
                                fi[e1][e2] = 0
                                break
                        elif fi[e1 - 1][e2] == 2:
                            try:
                                fi[e1][e2 - 1] = 9
                                fi[e1][e2] = 0
                                break
                            except IndexError:
                                fi[e1][e2 + 1] = 9
                                fi[e1][e2] = 0
                                break
                        else:
                            fi[e1 - 1][e2] = 9
                            fi[e1][e2] = 0
                            break
                    elif p1 > e1:
                        if fi[e1 + 1][e2] == 1:
                            try:
                                fi[e1][e2 - 1] = 9
                                fi[e1][e2] = 0
                                break
                            except IndexError:
                                fi[e1][e2 + 1] = 9
                                fi[e1][e2] = 0
                                break
                        elif fi[e1 + 1][e2] == 2:
                            try:
                                fi[e1][e2 - 1] = 9
                                fi[e1][e2] = 0
                                break
                            except IndexError:
                                fi[e1][e2 + 1] = 9
                                fi[e1][e2] = 0
                                break
                        else:
                            fi[e1 + 1][e2] = 9
                            fi[e1][e2] = 0
                            break

