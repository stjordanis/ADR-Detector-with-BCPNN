import numpy as np

def get(Medilist):
    file1 = open('data For ML/DICTMedicine.txt', 'r', encoding='utf-8')
    file2 = open('data For ML/DICTADRs.txt', 'r', encoding='utf-8')
    High = []
    Med = []
    Low = []
    Unknown = []

    dim = {}
    dia = {}

    for lines in file1:
        v = lines.split('|')
        for itm in v:
            s = itm.strip()
        dim[v[0]] = int(v[1])

    for lines in file2:
        v = lines.split('|')
        for itm in v:
            s = itm.strip()
        dia[(int)(v[1])] = v[0]

    file = open('ThetaCN.txt', 'r', encoding='utf-8')

    T = []

    for i in range(0, 5000):
        at = []
        for j in range(0, 5000):
            at.append(0)
        T.append(at)

    ro = 0
    co = 0

    for i, row in enumerate(file):
        ro = max(ro, i)
        v = row.split()
        for j, ele in enumerate(v):
            co = max(co, j)
            T[j][i] = float(ele)

    for med in Medilist:
        if((med in dim) == False): continue
        id = dim[med]
        for x in range(ro + 1):
            if(T[id][x] >= 3.0): High.append(dia[x])
            elif(1.5 <= T[id][x] < 3.0): Med.append(dia[x])
            elif(0 <= T[id][x] < 1.5): Low.append(dia[x])
            else: Unknown.append(dia[x])

    High = np.unique(High)
    Low = np.unique(Low)
    Med = np.unique(Med)
    Unknown = np.unique(Unknown)

    return High, Med, Low, Unknown


#1239
#631

#get('ds')
