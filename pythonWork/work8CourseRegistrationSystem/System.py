#Person类
class Person:
    #姓、名、性别、生日四个域
    def __init__(self,firstname,lastname,gender,birthday):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.birthday = birthday
    #以标题格式返回姓
    def get_lastname(self):
        return self.lastname.title()
    #以标题格式返回名
    def get_firstname(self):
        return self.firstname.title()
#student类
class student(Person):
    #继承父类属性外，还有学生号和部门两个属性
    def __init__(self, firstname, lastname, gender, birthday, studentNumber, department):
        super().__init__(firstname, lastname, gender, birthday)
        self.studentNumber = studentNumber
        self.department = department
        self.courses = course.values()
        self.GPA = Credits.values()

    def get_courses(self):
        return self.courses
    
    def get_GPA(self):
        return self.GPA
#courses类
class courses():
    #课程编号，课程名，部门，学分，时间和地点
    def __init__(self,courseid,coursename,department,credits,time,location):
        self.courseid = courseid
        self.coursename = coursename
        self.department = department
        self.credits = credits
        self.time = time
        self.location = location
#courses_management类
class courses_management(courses):
    #继承父类属性外，还有学生成绩属性
    def __init__(self, courseid, coursename, department, credits, time, location,studentsgrades):
        super().__init__(courseid, coursename, department, credits, time, location)
        self.students = Students.values()
        self.studentsgrades = studentsgrades

    def addstudents(self):
        return self.students
    #计算GPA
    def setgrades(self):
        for i,j in Credits , Grades:
            self.credits = sum(i*j)/sum(i)
        return self.credits
    #打印课程信息
    def returninfor(self):
        print(f"courseid: {self.courseid},coursename: {self.coursename}")

#课程，学分和成绩，键全部为课程编号
course = {}
Credits = {}
Grades = {}
#创建课程对象，储存对象到字典
def course_registration():
    server2_1 = input('Please enter your course number: ')
    server2_2 = input('Please enter your course name: ')
    server2_3 = input("Please enter your course's department: ")
    server2_4 = input('Please enter your course cord: ')
    server2_5 = input('Please enter your course time: ')
    server2_6 = input('Please enter your course location: ')
    my_course = courses(server2_1,server2_2,server2_3,server2_4,server2_5,server2_6)
    while True:
        server2_7 = input("\nPlease check it and preass 'y' to end or 'n' to correct('q' to quit): ")
        if server2_7 =='y':
            course[server2_1] = my_course
            Credits[server2_1] = server2_4
            break
        elif server2_3 == 'n':
            course_registration()
        elif server2_3 == 'q':
            break
        else:
            continue
#学生，键为学生编号
Students = {}
#创建学生对象，储存到字典
def user_registration():
    first_name = input('Please enter your firstname: ')
    last_name = input('Please enter your lastname: ')
    user_gender = input('Please enter your gender: ')
    user_birthday = input('Please enter your birthday(Y/M/D) ')
    student_number = input('Please enter your studentnumber: ')
    stu_department = input('Please enter your department: ')
    my_infor = first_name + last_name
    my_infor = student(first_name,last_name,user_gender,user_birthday,student_number,stu_department)
    print('Your information is:\n' 
        'lastname: '+my_infor.get_lastname()+
        '\nfirstname: '+ my_infor.get_firstname()+
        '\ngender'+my_infor.gender+
        '\nbirthday'+my_infor.birthday
        )
    while True:
        server1_1 = input("Please check your information and preass 'y' to end or 'n' to correct: ")
        if server1_1 == 'y':
            Students[student_number] = my_infor
            break
        elif server1_1 == 'n':
            user_registration()
        else:
            continue
#给课程分数/修改和删除课程
def course_management():
    print('The following courses have been registrated:\n')
    for key,value in course.items():
        print(key + value)
    server3_0 = input('\nPlease enter your option(g to entetr grades & c to manage course): ')
    if server3_0 == 'g':
        while True:
            server3_0_1 = input('Please enter your course number(q to quit): ')
            server3_0_2 = input('Please enter your grades(q to quit): ')
            if server3_0_1 != 'q':
                if server3_0_2 != 'q':
                    Grades[server3_0_1] = server3_0_2
                else:
                    return
    elif server3_0 == 'c':
        while True:
            server3 = input("Press 'c' to correct or 'd' to delete('q' to quit): ")
            if server3 == 'c':
                server3_1 = input('Please enter your course number to correct it: ')
                server3_2 = input('The correct course number is: ')
                server3_3 = input('The correct course name is: ')
                course[server3_2] = server3_3
                del course[server3_1]
                print('Your course have been corrected!')
            elif server3 == 'd':
                server3_4 = input('Please enter the course number that you want to delete: ')
                del course[server3_4]
                print('Your course have been delete!')
            elif server3 == 'q':
                break
            else:
                continue
#打印课程或课程表
def course_schedule():
    while True:
        server4 = input('Please enter the course number you want to select(a for all courses & q to quit): ')
        if server4 == 'a':
            for key,value in course.items():
                print(key + value)
            break
        elif server4 == 'q':
            return
        else:
            boolean1 = server4 in course.values()
            if boolean1 == True:
                list(course.keys())[list(course.values()).index(server4)]
            elif boolean1 == False:
                print('wrong number!Please enter again.')
                continue
#打印单个或全部学生信息
def student_infor():
    for key,value in Students.items():
        print(key + value)
    while True:
        server5 = input('Please enter the student number you want to select: ')
        boolean1 = server5 in Students.values()
        if boolean1 == True:
            list(Students.keys())[list(Students.values()).index(server5)]
        elif boolean1 == False:
            print('wrong number!Please enter again.')
            continue
#返回学生成绩
def user_grades():
    if Credits:
        for i in Credits.values():
            print(sum(i))
    else:
        print('Your credits is empty')
    if Grades:
        for i in Grades.values():
            print(i)
    else:
        print('Your grades is empty')
#初始界面
def begin():
    while True:
        print('############################################################################\n'
                '###############  Welcome to our course registration system! ################\n'
                '############################################################################\n'
                '###############     1. Course registration for new user     ################\n'
                '###############     2. Modify user course registration      ################\n'
                '###############     3. Course management                    ################\n'
                '###############     4. Print selected course schedule       ################\n'
                '###############     5. Query grades and credits             ################\n'
                '###############     6. Exit                                 ################\n'
                '##########################################################################')
        server1 = input("Please enter your option:")
        if server1 == '1':
            user_registration()
        elif server1 == '2':
            course_registration()
        elif server1 == '3':
            course_management()
        elif server1 == '4':
            course_schedule()
        elif server1 == '5':
            user_grades()
        elif server1 == '6':
            break
        else:
            continue

begin()


"""
总结:
1.在子类继承父类属性时，无需初始化父类属性，但要初始化添加的子类属性
2.当属性不设置域时，在使用时自动返回属性 
eg:object = class(property)
print(object.property)
3.对象可以用字典储存信息，以某一属性为索引值
4. boolean1 = value in dic.values() 用来判断字典中是否有该索引值
5.for key,value in dic.items():
    print(key + value) 打印字典
6.dic[key] = value 添加键值对
"""