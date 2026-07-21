from abc import ABC, abstractmethod
import json

# 书籍类
class Book:

    def __init__(self, book_id, title, author, total_num):
        self.book_id = book_id       # 图书编号
        self.title = title           # 书籍标题
        self.author = author         # 作者
        self.total_num = total_num   # 总数量
        self.__available_num = total_num  # 可借数量

    def borrow_book(self):
        if self.__available_num > 0:
            self.__available_num -= 1
            return True
        else:
            print("抱歉，该书籍已借完。")
            return False

    def return_book(self):
        self.__available_num += 1
        return True

    def get_available_num(self):
       return self.__available_num

class Member(ABC):

    def __init__(self, member_id, name, password):
        self.member_id = member_id  # 会员编号
        self.name = name            # 会员姓名
        self.__password = password   # 会员密码
        self.__borrowed_books = []   # 借阅的书籍列表

    def borrow_book(self, book):
        # 判断会员是否已达到了借阅上限

        if len(self.__borrowed_books) >= self.get_max_books():
            print(f"{self.name} 已达到借阅上限。")
            return False

        if book.borrow_book():
            self.__borrowed_books.append(book)
            print(f"{self.name} 成功借阅了《{book.title}》。")
            return True
        else:
            print(f"{self.name} 借阅《{book.title}》失败。")
            return False

    def return_book(self, book):

        # 判断会员是否借阅了该书籍
        if book in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book)
            print(f"{self.name} 成功归还了《{book.title}》。")
            return True
        else:
            print(f"{self.name} 没有借阅《{book.title}》，无法归还。")
            return False

    def get_password(self):
        return self.__password

    def get_borrowed_books(self):
        return self.__borrowed_books

    # 抽象方法：子类实现
    @abstractmethod
    def get_max_books(self) -> int:
        pass


# 普通会员类
class NormalMember(Member):

    def get_max_books(self) -> int:
        return 3

# VIP会员类
class VipMember(Member):

    def __init__(self, member_id, name, password, vip_level):
        super().__init__(member_id, name, password)
        self.vip_level = vip_level

    def get_max_books(self) -> int:
        return 6 + self.vip_level

# 图书馆管理系统
class LibrarySystem:

    def __init__(self):
        self.books = {}     # 书籍列表 --> {"AI001": Book对象, "AI002": Book对象}
        self.members = {}   # 会员列表 --> {"N001": NormalMember对象, "V001": VipMember对象}
        self.current_member: Member|None = None

        # 加载书籍对象
        self.__load_books_data()
        self.__load_members_data()

    def __load_books_data(self):
        # 加载resources/books.json文件中的书籍数据
        with open("resources/books.json", "r", encoding="utf-8") as f:
            books_data = json.load(f)
            for book_data in books_data:
                book = Book(
                    book_id=book_data["编号"],
                    title=book_data["标题"],
                    author=book_data["作者"],
                    total_num=book_data["数量"]
                )
                self.books[book.book_id] = book
            print("书籍数据加载完成。")

    def __load_members_data(self):
        # 加载resources/members.json文件中的会员数据
        with open("resources/members.json", "r", encoding="utf-8") as f:
            members_data = json.load(f)
            for member_data in members_data:
                if member_data["卡号"].startswith("N"):
                    member = NormalMember(
                        member_id=member_data["卡号"],
                        name=member_data["姓名"],
                        password=member_data["密码"]
                    )
                elif member_data["卡号"].startswith("V"):
                    member = VipMember(
                        member_id=member_data["卡号"],
                        name=member_data["姓名"],
                        password=member_data["密码"],
                        vip_level=member_data["会员等级"]
                    )
                else:
                    continue
                self.members[member.member_id] = member
            print("会员数据加载完成。")

    def login(self):
        while True:
            print("欢迎使用图书管理系统，请登录：")
            member_id = input("请输入会员卡号：")
            # 判断会员卡号是否存在
            if member_id not in self.members:
                print("会员登入失败，会员卡号不存在！")
                continue

            password = input("请输入密码：")
            # 判断密码是否正确
            member = self.members[member_id]
            if member.get_password() == password:
                self.current_member = member
                print(f"{member.name} 登录成功。")
                return True
            else:
                print("会员登入失败，密码错误！")
                continue

    def run(self):
        if self.login():
            while True:
                self.__print_menu()
                choice = int(input("请输入您的选择："))
                match choice:
                    case 1:
                        self.__borrow_book()
                    case 2:
                        self.__return_book()
                    case 3:
                        self.__view_borrowed_books()
                    case 4:
                        print("bey bey~~。")
                        break
                    case _:
                        print("无效的选择，请重新输入。")


    @staticmethod
    def __print_menu():
        print("====================图书管理系统菜单========================")
        print("=                   1.借阅图书                            =")
        print("=                   2.归还图书                            =")
        print("=                   3.查看已借阅图书                       =")
        print("=                   4.退出系统                            =")
        print("==========================================================")

    def __borrow_book(self):
        # 1. 展示出当前图书馆的图书列表
        for book in self.books.values():
            print(f"编号：{book.book_id}，标题：{book.title}，作者：{book.author}，总数量：{book.total_num}，可借数量：{book.get_available_num()}")
        # 2. 获取用户输入的图书编号，执行借书操作
        book_id = input("请输入要借阅的图书编号：")
        # 3. 根据图书编号查找图书
        if book_id in self.books:
            book = self.books[book_id]
            # 4. 执行借书操作
            if book.get_available_num() > 0:
                if self.current_member.borrow_book(book):
                    print("借书成功。")
                else:
                    print("借书失败。")
            else:
                print("该图书已借完。")
        else:
            print("图书编号不存在。")

    def __return_book(self):
        # 展示出当前会员的借阅列表
        borrowed_books = self.current_member.get_borrowed_books()
        print("当前会员的借阅列表：")
        for book in borrowed_books:
            print(f"编号：{book.book_id}，标题：{book.title}，作者：{book.author}")
        # 获取用户输入的图书编号，执行还书操作
        book_id = input("请输入要归还的图书编号：")
        # 根据图书编号查找图书
        if book_id in self.books:
            book = self.current_member.return_book(self.books[book_id])
            print("归还成功。")
        else:
            print("还书失败，图书编号不存在。")

    def __view_borrowed_books(self):
        # 展示出当前会员的借阅列表
        borrowed_books = self.current_member.get_borrowed_books()
        print("当前会员的借阅列表：")

        if len(borrowed_books) > 0:
            print("以借阅的图书")
            for book in borrowed_books:
                print(f"编号：{book.book_id}，标题：{book.title}，作者：{book.author}")
        else:
            print("当前没有借阅任何图书。")


if __name__ == '__main__':
    # m = NormalMember("N001", "张三", "123456")
    # print(m.get_max_books())

    library = LibrarySystem()
    library.run()