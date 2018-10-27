import pymysql
import copy
import numpy as np
import re
import operator

conn = pymysql.connect(host='localhost', user='root', password='password',
                       db='gtg', charset='utf8')

curs = conn.cursor()
sql = "select * from mj"
curs.execute(sql)
rows = curs.fetchall()
maj_cd_list = []
# print(rows[0])
for index in rows:
    maj_cd_list.append((index[1], index[2]))

# 받아올 항목 학과, 학점범위, 학년

combination = []
resultList = []
cohesion_checked_list = []
def generator(min,max,major,choice_grade):
    maj_cd = ""
    grade = choice_grade
    for i in maj_cd_list:
        if (i[1] == major):
            maj_cd = i[0]
            print(maj_cd)

    # 학년별 뽑아오기
    course_sql = '''
    select title,time,credit,IFNULL(cor_cd,'777') cor_cd 
    FROM COURSE WHERE MAJ_CD=%s 
    AND (GRADE LIKE %s
    )
    '''
    curs.execute(course_sql, (maj_cd, "%{}%".format(str(grade))))
    course_list = curs.fetchall()
    print(course_list)
    shuffled_list= np.array(course_list)
    print(shuffled_list)
    np.random.shuffle(shuffled_list)

    for time in shuffled_list:
        time[1] = time[1].replace(' ', '')  # 각 각의당 시간대 문자열에서 공백 제거

    return MakeTimeTable(min,max,shuffled_list)


def MakeTimeTable(min_credit, max_credit, shuffled_list):
    for i in range(20):
        total_leccredit = 0
        np.random.shuffle(shuffled_list)
        f_lecs = []
        f_lecs.append(shuffled_list[len(shuffled_list) - 1])
        total_leccredit+=int(f_lecs[0][2])
        for lecture in shuffled_list:
            if (total_leccredit < min_credit):
                if (Compare(lecture[1].split(','), lecture[0], f_lecs)):
                    f_lecs.append(lecture)
                    total_leccredit += int(lecture[2])
            elif (total_leccredit == max_credit):
                combination.append(copy.deepcopy(f_lecs))
                break
            elif (total_leccredit >= min_credit):
                combination.append(copy.deepcopy(f_lecs))
                # print(combination)
                #print(lecture)
                if (Compare(lecture[1].split(','), lecture[0], f_lecs)):
                    f_lecs.append(lecture)
                    total_leccredit += int(lecture[2])
                else:
                    break

            else:
                break
    return Dup_func(combination)



def Compare(timelist, lecname, f_lecs):
    compare_list = np.array(f_lecs)
    #print(lecname + ' ' + str(timelist))
    lecname_list = compare_list[:, 0]
    for name in lecname_list:
        if name in lecname:
            #print("this lecture " + lecname + ' duplicated')
            return False
    if any(lecname in c for c in lecname_list):
        #print("this lecture " + lecname + ' duplicated')
        return False
    else:
        compare_list2 = compare_list[:, 1]  # 열만 추출함
        for time in timelist:
            if any(time in c for c in compare_list2):
                return False
            elif (time == time[0] + '1' or time == time[0] + '2'):
                if any(time[0] + 'A' in c for c in compare_list2):
                    return False
            elif (time == time[0] + '3' or time == time[0] + '4'):
                if any(time[0] + 'B' in c for c in compare_list2):
                    return False
            elif (time == time[0] + '4' or time == time[0] + '5'):
                if any(time[0] + 'C' in c for c in compare_list2):
                    return False
            elif (time == time[0] + '5'):
                if any(time[0] + 'C' in c for c in compare_list2):
                    return False
            elif (time == time[0] + '6' or time == time[0] + '7'):
                if any(time[0] + 'D' in c for c in compare_list2):
                    return False
            elif (time == time[0] + '7' or time == time[0] + '8'):
                if any(time[0] + 'E' in c for c in compare_list2):
                    return False
            elif (time == time[0] + 'A'):
                if any(time[0] + '1' in c for c in compare_list2):
                    return False
            elif (time == time[0] + 'A'):
                if any(time[0] + '2' in c for c in compare_list2):
                    return False
            elif (time == time[0] + 'B'):
                if any(time[0] + '3' in c for c in compare_list2):
                    return False
            elif (time == time[0] + 'B'):
                if any(time[0] + '4' in c for c in compare_list2):
                    return False
            elif (time == time[0] + 'C'):
                if any(time[0] + '4' in c for c in compare_list2):
                    return False
            elif (time == time[0] + 'C'):
                if any(time[0] + '5' in c for c in compare_list2):
                    return False
            elif (time == time[0] + 'D'):
                if any(time[0] + '6' in c for c in compare_list2):
                    return False
            elif (time == time[0] + 'D'):
                if any(time[0] + '7' in c for c in compare_list2):
                    return False
            elif (time == time[0] + 'E'):
                if any(time[0] + '7' in c for c in compare_list2):
                    return False
            elif (time == time[0] + 'E'):
                if any(time[0] + '8' in c for c in compare_list2):
                    return False
    #print(lecname + " will be added")
    return True
def Dup_func(combination):
    for comb in combination:
        Duplication_check(comb)
    PrintList()

def Duplication_check(comb):
    for Oneofresults in resultList:  # 시간표 조합들
        combination = np.array(comb)
        Oneofresult = np.array(Oneofresults)
        Oneofresult = Oneofresult[:, 0:2]
        comb1 = combination[:, 0:2]
        setOneofresult = set()
        for One in Oneofresult:
            setOneofresult.update(One)
        setComb = set()
        for com in comb1:
            setComb.update(com)
        if (setComb == (setComb & setOneofresult) and setOneofresult == (setComb & setOneofresult)):
            return False
    copycomb = copy.deepcopy(comb)
    resultList.append(copy.deepcopy(copycomb))
    lectime_list = []
    slectime = []
    comb = np.array(comb)
    for lectime in comb:
        lectime[1] = lectime[1].replace(' ', '')
        #print(lectime[1])
        slectime = lectime[1].split(',')
        for lec in slectime:
            lectime_list.append(lec)
    lectime_list.sort()
    print(lectime_list)
    print(comb)
    cohesion = cohesion_check(lectime_list)
    #print(resultList[0])
    cohesion_checked_list.append(cohesion)
    print(cohesion_checked_list)
    return True
def PrintList():
    cohesion_dict_list = {}
    for i in range(len(cohesion_checked_list)):
        cohesion_dict_list[i] = cohesion_checked_list[i]

    sorted_list = sorted(cohesion_dict_list.items(), key=operator.itemgetter(1))
    '''
    print(np.array(resultList[0]))
    print('-------------------------------')
    print('-------------------------------')
    print('-------------------------------')
    rlist=np.array(resultList)
    rrlist=np.array(rlist[0:3])
    print(rrlist)
    print('-------------------------------')
    print('-------------------------------')
    print('-------------------------------')
    for i in range(0, 3):
        print(sorted_list[i])
        print(np.array(resultList[i]))
    '''
    print('-------------------------------')
    print('-------------------------------')
    print('-------------------------------')
    print(sorted_list[0])
    print(np.array(resultList[0]))
    return np.array(resultList[0])

def cohesion_check(lectime_list):
    cohesion_degree = 0.0
    m_daytime = []
    tu_daytime = []
    w_daytime = []
    th_daytime = []
    f_daytime = []
    for lec in lectime_list:
        if (lec[0] == '월'):
            m_daytime.append(calc(lec[1:]))
        elif (lec[0] == '화'):
            tu_daytime.append(calc(lec[1:]))
        elif (lec[0] == '수'):
            w_daytime.append(calc(lec[1:]))
        elif (lec[0] == '목'):
            th_daytime.append(calc(lec[1:]))
        elif (lec[0] == '금'):
            f_daytime.append(calc(lec[1:]))
    m_daytime.sort()
    tu_daytime.sort()
    w_daytime.sort()
    th_daytime.sort()
    f_daytime.sort()
    for i in range(0, len(m_daytime) - 1):
        cohesion_degree += m_daytime[i + 1] - m_daytime[i]
    for i in range(0, len(tu_daytime) - 1):
        cohesion_degree += tu_daytime[i + 1] - tu_daytime[i]
    for i in range(0, len(w_daytime) - 1):
        cohesion_degree += w_daytime[i + 1] - w_daytime[i]
    for i in range(0, len(th_daytime) - 1):
        cohesion_degree += th_daytime[i + 1] - th_daytime[i]
    for i in range(0, len(f_daytime) - 1):
        cohesion_degree += f_daytime[i + 1] - f_daytime[i]
    return cohesion_degree


def calc(time_type):
    # print(type(time_type))
    if (isAlpha(time_type)):
        itype = ord(time_type)
        return float(itype)
    elif (isNumeric(time_type)):
        itype = int(time_type)
        itype = change(itype)
        return itype


def change(time):
    if (time == 1 or time == 2 or time == 3):
        time += 63
    elif (time == 4):
        time += 62.5
    elif (time == 5 or time == 6):
        time += 62
    elif (time == 7):
        time += 61.5
    else:
        time += 61
    return time


def isAlpha(time_type):
    p = re.compile('^[a-zA-z]*$')
    m = p.match(time_type)
    if m:
        result = 1
    else:
        result = 0
    return result


def isNumeric(time_type):
    p2 = re.compile('^[0-9]*$')
    m2 = p2.match(time_type)
    if m2:
        result = 1
    else:
        result = 0
    return result
generator(12,15,'컴퓨터공학과',2)
#MakeTimeTable(12,15,shuffled_list)
'''
for comb in combination:
    Duplication_check(comb)
cohesion_dict_list = {}
for i in range(len(cohesion_checked_list)):
    cohesion_dict_list[i]=cohesion_checked_list[i]

sorted_list = sorted(cohesion_dict_list.items(), key=operator.itemgetter(1))
for i in range(0, 3):
    print(sorted_list[i])
    print(np.array(resultList[i]))
'''
