import csv
import os
import cv2 as cv
import pandas as pd
from classself import userchange as user

userFileName = 'D:/VScode/vs project/game/file.csv'
skillFileName = 'D:/VScode/vs project/game/skill.csv'
userPhotoName = 'D:/VScode/vs project/game/user.png'

def read_data(file):  # dataframe构造二元数组
    data = pd.read_csv(file, encoding='gb18030')
    data = pd.DataFrame(data)
    print(data)


def return_csv_list(file):  # csv转化为列表中字典换行输出
    with open(file, 'rt') as csvfile:
        reader = csv.DictReader(csvfile)
        column = [row for row in reader]
    for i in range(len(column)):
        print(column[i], '\n', end='')


def write_data(data, file):  # 写入多行数据
    with open(file, 'a', newline='') as f:
        write = csv.writer(f, dialect='excel')
        write.writerows(data)

def rewrite_data_user(name,data): #重写数据
    user_cleardel(name)
    write_data([(name,data)],userFileName)

def read_csv_loc(file, read):  # 返回某一属性的索引值
    with open(file, 'rt') as csvfile:
        reader = csv.DictReader(csvfile)
        column = [row['属性名'] for row in reader]
        location = column.index(read)

def return_csv_data(location): #返回某一属性的值
    with open(userFileName,'rt') as csvfile:
        reader = csv.DictReader(csvfile)
        column = [row['属性值'] for row in reader]
        num = int(column[location])

def read_csv_cell(file, cell1, cell2):  # 查询指定单元格
    data = pd.read_csv(file, encoding='gb18030')
    num = data[cell1].loc[cell2]
    print(num)


def read_picture():  # 读取照片
    img = cv.imread(userPhotoName, 1)
    cv.namedWindow('IMG')
    cv.imshow("IMG", img)
    cv.waitKey()
    cv.destroyAllWindows()


def user_add():  # 添加用户属性
    add1 = input('输入属性名: ')
    add2 = input('输入属性值: ')
    add = [(add1, add2)]
    write_data(add, userFileName)
    read_data(userFileName)

def user_cleardel(delete):
    data = pd.read_csv(userFileName, encoding='gb18030')
    user2 = user(userFileName,delete)
    user2._pptloc_(userFileName,delete)
    location = int(user2.userPPTloc)
    data_new = data.drop([location], axis=0)  # axis=0按行，axis=1按列
    data_new.to_csv(userFileName, index=False, encoding='gb18030')

def user_del():  # 删除用户属性
    data = pd.read_csv(userFileName, encoding='gb18030')
    read_data(userFileName)
    lenfile = len(open(userFileName).readlines())
    # 通过比较输入和实际行数避免异常
    while True:
        delete = input('输入删除的属性(回车键退出): ')
        try:
            user1 = user(userFileName,delete)
            user1._pptloc_(userFileName,delete)
            location = int(user1.PPTloc)
            #if delete.isdigit() == True:判断能否转换为数字
            if location <= lenfile:
                data_new = data.drop([location], axis=0)  # axis=0按行，axis=1按列
                data_new.to_csv(userFileName, index=False, encoding='gb18030')
                print('删除成功！')
            elif lenfile == 1:
                print('不存在属性，请添加属性')
            else:
                print('不存在此属性！请重试')
        except ValueError:
            print('不存在此属性！')
            return


def user_infor():  # 用户信息初始化以及读取用户信息
    # 判断csv文件是否为空，try…except跳过异常
    try:
        if os.path.getsize(userFileName):
            # read_picture() 这里添加头像显示
            # 读取csv文件
            read_data(userFileName)
            while True:
                user3 = input('按a添加属性，d删除属性，q退出: ')
                if user3 == 'a':
                    user_add()
                elif user3 == 'd':
                    user_del()
                elif user3 == 'q':
                    break
        else:
            user1 = input('输入你的ID: ')
            user2 = input('创建时间：')
            user = [('ID', user1), ('构图', 0), ('透视', 0), ('创建时间', user2)]
            df = pd.read_csv(userFileName, header=None, names=[
                            '属性名', '属性值'], encoding='gb18030')  # 添加表头
            df.to_csv(userFileName, index=False, encoding='gb18030')  # 写入表头
            write_data(user, userFileName)
            print("创建人物成功，已初始化属性。")
            read_data(userFileName)
    except FileNotFoundError:
        print('无法查找到文件！请检查路径')


def skills_add():
    skill1 = input('技能名称: ')
    skill2 = input('关联属性: ')
    skill3 = input('成长系数: ')
    skill4 = input('成长属性: ')
    skill5 = input('成长值: ')
    skill6 = input('成长周期: ')
    skill7 = input('总时长: ')
    skill = [(skill1, skill2, skill3, skill4, skill5, skill6, skill7)]
    write_data(skill, skillFileName)
    read_data(skillFileName)


def skills_del():
    data = pd.read_csv(skillFileName, encoding='gb18030')
    read_data(skillFileName)
    lenfile = len(open(skillFileName).readlines())
    # 通过比较输入和实际行数避免异常
    while True:
        delete = input('输入删除的一行技能(q退出): ')
        if delete.isdigit() == True:  # 判断能否转换为数字
            delete = int(delete)
            if delete <= lenfile:
                data_new = data.drop([delete], axis=0)
                data_new.to_csv(skillFileName, index=False, encoding='gb18030')
            elif lenfile == 1:
                print('不存在技能，请添加技能')
            else:
                print('不存在此行技能！请重试')
        else:
            if delete == 'q':
                return
            else:
                print('请输入数字字符！')
                continue


def skills_list():
    # 判断csv文件是否为空，try…except跳过异常
    if os.path.getsize(skillFileName):
        while True:
            read_data(skillFileName)
            skillserver = input('输入a添加技能，d删除技能，q退出: ')
            if skillserver == 'a':
                skills_add()
            elif skillserver == 'd':
                skills_del()
            elif skillserver == 'q':
                break
            else:
                continue
    else:
        print('你还没有学习技能！')
        while True:
            skill2 = input('输入a来添加技能，q退出: ')
            if skill2 == 'a':
                skills_add()
                df = pd.read_csv(skillFileName, header=None, names=[
                                '技能名', '关联属性', '成长系数', '成长属性', '成长值', '记录周期', '总时长'], encoding='gb18030')
                df.to_csv(skillFileName, index=False, encoding='gb18030')
                print('技能添加成功！')
                read_data(skillFileName)
            elif skill2 == 'q':
                break
            else:
                continue


def training_instance():
    name = input('副本名称: ')

def task_list():
    pass



def information_table():
    pass

# 初始界面


def begin():
    while True:
        print('###################################################\n'
            '###############  Welcome to paint! ################\n'
            '###################################################\n'
            '###############     1.角色信息      ################\n'
            '###############     2.技能列表      ################\n'
            '###############     3.训练副本      ################\n'
            '###############     4.任务列表      ################\n'
            '###############     5.统计信息      ################\n'
            '###############     6.退出          ################\n'
            '####################################################')
        server1 = input("输入你的选项: ")
        if server1 == '1':
            user_infor()
        elif server1 == '2':
            skills_list()
        elif server1 == '3':
            training_instance()
        elif server1 == '4':
            task_list()
        elif server1 == '5':
            information_table()
        elif server1 == '6':
            break
        else:
            continue

begin()

"""
总结：
1.try……except也可以用于处理异常
2.读写csv文件需要用enconding = 'gb18030'
3.if os.path.getsize(fileName):  判断filename文件是否为空 T为不空F为空
4.读取写入csv文件的方式 添加表头 按行按列添加和删除数据 cv2读取本地照片
5.使用属性获取数据 可以使函数调用另一个函数的变量
"""
