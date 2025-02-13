#encoding=utf-8

import pymssql
import sys

class MSSQL:
    """
    对pymssql的简单封装
    pymssql库，该库到这里下载：http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql
    使用该库时，需要在Sql Server Configuration Manager里面将TCP/IP协议开启

    用法：

    """

    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

        调用示例：
                ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        """
        执行非查询语句

        调用示例：
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

def process(str):
    res = u''
    isParenthesis = False
    for ch in str:
        if(ch == u'（' or ch == u'('): isParenthesis = True
        else:
            if(isParenthesis == True or (ch >= '0'and ch <= '9') or ch == '.' or ch == '%'): continue
            elif(ch == u'）' or ch == u')'): isParenthesis = False
            else: res = res + ch
    return res

def main():
    # reslist = ms.ExecQuery('SELECT [MedicinalProduct], [ReactionMeddrapt] FROM [ADR].[dbo].[Drug_Reaction]')
    ms = MSSQL(host="PC-PC", user="sa", pwd="sa", db="ADR")
    res = ms.ExecQuery('SELECT [INPATIENT_NO], [PRESENTMEDICALHISTORY] FROM [MedicalData2].[dbo].[AfterJoin]')
    file = open('RawMedicalReport.txt', "w")
    dict = {}
    cnt = 0
    for i in res:
        v = []
        for j in i:
            v.append(j)
        if(v[0] in dict == False):
            file.write('\n')
            dict[v[0]] = cnt
            file.write(v[0]+ '|')
        for i, item in enumerate(v):
            if i == 0: continue
            file.write(process(v[i]) + '|')

#main()

# SELECT [INPATIENT_NO], [ITEM_NAME] FROM [MedicalData2].[dbo].[AfterJoin]

def tyu(str):
    file = open('str')