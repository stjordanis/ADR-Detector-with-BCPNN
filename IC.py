#coding-utf-8
import numpy as np
import math

def main():
    filei = open('data For ML/CNTi.txt', 'r', encoding='utf-8')
    filej = open('data For ML/CNTj.txt', 'r', encoding='utf-8')
    fileij = open('data For ML/CNTij.txt', 'r', encoding='utf-8')

    cnti = []
    N = 0
    for s in filei:
        v = s.split(' ')
        for i in v:
          cnti.append(int(i))
          N = N + int(i)

    cntj = []

    for s in filej:
        v = s.split(' ')
        for i in v:
          cntj.append(int(i))
          N = N + int(i)

    cntij = []

    for s in fileij:
        c = []
        v = s.split(' ')
        for i in v:
          c.append(int(i))
        cntij.append(c)

    file = open('ThetaCN.txt', 'w', encoding='utf-8')
    Theta = []
    epi = 1e-9

    # 86 i medi + adr j = medi k = adr
    for i, c in enumerate(cntij):
        v = []
        for j, k in enumerate(cntij[i]):
            gamma = 1.0 * (N + 2) * (N + 2) / (cnti[i] + 1) / (cntj[j] + 1)
            E = math.log(gamma, 2) + math.log(cntij[i][j] + 1, 2) - math.log(N + gamma, 2)
            V = (N - cntij[i][j] + gamma - 1)/((cntij[i][j] + 1) * (1 + N + 1)) + (N - cnti[i] + 1)/((cnti[i] + 1)*(3 + N)) + (N - cntj[j] + 1) / ((cnti[i] + 1)*(N + 3))
            V = V / (math.log(2) * math.log(2))
            v.append(E - 2 * math.sqrt(V))
        Theta.append(v)

    for c in Theta:
       for j in c:
           file.write(str(j) + ' ')
       file.write('\n')