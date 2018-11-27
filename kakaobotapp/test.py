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
    maj_cd_list.append((index[0],index[1],index[2]))
    #print(maj_cd_list)

real_course_list=[]

for maj_cd in maj_cd_list:
    #print(maj_cd)
    course_sql = '''
    select title,time,credit,IFNULL(cor_cd,'777') cor_cd 
    FROM COURSE WHERE MAJ_CD=%s 
    '''
    curs.execute(course_sql,(maj_cd[0]))
    course_list=curs.fetchall()
    if len(course_list)==0:
        #print(maj_cd[0]+' '+maj_cd[1]+' :',len(course_list))
        continue
    else:
        real_course_list.append(maj_cd[1])
        #print(real_course_list)
        print(maj_cd[0]+' '+maj_cd[1]+' :',len(course_list))
#print(course_list)
'''
for course in course_list:
    print(course)
'''

list=lecturealgo.generator(9,12,'미술·디자인학부(디자인)','3')
print(str(list))


