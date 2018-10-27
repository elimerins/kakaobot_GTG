import pymysql
import copy
import re
import numpy as np
import operator
import lecturealgo as al



conn = pymysql.connect(host='localhost', user='root', password='password',
                       db='gtg', charset='utf8')
curs = conn.cursor()
sql = "select * from mj"
curs.execute(sql)
rows = curs.fetchall()
maj_cd_list=[]

string='운영체제(원어강의)'
string2='운영체제'
if string2 in string:
    print("duplicated")
for index in rows:
    maj_cd_list.append((index[1],index[2]))
major='컴퓨터공학과'
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
curs.execute(course_sql,(maj_cd,"%{}%".format(str(grade))))
course_list=curs.fetchall()

