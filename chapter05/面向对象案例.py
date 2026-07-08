# 学生类
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math} | 英语：{self.english}"

    # 修改学生的成绩
    def update_score(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english


class EduManagement:

    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        # 在校学生的管理信息
        self.student_list = []

    # 添加学生成绩
    def add_student(self):
        name = input("请输入学生姓名：")

        # 判断学生姓名是否存在，如果存在，则添加失败(不能重复添加)
        for student in self.student_list:
            if student.name == name:
                print("该学生已经存在，添加失败！")
                return

        chinese = int(input("请输入学生语文成绩："))
        math = int(input("请输入学生数学成绩："))
        english = int(input("请输入学生的英语成绩："))

        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            student = Student(name, chinese, math, english)
            self.student_list.append(student)
            print("添加学生信息成功~")
        else:
            print("输入的成绩必须在0到100之间！")

    # 修改学生成绩
    def update_student(self):
        name = input("请输入学生姓名：")

        # 根据学生姓名查找学生成绩
        for student in self.student_list:
            if student.name == name:
                print(f"当前学生成绩：{student}")

                chinese = int(input("请输入修改该学生语文成绩："))
                math = int(input("请输入修改该学生数学成绩："))
                english = int(input("请输入修改该学生的英语成绩："))

                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    student.update_score(chinese, math, english)
                    print("修改成绩成功！")
                    print(f"修改后的成绩：{student}")
                else:
                    print("输入的成绩必须在0到100之间！")
            else:
                print("学生没有找到，修改失败！")

    def delete_student(self):
        name = input("请输入学生姓名：")

        # 根据学生姓名查找学生成绩
        for student in self.student_list:
            if student.name == name:
                self.student_list.remove(student)
                print("学生信息删除成功~")
            else:
                print("学生没有找到，删除失败！")

    # 查询学生成绩
    def query_student(self):
        name = input("请输入学生姓名：")

        # 根据学生姓名查找学生成绩
        for student in self.student_list:
            if student.name == name:
                print(f"学生信息：{student}")
        print("学生没有找到，查询失败！")

    # 展示全部学生成绩
    def list_student(self):
        for student in self.student_list:
            print(student)

    #运行系统
    def run(self):
        print(f"欢迎使用教务管理系统 V{EduManagement.system_version}")

        while True:
            print()
            print("##################################################################################")
            print("1.添加学生成绩  2.修改学生成绩  3.删除学生成绩  4.查询学生成绩  5.查询所有学生成绩  6.推出系统")
            print("##################################################################################")
            print()

            choice = input("请选择要执行的操作，输入1~6:")
            match choice:
                case "1":
                    self.add_student()
                case "2":
                    self.update_student()
                case "3":
                    self.delete_student()
                case "4":
                    self.query_student()
                case "5":
                    self.list_student()
                case "6":
                    print("再见")
                    break
                case _:
                    print("输入错误，请重新输入！！！")

if __name__ == '__main__':
    s1 = Student("万林", 90, 88, 92)
    print(s1)

    stu_manager = EduManagement()

    stu_manager.run()