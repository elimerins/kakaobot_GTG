import pymysql
import copy
import re
import numpy as np
import operator
from kakaobotapp import lecturealgo

conn = pymysql.connect(host='localhost', user='root', password='password',
                       db='gtg', charset='utf8')
curs = conn.cursor()
sql = "select * from mj"
curs.execute(sql)
rows = curs.fetchall()
maj_cd_list=[]

for index in rows:
    maj_cd_list.append((index[1],index[2]))
    #print(maj_cd_list)
for maj in maj_cd_list:
    print(maj)
major='경영학과'
maj_cd=""
grade=2
for i in maj_cd_list:
    if(i[1]==major):
        maj_cd=i[0]
        print(maj_cd)
course_sql='''
select title,time,credit,IFNULL(cor_cd,'777') cor_cd 
FROM COURSE WHERE MAJ_CD=%s 
AND (GRADE LIKE %s
)
'''
curs.execute(course_sql,('C20110',"%{}%".format(str(grade))))
course_list=curs.fetchall()
print(course_list)
list=lecturealgo.generator(9,12,'컴퓨터공학과','3')
print(str(list))

