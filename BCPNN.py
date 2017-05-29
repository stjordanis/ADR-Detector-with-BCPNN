import numpy as np

file1 = open('data For ML/DICTMedicine.txt', 'r', encoding='utf-8')
file2 = open('data For ML/DICTADRs.txt', 'r', encoding='utf-8')
fw = open('answerYes.txt', 'w', encoding='utf-8')

dim = {}
dia = {}
cnm = 0
cna = 0

for lines in file1:
    cnm += 1
    v = lines.split('|')
    for itm in v:
        s = itm.strip()
    dim[int(v[1])] = v[0]

for lines in file2:
    cna += 1
    v = lines.split('|')
    for itm in v:
        s = itm.strip()
    dia[int(v[1])] = v[0]

file = open('ThetaCN.txt', 'r', encoding='utf-8')

T = []

for i in range(0, 631):
    at = []
    for j in range(0, 1256):
        at.append(0)
    T.append(at)


for i, row in enumerate(file):
    v = []
    list = row.split(' ')
    for j, ele in enumerate(list):
        if(len(ele) <= 2): continue
        t = float(ele)
        T[j][i] = t

for i, row in enumerate(T):
    v = []
    for j, ele in enumerate(row):
        if(ele > 3.0): v.append(dia[j])
    fw.write(str(dim[i]) + '=>')
    for adr in v:
        fw.write('|' + adr)
    fw.write('\n')
