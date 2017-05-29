import AC_Automaton
import tryi
import numpy as np
import xdrlib, sys
import xlrd

def gen(str):
    flag = False
    s=''
    for i, ch in enumerate(str):
      if(str[i] == u'无'):
          if(str[i + 1] == u'明'): continue
          else: flag = True
      if (str[i] == u'否'):
          flag = True
      if(flag == False): s = s + ch
      if(ch == u'，' or ch == u','): flag = False
    return s

def process(str):
    res = u''
    isParenthesis = False
    for ch in str:
        if(ch == u'（' or ch == u'('): isParenthesis = True
        else:
            if(isParenthesis == True): continue
            elif(ch == u'）' or ch == u')'): isParenthesis = False
            else: res = res + ch
    return res

def get(str1):
    print (str1)
    data = xlrd.open_workbook(str1)
    tableOrder = data.sheet_by_name(u'Order')  # 通过名称获取
    tableEmr = data.sheet_by_name(u'emr')
    PatientIDe = tableEmr.col_values(0)
    PatientInfoe = tableEmr.col_values(4)
    PatientIDo = tableOrder.col_values(0)
    Medicineo = tableOrder.col_values(11)
    MedicineTypeo = tableOrder.col_values(13)

    print(len(PatientIDo), len(Medicineo), len(MedicineTypeo))
    print(len(PatientIDe), len(PatientInfoe))

    lenO = len(PatientIDo)
    lenE = len(PatientIDe)

    Patient1 = []
    Patient2 = []
    Medicine1 = []
    Medicine2 = []
    for i in range(lenE):
        if (i == 0): continue
        Patient1.append(PatientIDe[i])
        Patient2.append(gen(PatientInfoe[i]))

    for i in range(lenO):
        if (i == 0): continue
        if (MedicineTypeo[i] == u'西药' or MedicineTypeo[i] == u'中成药'):
            Medicine1.append(PatientIDo[i])
            Medicine2.append(process(Medicineo[i]))

    return Patient1, Patient2, Medicine1, Medicine2

def main(str1, str2):
    fi = open(str2, 'w', encoding='utf-8')
    A,B,C,D = get(str1)

    ac = AC_Automaton.UnicodeAcAutomation()
    file = open('forAC/CNADR_Library.txt', 'r', encoding='utf-8')
    pu = []

    for adr in file:
        s = adr.strip('\n')
        if (len(s) < 2): continue
        pu.append(s)

    pu = np.unique(pu)
    for x in pu:
        ac.insert(x)
    ac.build_automation()

    cnt = 0
    dictIDtoE = {}
    dictEtoID = {}
    medi = []
    v = []

    for i, x in enumerate(C):
        if((x in dictEtoID) == False):
            if(i > 0):
                medi.append(v)
                del v[:]
            dictEtoID[x] = cnt
            dictIDtoE[cnt] = x
            cnt += 1
            v.append(D[i])
        else:
            v.append(D[i])


    if(len(v) > 0):
        medi.append(v)


    print (len(medi))
   # print (dictEtoID['ZY010000049908'])

    for i, id in enumerate(A):
        if ((id in dictEtoID) == False): continue
        else:
            adrlist = []
            ac.matchOne(adrlist, B[i])
            print (dictEtoID[id])
            adrlist = np.unique(adrlist)
            print (adrlist)
            xx = medi[dictEtoID[id]]
            xx = np.unique(xx)

            gnu = []
            for x in adrlist:
                gnu.append(x)
            a, b, c, d = tryi.get(xx)
            fi.write(A[i] + ':\n')
            fi.write(u'强信号:')

            for x in a:
                if ((x in gnu) == True):
                    gnu.remove(x)
                    print(x)
                    fi.write(' ' + x)
            fi.write('\n')

            fi.write(u'中信号:')
            for x in b:
                if ((x in gnu) == True):
                    gnu.remove(x)
                    fi.write(' ' + x)
            fi.write('\n')

            fi.write(u'弱信号:')
            for x in c:
                if x in gnu:
                    gnu.remove(x)
                    fi.write(' ' + x)
            fi.write('\n')

            fi.write(u'无信号:')
            for x in d:
                if x in gnu:
                    gnu.remove(x)
                    fi.write(' ' + x)
            fi.write('\n')

#main('2016-05-02.xls','')
