#coding=utf-8
import time
import numpy as np

KIND = 30

BASE = ord('a')

class Node():
    static = 0

    def __init__(self):
        self.fail = None
        self.next = [None] * KIND
        self.end = False
        self.word = None
        Node.static += 1

class AcAutomation():
    def __init__(self):
        self.root = Node()
        self.queue = []

    def getIndex(self, char):
        return ord(char) - BASE

    def insert(self, string):
        p = self.root
        for char in string:
            index = self.getIndex(char)
            if p.next[index] == None:
                p.next[index] = Node()
            p = p.next[index]
        p.end = True
        p.word = string
        #print p.word

    def build_automation(self):
        self.root.fail = None
        self.queue.append(self.root)
        while len(self.queue) != 0:
            parent = self.queue[0]
            self.queue.pop(0)
            for i, child in enumerate(parent.next):
                if child == None: continue
                if parent == self.root:
                    child.fail = self.root
                else:
                    failp = parent.fail
                    while failp != None:
                        if failp.next[i] != None:
                            child.fail = failp.next[i]
                            break
                        failp = failp.fail
                    if failp == None: child.fail = self.root
                self.queue.append(child)

    def matchOne(self, list, string):
        p = self.root
        for char in string:
            index = self.getIndex(char)
            while p.next[index] == None and p != self.root: p = p.fail
            if p.next[index] == None:
                p = self.root
            else:
                p = p.next[index]
                if p.end:
                    list.append(p.word)

        while p != self.root:
            p = p.fail
            if p.end:
                list.append(p.word)

class UnicodeAcAutomation():
    def __init__(self):
        self.ac = AcAutomation()

    def getAcString(self, string):
        string = bytearray(string.encode('utf-8'))
        ac_string = ''
        for byte in string:
            ac_string += chr(byte % 16 + BASE)
            ac_string += chr(byte // 16 + BASE)
        return ac_string

    def insert(self, string):
        ac_string = self.getAcString(string)
        self.ac.insert(ac_string)

    def build_automation(self):
        self.ac.build_automation()

    def matchOne(self, list, string):
        li = []
        ac_string = self.getAcString(string)
        self.ac.matchOne(li, ac_string)

        for x in li:
            s = bytearray()
            for i in range(len(x) // 2):
                s.append(ord(x[2 * i]) - ord('a') + (ord(x[2 * i + 1]) - ord('a')) * 16)
            ts = s.decode()
            list.append(ts)

def get_symptom(message) :

    start = time.clock()
    ac = UnicodeAcAutomation()
    file = open('forAC/CNADR_Library.txt', 'r', encoding='utf-8')
    nu = []

    for adr in file:
        s = adr.strip('\n')
        if (len(s) < 2): continue
        nu.append(s)

    nu = np.unique(nu)
    for x in nu:
        ac.insert(x)
    ac.build_automation()

    adrlist = []
    ac.matchOne(adrlist, message)
    adrlist = np.unique(adrlist)
    end = time.clock()
    print('running time = %s\n' % (end - start))

    return adrlist
