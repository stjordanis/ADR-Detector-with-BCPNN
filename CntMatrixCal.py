#coding = utf-8
import numpy as np

def main():

    file = open('Stat.txt', "r", encoding='utf-8')
    file_t = open('SourceData/ItemID.txt', "r", encoding='utf-8')
    file_w = open('data For ML/CNTij.txt', "w", encoding='utf-8')
    file_w1 = open("data For ML/CNTj.txt", "w", encoding='utf-8')
    file_w2 = open("data For ML/CNTi.txt", "w", encoding='utf-8')

    totalMedi = 0
    ThetaW = []
    ThetaM = []
    ThetaA = []

    dict_ID = {}
    dict_ADR = {}
    dict_Medi = {}

    ADRlist = []
    ADRlistID = []
    totalID = 0

    for i in range(0, 5000):
        at = []
        ThetaM.append(0)
        ThetaA.append(0)
        for j in range(0, 5000):
            at.append(0)
        ThetaW.append(at)

    for lines in file:
        vec = lines.split('|')
        li = []
        realID = -1
        for i, x in enumerate(vec):
            x = x.strip()
            if(len(x) < 2): continue
            if(i == 0):
                if((x in dict_ID) == False): dict_ID[x] = totalID; realID = totalID; totalID += 1
                else: realID = dict_ID[x]
            else:
                 li.append(x)
        if(len(ADRlist) == realID):
            ADRlist.append(li)
        else:
            for v in li:
                ADRlist[realID].append(v)

    print (totalID)

    totalID2 = 0

    for i in range(0, totalID):
        list = []
        ADRlist[i] = np.unique(ADRlist[i])
        for v in ADRlist[i]:
            if ((v in dict_ADR) == False):
                dict_ADR[v] = totalID2; totalID2 += 1
            ThetaA[dict_ADR[v]] += 1
            list.append(dict_ADR[v])
        ADRlistID.append(list)

    for j in range(0, totalID2):
        if(j == totalID2 - 1): file_w2.write(str(ThetaA[j]) + '\n')
        else: file_w2.write(str(ThetaA[j]) + ' ')

    for lines in file_t:
        vec = lines.split('|')
        realID = -1
        cata = []
        for i, x in enumerate(vec):
            MediId = -1
            x = x.strip()
            if(len(x) <= 2): continue
            if(i == 0):
                if((x in dict_ID) == False): continue
                else: realID = dict_ID[x]
            else:
                if ((x in dict_Medi) == False): dict_Medi[x] = totalMedi; MediId = dict_Medi[x]; totalMedi += 1
                else: MediId = dict_Medi[x];
                cata.append(MediId)
            if(realID == -1): break
        if(realID == -1): continue
        for x in cata:
            ThetaM[x] += 1
            for y in ADRlistID[realID]:
                ThetaW[y][x] += 1

    for i in range(0, totalMedi):
        if (i == totalMedi - 1):
            file_w1.write(str(ThetaM[i]) + '\n')
        else:
            file_w1.write(str(ThetaM[i]) + ' ')

    for i in range(0, totalID2):
        for j in range(0, totalMedi):
            if(j == totalMedi - 1): file_w.write(str(ThetaW[i][j]) + '\n')
            else: file_w.write(str(ThetaW[i][j]) + ' ')


    filew2 = open("data For ML/DICTMedicine.txt", "w", encoding='utf-8')
    filew1 = open("data For ML/DICTADRs.txt", "w", encoding='utf-8')

    cnt = 0
    for x in dict_ADR:
        cnt += 1
        filew1.write(x + '|' + str(dict_ADR[x]) + '\n')
    print (cnt)
    cnt = 0
    for x in dict_Medi:
        cnt += 1
        filew2.write(x + '|' + str(dict_Medi[x]) + '\n')
    print (cnt)


#10510
#1257
#675