import pandas as pd
import random
def naa():
    ret = []
    for i in range(5):
        n = random.randint(1,9)
        ret.append(n)
        ret.append(n)
    return ret
def addhuan():
    ret = []
    while(1):
        a = random.randint(1,9)
        b = random.randint(1,9)
        if (a != b):
            break
    ret.append(a)
    ret.append(b)
    return ret
def naaa():
    ret = []
    for i in range(4):
        n = random.randint(1,9)
        ret.append(n)
        ret.append(n)
        ret.append(n)
    return ret
def nabb():
    ret = []
    for i in range(8):
        while(1):
            a = random.randint(1,9)
            b = random.randint(1,9)
            if (a != b):
                break
        ret.append(a)
        ret.append(b)
        ret.append(b)
    return ret
def wh():
    ret = []
    for i in range(4):
        x = random.randint(1,2)

        if (x == 1):#hang
            base = random.randint(1,3) *3 - 2
            ret.append(base)
            ret.append(base+1)
            ret.append(base+2)
        else:#lie
            base = random.randint(1,3)
            ret.append(base)
            ret.append(base+3)
            ret.append(base+6)
    return ret
def ncross():
    ret = []
    cross0 = [1, 5, 9]
    cross1 = [9, 5, 1]
    cross2 = [7, 5, 3]
    cross3 = [3, 5, 7]
    crosses = [cross0, cross1, cross2, cross3]
    for i in range(4):
        x = random.randint(1, 4)
        for j in crosses[x- 1]:
            ret.append(j)
    return ret
def abc3():
    ret = []
    for i in range(3):
        flag = 0
        while(flag == 0):
            a = random.randint(1, 9)
            b = random.randint(1, 9)
            c = random.randint(1, 9)
            if (a != b and a != c and b != c):
                flag = 1
                for x in range(3):
                    ret.append(a)
                    ret.append(b)
                    ret.append(c)
    return ret
list0 = []
for i in range(1, 10):
    list0.append(['pic/' + str(i) +'.png', "['{}']".format(str(i))])
dict0 = {}
for i in range(len(list0)):
    dict0[i+1] = list0[i]
#print(dict0)
num = []
for i in naa():
    num.append([i, 'aa'])
for i in addhuan():
    num.append([i, 'huan'])
for i in naaa():
    num.append([i, 'aaa'])
for i in addhuan():
    num.append([i, 'huan'])
for i in nabb():
    num.append([i, 'abb'])
for i in addhuan():
    num.append([i, 'huan'])
for i in wh():
    num.append([i, 'wh'])
for i in ncross():
    num.append([i, 'cross'])
for i in addhuan():
    num.append([i, 'huan'])
for i in abc3():
    num.append([i, 'abc3'])
ready = []
for i in range(len(num)):
    tem = dict0[num[i][0]][:]
    tem.append(num[i][1])
    tem.append(i+1)
    ready.append(tem)
data = pd.DataFrame(ready, columns = ['pic', 'ans', 'cla', 'no'])
data.to_csv('formal_click.csv', index = False)