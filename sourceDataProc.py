#coding=utf-8
import numpy
import sys

def gen(str):
    str=str.decode('utf-8')
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

# To ignore parenthesis

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

def Medicine_pre():
    file = open('SourceData/ItemaId.txt', 'r')
    fi = open('ItemID.txt', 'w')
    for i in file:
        v = i.split('|')
        for j in v:
            if(j == '\n'): continue
            fi.write(process(j) + '|')
        fi.write('\n')

def text() :
    fil = open('SourceData/ItemaId.txt', 'r')
    fi = open('ItemID.txt', 'a')

Medicine_pre()
