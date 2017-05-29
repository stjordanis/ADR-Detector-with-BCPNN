import urllib
import re
import sys

from googleapiclient.discovery import build

def translateNoob(querystr, to_l="zh-CN", from_l="en"):
    C_agent = {'User-Agent': "Chrome/31.0.165063"}
    tarurl = "http://translate.google.cn/m?hl=%s&sl=%s&ie=UTF-8&q=%s" % (to_l, from_l, querystr.replace(" ", "+"))
    request = urllib.Request(tarurl, headers=C_agent)
    result = urllib.urlopen(request).read()
    print (result)
    res = re.search(r"s=.{1}t0.{1}>[^<]*", result)
    print (res.group(0)[1:])
    if res:
        return res.group(0)[7:]
    else:
        return 'none'

def translate(str):
    service = build('translate', 'v2', developerKey='AIzaSyDhxO0IoE4DxcmlKQrqNCRGyyRM_tue2Cs')
    s = service.translations().list(
        source='en',
        target='zh-CN',
        q = str
    ).execute()
    for i in s:
        st = s[i]
        return st[0][u'translatedText']

file = open('forAC/Text.txt', 'r')
file_w = open('CNADR_Library.txt', 'a')

for v in file:
    k = v.split("|")
    file_w.write(k[0].strip() + '\n')

"""
v = []
cnt = 0
for adr in file:
  str = adr.strip().lower()
  t = translate(str)
  print t
  file_w.write(t + '\n')
  cnt += 1
  print cnt
"""