import pymysql
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import tkinter.messagebox as messagebox
import tkinter as tk

class FrameManager:
    def __init__(self, root):
        self.root = root
        self.frames = {}

    def add_frame(self, frame_class, name):
        frame = frame_class(self.root)
        self.frames[name] = frame


        333333
        

    def show_frame(self, name):
        frame = self.frames[name]
        frame.pack(fill=tk.BOTH, expand=True)
        frame.tkraise()
        self.root.attributes('-fullscreen', True)  # 强制全屏模式

    def hide_frame(self, name):
        frame = self.frames[name]
        frame.pack_forget()
# 开始界面
class StartPage:
    def __init__(self, parent_window):
        self.window = parent_window
        self.window.title('大学信息管理系统')
        self.window.geometry('1920x1080')  # 这里的乘是小x

        # 销毁其他子窗口
        for widget in self.window.winfo_children():
            widget.destroy()

        label = Label(self.window, text="大学信息管理系统", font=("Verdana", 20))
        label.pack(pady=100)  # pady=100 界面的长度

        Button(self.window, text="管理员登录", font=tkFont.Font(size=16), command=lambda: AdminPage(self.window), width=30,
               height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="学生登录", font=tkFont.Font(size=16), command=lambda: StudentPage(self.window), width=30,
               height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text='退出系统', height=2, font=tkFont.Font(size=16), width=30, command=self.window.destroy,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()

# 管理员登陆页面
class AdminPage:
    def __init__(self, parent_window):
        self.window = parent_window
        self.window.title('管理员登陆页面')
        self.window.geometry('1920x1080')  # 这里的乘是小x

        # 销毁其他子窗口
        for widget in self.window.winfo_children():
            widget.destroy()

        label = tk.Label(self.window, text='管理员登陆', bg='white', font=('Verdana', 20), width=30, height=2)
        label.pack()

        Label(self.window, text='管理员账号：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_username = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.admin_username.pack()

        Label(self.window, text='管理员密码：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_pass = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.admin_pass.pack()

        Button(self.window, text="登陆", width=8, font=tkFont.Font(size=12), command=self.login).pack(pady=40)
        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back).pack()

    def login(self):
        admin_pass = None

        # 数据库操作 查询管理员表
        db = pymysql.connect(host="localhost", user="root", password="a1596s1596", database="school", port=3306)
        cursor = db.cursor()
        sql = "SELECT * FROM admin_login WHERE admin_id = '%s'" % (self.admin_username.get())
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                admin_pass = row[1]
        except:
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        db.close()

        if self.admin_pass.get() == admin_pass:
            AdminManage(self.window)  # 进入管理员操作界面
        else:
            messagebox.showinfo('警告！', '用户名或密码不正确！')

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口

# 学生登陆页面
class StudentPage:
    def __init__(self, parent_window):
        self.window = parent_window
        self.window.title('学生登陆页面')
        self.window.geometry('1920x1080')  # 这里的乘是小x

        # 销毁其他子窗口
        for widget in self.window.winfo_children():
            widget.destroy()

        label = tk.Label(self.window, text='学生登陆', bg='white', font=('Verdana', 20), width=30, height=2)
        label.pack()

        Label(self.window, text='学生账号：', font=tkFont.Font(size=14)).pack(pady=25)
        self.student_id = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.student_id.pack()

        Label(self.window, text='学生密码：', font=tkFont.Font(size=14)).pack(pady=25)
        self.student_pass = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.student_pass.pack()

        Button(self.window, text="登陆", width=8, font=tkFont.Font(size=12), command=self.login).pack(pady=40)
        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back).pack()
    
    def login(self):
        student_pass = None

        # 数据库操作 查询学生表
        db = pymysql.connect(host="localhost", user="root", password="a1596s1596", database="school", port=3306)
        cursor = db.cursor()
        sql = "SELECT * FROM student_login WHERE stu_id = '%s'" % (self.student_id.get())
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                student_pass = row[1]
        except:
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        db.close()

        if self.student_pass.get() == student_pass:
            StudentView(self.window, self.student_id.get())  # 进入学生信息查看界面
        else:
            messagebox.showinfo('警告！', '用户名或密码不正确！')

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口
# 管理员操作界面
class AdminManage:
    def __init__(self, parent_window):
        self.window = parent_window
        self.window.geometry('1920x1080')  # 这里的乘是小x
        self.window.title('管理员操作界面')
        # 销毁其他子窗口
        for widget in self.window.winfo_children():
            widget.destroy()

        self.frame = tk.Frame(self.window)
        self.frame.pack(fill=tk.BOTH, expand=True)

        label = Label(self.frame, text="请选择操作", font=("Verdana", 20))
        label.pack(pady=100)  # pady=100 界面的长度

        Button(self.frame, text="学生信息", font=tkFont.Font(size=16), command=lambda: self.show_frame(Student), width=30,
               height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.frame, text="课程信息", font=tkFont.Font(size=16), command=lambda: self.show_frame(Lesson), width=30,
               height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.frame, text="选课信息", font=tkFont.Font(size=16), command=lambda: self.show_frame(Learn), width=30,
               height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.frame, text='退出系统', height=2, font=tkFont.Font(size=16), width=30, command=self.window.destroy,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()

    def show_frame(self, FrameClass):
        for widget in self.window.winfo_children():
            widget.destroy()
        FrameClass(self.window)

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口

# 学生信息界面
class Student:
    def __init__(self, parent_window):
        self.window = parent_window
        self.window.geometry('1920x1080')
        self.window.title('学生信息')

        self.frame_left_top = tk.Frame(width=700, height=200)
        self.frame_right_top = tk.Frame(width=700, height=200)
        self.frame_center = tk.Frame(width=700, height=400)
        self.frame_bottom = tk.Frame(width=700, height=200)

        # 定义下方中心列表区域
        self.columns = ("学号", "姓名", "性别", "学院")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vbar.set)

        self.tree.column("学号", width=100, anchor='center')
        self.tree.column("姓名", width=50, anchor='center')
        self.tree.column("性别", width=50, anchor='center')
        self.tree.column("学院", width=300, anchor='center')

        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.id = []
        self.name = []
        self.gender = []
        self.college = []
        self.update_treeview()

        for col in self.columns:
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        self.top_title = Label(self.frame_left_top, text="学生信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_college = StringVar()

        self.right_top_id_label = Label(self.frame_left_top, text="学号：", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)
        self.right_top_id_entry.grid(row=1, column=1)
        self.right_top_name_label = Label(self.frame_left_top, text="姓名：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)
        self.right_top_name_entry.grid(row=2, column=1)
        self.right_top_gender_label = Label(self.frame_left_top, text="性别：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_gender, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=3, column=0)
        self.right_top_gender_entry.grid(row=3, column=1)
        self.right_top_college_label = Label(self.frame_left_top, text="学院：", font=('Verdana', 15))
        self.right_top_college_entry = Entry(self.frame_left_top, textvariable=self.var_college, font=('Verdana', 15))
        self.right_top_college_label.grid(row=4, column=0)
        self.right_top_college_entry.grid(row=4, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))

        self.tree.bind('<Button-1>', self.click)
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建学生信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中学生信息', width=20, command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中学生信息', width=20, command=self.del_row)
        self.right_top_button4 = ttk.Button(self.frame_right_top, text='搜索学生信息', width=20, command=self.search_student)

        # 搜索框
        self.search_var = StringVar()
        self.search_entry = Entry(self.frame_right_top, textvariable=self.search_var, font=('Verdana', 15))
        self.search_entry.grid(row=0, column=0, pady=10)
        self.search_button = ttk.Button(self.frame_right_top, text='搜索', command=self.search_student)
        self.search_button.grid(row=0, column=1, padx=10, pady=10)

        # 位置设置
        self.right_top_title.grid(row=0, column=0, pady=10)
        self.right_top_button1.grid(row=1, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button4.grid(row=4, column=0, padx=20, pady=10)

        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(False)
        self.frame_right_top.grid_propagate(False)
        self.frame_center.grid_propagate(False)
        self.frame_bottom.grid_propagate(False)

        self.frame_left_top.tkraise()
        self.frame_right_top.tkraise()
        self.frame_center.tkraise()
        self.frame_bottom.tkraise()

        self.window.protocol("WM_DELETE_WINDOW", self.back)
        self.window.mainloop()

    def update_treeview(self):
        self.id.clear()
        self.name.clear()
        self.gender.clear()
        self.college.clear()

        db = pymysql.connect(host="localhost", user="root", password="a1596s1596", database="school", port=3306)
        cursor = db.cursor()
        sql = "SELECT stu_id, stu_name, stu_gender, stu_college FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()
        db.close()

        for row in results:
            self.id.append(row[0])
            self.name.append(row[1])
            self.gender.append(row[2])
            self.college.append(row[3])

        for i in range(len(self.id)):
            self.tree.insert('', 'end', values=(self.id[i], self.name[i], self.gender[i], self.college[i]))

    def search_student(self):
        search_term = self.search_var.get()
        self.tree.delete(*self.tree.get_children())

        db = pymysql.connect(host="localhost", user="root", password="a1596s1596", database="school", port=3306)
        cursor = db.cursor()
        sql = "SELECT stu_id, stu_name, stu_gender, stu_college FROM student WHERE stu_id LIKE %s OR stu_name LIKE %s"
        cursor.execute(sql, ('%' + search_term + '%', '%' + search_term + '%'))
        results = cursor.fetchall()
        db.close()

        for row in results:
            self.tree.insert('', 'end', values=(row[0], row[1], row[2], row[3]))

    def back(self):
        AdminManage(self.window)

    def click(self, event):
        self.col = self.tree.identify_column(event.x)
        self.row = self.tree.identify_row(event.y)

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.var_name.set(self.row_info[1])
        self.var_gender.set(self.row_info[2])
        self.var_college.set(self.row_info[3])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id, font=('Verdana', 15))
        print('')

    def tree_sort_column(self, tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))

    def new_row(self):
        print('123')
        print(self.var_id.get())
        print(self.id)
        if str(self.var_id.get()) in self.id:
            messagebox.showinfo('警告！', '该学号已被占用！')
        else:
            if self.var_id.get() != '' and self.var_name.get() != '' and self.var_gender.get() != '':
                db = pymysql.connect(host="localhost", user="root", password="a1596s1596", database="school", port=3306)
                cursor = db.cursor()
                if self.var_college.get() != '':
                    sql = "INSERT INTO student(stu_id, stu_name, stu_gender, stu_adm_time, stu_college) \
                           VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(sql, (self.var_id.get(), self.var_name.get(), self.var_gender.get(), '2022-05-25', self.var_college.get()))
                else:
                    sql = "INSERT INTO student(stu_id, stu_name, stu_gender, stu_adm_time, stu_college) \
                           VALUES (%s, %s, %s, %s, '未划分学院')"
                    cursor.execute(sql, (self.var_id.get(), self.var_name.get(), self.var_gender.get(), '2022-05-25'))

                try:
                    db.commit()
                    messagebox.showinfo('提示！', '插入成功！')
                    self.id.append(self.var_id.get())
                    self.name.append(self.var_name.get())
                    self.gender.append(self.var_gender.get())
                    self.college.append(self.var_college.get())
                    self.tree.insert('', 'end', values=(self.var_id.get(), self.var_name.get(), self.var_gender.get(), self.var_college.get()))
                    self.tree.update()
                except:
                    db.rollback()
                    messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()
            else:
                messagebox.showinfo('警告！', '请填写必要学生数据')

    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res:
            if self.var_id.get() == self.row_info[0]:
                db = pymysql.connect(host="localhost", user="root", password="a1596s1596", database="school", port=3306)
                cursor = db.cursor()
                sql = "UPDATE student SET stu_name = %s, stu_gender = %s, stu_college = %s WHERE stu_id = %s"
                try:
                    cursor.execute(sql, (self.var_name.get(), self.var_gender.get(), self.var_college.get(), self.var_id.get()))
                    db.commit()
                    messagebox.showinfo('提示！', '更新成功！')
                    id_index = self.id.index(self.row_info[0])
                    self.name[id_index] = self.var_name.get()
                    self.gender[id_index] = self.var_gender.get()
                    self.college[id_index] = self.var_college.get()

                    self.tree.item(self.tree.selection()[0], values=(self.var_id.get(), self.var_name.get(), self.var_gender.get(), self.var_college.get()))
                except:
                    db.rollback()
                    messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                db.close()
            else:
                messagebox.showinfo('警告！', '不能修改学生学号！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res:
            print(self.row_info[0])
            print(self.tree.selection()[0])
            print(self.tree.get_children())
            db = pymysql.connect(host="localhost", user="root", password="a1596s1596", database="school", port=3306)
            cursor = db.cursor()
            sql = "DELETE FROM student WHERE stu_id = %s"
            try:
                cursor.execute(sql, (self.row_info[0],))
                db.commit()
                messagebox.showinfo('提示！', '删除成功！')
                id_index = self.id.index(self.row_info[0])
                print(id_index)
                del self.id[id_index]
                del self.name[id_index]
                del self.gender[id_index]
                del self.college[id_index]
                print(self.id)
                self.tree.delete(self.tree.selection()[0])
                print(self.tree.get_children())
            except:
                db.rollback()
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            db.close()

#课程信息界面
class Lesson:
    def __init__(self, parent_window):
        self.window = parent_window
        self.window.geometry('1920x1080')
        self.window.title('课程信息')

        self.frame_left_top = tk.Frame(width=700, height=200)
        self.frame_right_top = tk.Frame(width=700, height=200)
        self.frame_center = tk.Frame(width=700, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)

        # 定义下方中心列表区域
        self.columns = ("课程代码", "课程名称", "学分", "课时")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("课程代码", width=150, anchor='center')  # 表示列,不显示
        self.tree.column("课程名称", width=150, anchor='center')
        self.tree.column("学分", width=100, anchor='center')
        self.tree.column("课时", width=100, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.id = []
        self.name = []
        self.cre = []
        self.hour = []
        self.load_data()

        # 写入数据
        self.populate_treeview()

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 搜索框和按钮
        self.search_var = StringVar()
        self.search_entry = Entry(self.frame_left_top, textvariable=self.search_var, font=('Verdana', 15))
        self.search_button = ttk.Button(self.frame_left_top, text='搜索', width=20, command=self.search)
        self.search_entry.grid(row=0, column=0, padx=20, pady=10)
        self.search_button.grid(row=0, column=1, padx=20, pady=10)

        # 定义左上方区域
        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()  # 声明课号
        self.var_name = StringVar()  # 声明姓名
        self.var_cre = StringVar()  # 声明学分
        self.var_hour = StringVar()  # 声明课时
        # 学号
        self.right_top_id_label = Label(self.frame_left_top, text="课程代码：", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)  # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)
        # 姓名
        self.right_top_name_label = Label(self.frame_left_top, text="课程名称：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 性别
        self.right_top_gender_label = Label(self.frame_left_top, text="学分：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_cre,font=('Verdana', 15))
        self.right_top_gender_label.grid(row=3, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 学院
        self.right_top_gender_label = Label(self.frame_left_top, text="课时：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_hour,font=('Verdana', 15))
        self.right_top_gender_label.grid(row=4, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=4, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建课程信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中课程信息', width=20,command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中课程信息', width=20,command=self.del_row)

        # 位置设置
        self.right_top_title.grid(row=5, column=0, pady=10)
        self.right_top_button1.grid(row=6, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=7, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=8, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(False)
        self.frame_right_top.grid_propagate(False)
        self.frame_center.grid_propagate(False)
        self.frame_bottom.grid_propagate(False)

        self.frame_left_top.tkraise()
        self.frame_right_top.tkraise()
        self.frame_center.tkraise()
        self.frame_bottom.tkraise()

        self.window.protocol("WM_DELETE_WINDOW", self.back)
        self.window.mainloop()

    def load_data(self):
        # 打开数据库连接
        db = pymysql.connect(host="localhost", user="root", password="a1596s1596", database="school", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM lesson"  # SQL 查询语句
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            self.id = [row[0] for row in results]
            self.name = [row[1] for row in results]
            self.cre = [row[2] for row in results]
            self.hour = [row[3] for row in results]
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

    def populate_treeview(self):
        for i in range(min(len(self.id), len(self.name), len(self.cre), len(self.hour))):
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.cre[i], self.hour[i]))

    def search(self):
        search_term = self.search_var.get()
        for item in self.tree.get_children():
            self.tree.delete(item)
        for i in range(len(self.id)):
            if search_term in self.id[i] or search_term in self.name[i]:
                self.tree.insert('', 'end', values=(self.id[i], self.name[i], self.cre[i], self.hour[i]))

    def back(self):
        AdminManage(self.window)

    def click(self, event):
        self.col = self.tree.identify_column(event.x)
        self.row = self.tree.identify_row(event.y)

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.var_name.set(self.row_info[1])
        self.var_cre.set(self.row_info[2])
        self.var_hour.set(self.row_info[3])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id, font=('Verdana', 15))
        print('')

    def tree_sort_column(self, tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))

    def new_row(self):
        print('123')
        print(self.var_id.get())
        print(self.id)
        if str(self.var_id.get()) in self.id:
            messagebox.showinfo('警告！', '该课号已被占用！')
        else:
            if self.var_id.get() != '' and self.var_name.get() != '' and self.var_cre.get() != '':
                # 打开数据库连接
                db = pymysql.connect(host="localhost", user="root", password="a1596s1596", database="school", port=3306)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                if(self.var_hour!=''):
                    # SQL 插入语句
                    sql = "INSERT INTO lesson(lesson_id, lesson_name, credit, class_hour) \
                           VALUES ('%s', '%s', '%s', '%s')" % \
                          (self.var_id.get(), self.var_name.get(), self.var_cre.get(), self.var_hour.get())
                else:
                    sql = "INSERT INTO lesson(lesson_id, lesson_name, credit, class_hour) \
                           VALUES ('%s', '%s', '%s', '尚未设置学时')" % \
                          (self.var_id.get(), self.var_name.get(), self.var_cre.get())

                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '插入成功！')
                    self.id.append(self.var_id.get())
                    self.name.append(self.var_name.get())
                    self.cre.append(self.var_cre.get())
                    self.hour.append(self.var_hour.get())
                    self.tree.insert('', len(self.id) - 1, values=(
                        self.id[len(self.id) - 1], self.name[len(self.id) - 1], self.cre[len(self.id) - 1],
                        self.hour[len(self.id) - 1]))
                    self.tree.update()
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '课时太多了！学不完！')
                db.close()  # 关闭数据库连接

            else:
                messagebox.showinfo('警告！', '请填写必要课程信息')

    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_id.get() == self.row_info[0]:  # 如果所填学号与所选学号一致
                # 打开数据库连接
                db = pymysql.connect(host="localhost", user="root", password="a1596s1596", database="school", port=3306)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                # SQL 插入语句
                sql = "UPDATE lesson SET lesson_name = '%s', credit = '%s', class_hour = '%s' \
                WHERE lesson_id = '%s'" % \
                      (self.var_name.get(), self.var_cre.get(), self.var_hour.get(), self.var_id.get())
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '更新成功！')
                    id_index = self.id.index(self.row_info[0])
                    self.name[id_index] = self.var_name.get()
                    self.cre[id_index] = self.var_cre.get()
                    self.hour[id_index] = self.var_hour.get()

                    self.tree.item(self.tree.selection()[0], values=(
                        self.var_id.get(), self.var_name.get(), self.var_cre.get(),
                        self.var_hour.get()))  # 修改对于行信息
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                db.close()  # 关闭数据库连接

            else:
                messagebox.showinfo('警告！', '不能修改课程代码！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print(self.tree.selection()[0])  # 行号
            print(self.tree.get_children())  # 所有行
            # 打开数据库连接
            db = pymysql.connect(host="localhost", user="root", password="a1596s1596", database="school", port=3306)
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "DELETE FROM lesson WHERE lesson_id = '%s'" % (self.row_info[0])  # SQL 删除语句
            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
                id_index = self.id.index(self.row_info[0])
                print(id_index)
                del self.id[id_index]
                del self.name[id_index]
                del self.cre[id_index]
                del self.hour[id_index]
                print(self.id)
                self.tree.delete(self.tree.selection()[0])  # 删除所选行
                print(self.tree.get_children())
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            db.close()  # 关闭数据库连接


# 选课信息界面
class Learn:
    def __init__(self, parent_window):
        self.window = parent_window
        self.window.geometry('1920x1080')
        self.window.title('选课信息')

        self.frame_left_top = tk.Frame(width=700, height=200)
        self.frame_right_top = tk.Frame(width=700, height=200)
        self.frame_center = tk.Frame(width=700, height=400)
        self.frame_bottom = tk.Frame(width=850, height=50)

        # 定义下方中心列表区域
        self.columns = ("学生学号", "课程代码", "教室", "成绩")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("学生学号", width=150, anchor='center')
        self.tree.column("课程代码", width=150, anchor='center')
        self.tree.column("教室", width=100, anchor='center')
        self.tree.column("成绩", width=100, anchor='center')

        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.id = []  # 学生学号
        self.les = []  # 课程代码
        self.cla = []  # 教室
        self.scr = []  # 成绩
        self.load_data()

        for i in range(min(len(self.id), len(self.les), len(self.cla), len(self.scr))):
            self.tree.insert('', i, values=(self.id[i], self.les[i], self.cla[i], self.scr[i]))

        for col in self.columns:
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        self.top_title = Label(self.frame_left_top, text="选课信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()
        self.var_les = StringVar()
        self.var_cla = StringVar()
        self.var_scr = StringVar()
        self.search_var = StringVar()  # 搜索变量

        # 学号
        self.right_top_id_label = Label(self.frame_left_top, text="学生学号：", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=0, column=0)
        self.right_top_id_entry.grid(row=0, column=1)
        # 课程代码
        self.right_top_name_label = Label(self.frame_left_top, text="课程代码：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_les, font=('Verdana', 15))
        self.right_top_name_label.grid(row=1, column=0)
        self.right_top_name_entry.grid(row=1, column=1)
        # 教室
        self.right_top_gender_label = Label(self.frame_left_top, text="教室：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_cla, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=2, column=0)
        self.right_top_gender_entry.grid(row=2, column=1)
        # 成绩
        self.right_top_gender_label = Label(self.frame_left_top, text="成绩：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_scr, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=3, column=0)
        self.right_top_gender_entry.grid(row=3, column=1)

        # 搜索框和按钮
        self.search_label = Label(self.frame_left_top, text="搜索：", font=('Verdana', 15))
        self.search_entry = Entry(self.frame_left_top, textvariable=self.search_var, font=('Verdana', 15))
        self.search_button = Button(self.frame_left_top, text="搜索", font=('Verdana', 12), command=self.search)
        self.search_label.grid(row=4, column=0)
        self.search_entry.grid(row=4, column=1)
        self.search_button.grid(row=4, column=2)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建选课信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中选课信息', width=20, command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中选课信息', width=20, command=self.del_row)
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)
        self.frame_left_top.grid_propagate(False)
        self.frame_right_top.grid_propagate(False)
        self.frame_center.grid_propagate(False)
        self.frame_bottom.grid_propagate(False)
        self.frame_left_top.tkraise()
        self.frame_right_top.tkraise()
        self.frame_center.tkraise()
        self.frame_bottom.tkraise()
        self.window.protocol("WM_DELETE_WINDOW", self.back)
        self.window.mainloop()

    def load_data(self):
        # 打开数据库连接
        db = pymysql.connect(host="localhost", user="root", password="a1596s1596", database="school", port=3306)
        cursor = db.cursor()
        sql = "SELECT * FROM learn"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                self.id.append(row[0])
                self.les.append(row[1])
                self.cla.append(row[3])
                self.scr.append(row[2])
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()

    def search(self):
        search_text = self.search_var.get().strip()
        for item in self.tree.get_children():
            self.tree.delete(item)
        for i, (id, les, cla, scr) in enumerate(zip(self.id, self.les, self.cla, self.scr)):
            if search_text in id or search_text in les or search_text in cla or search_text in scr:
                self.tree.insert('', i, values=(id, les, cla, scr))

    def back(self):
        AdminManage(self.window)

    def click(self, event):
        self.col = self.tree.identify_column(event.x)
        self.row = self.tree.identify_row(event.y)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.var_les.set(self.row_info[1])
        self.var_cla.set(self.row_info[2])
        self.var_scr.set(self.row_info[3])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id, font=('Verdana', 15))

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        #rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def new_row(self):
        print('123')
        print(self.var_id.get())
        print(self.id)
        if str(self.var_id.get()) in self.id and str(self.var_les.get()) == self.les[self.id.index(self.var_id.get())]:
            messagebox.showinfo('警告！', '该学生已选过此课程！')
        else:
            stu_id = [] # 所有学生
            les_id = [] # 开设的所有课程
            lesed_id = [] # 有人教的课
        db = pymysql.connect(host="localhost", user="root", password="a1596s1596", database="school", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标


        if self.var_id.get() == '' or self.var_les.get() == '':
            messagebox.showinfo('警告！', '请输入必要的选课信息')
        else:
                # 打开数据库连接
                db = pymysql.connect(host="localhost", user="root", password="a1596s1596", database="school", port=3306)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标

                # SQL 插入语句
                sql = "INSERT INTO learn(stu_id, lesson_id, score, class_number) \
                       VALUES ('%s', '%s', '%s', '%s')" % \
                      (self.var_id.get(), self.var_les.get(), self.var_scr.get(), self.var_cla.get())

                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    self.id.append(self.var_id.get())
                    self.les.append(self.var_les.get())
                    self.cla.append(self.var_cla.get())
                    self.scr.append(self.var_scr.get())
                    self.tree.insert('', len(self.id) - 1, values=(
                        self.id[len(self.id) - 1], self.les[len(self.id) - 1], self.cla[len(self.id) - 1],
                        self.scr[len(self.id) - 1]))
                    self.tree.update()
                    messagebox.showinfo('提示！', '插入成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '该学生已经选过此课程！')
                db.close()  # 关闭数据库连接


    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_id.get() == self.row_info[0]:  # 如果所填学号与所选学号一致
                # 打开数据库连接
                db = pymysql.connect(host="localhost", user="root", password="a1596s1596", database="school", port=3306)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                # SQL 插入语句
                sql = "UPDATE learn SET lesson_id = '%s', score = '%s', class_number = '%s' \
                WHERE stu_id = '%s' and lesson_id = '%s'" % \
                      (self.var_les.get(), self.var_scr.get(), self.var_cla.get(), self.row_info[0], self.row_info[1])
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '更新成功！')
                    id_index = self.id.index(self.row_info[0])
                    self.les[id_index] = self.var_les.get()
                    self.cla[id_index] = self.var_cla.get()
                    self.scr[id_index] = self.var_scr.get()

                    self.tree.item(self.tree.selection()[0], values=(
                        self.var_id.get(), self.var_les.get(), self.var_cla.get(),
                        self.var_scr.get()))  # 修改对于行信息
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '该学生已经选过此课程！')
                db.close()  # 关闭数据库连接

            else:
                messagebox.showinfo('警告！', '不能修改学生学号！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print(self.tree.selection()[0])  # 行号
            print(self.tree.get_children())  # 所有行
            # 打开数据库连接
            db = pymysql.connect(host="localhost", user="root", password="a1596s1596", database="school", port=3306)
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "DELETE FROM learn WHERE stu_id = '%s' and lesson_id = '%s'" % (self.row_info[0],self.row_info[1])  # SQL 删除语句
            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，不能修改')
            db.close()  # 关闭数据库连接

            id_index = self.id.index(self.row_info[0])
            print(id_index)
            del self.id[id_index]
            del self.les[id_index]
            del self.cla[id_index]
            del self.scr[id_index]
            print(self.id)
            self.tree.delete(self.tree.selection()[0])  # 删除所选行
            print(self.tree.get_children())

# 学生查看信息界面
class StudentView:
    def __init__(self, parent_window, student_id):
        self.window = parent_window
        self.window.title('学生信息查看')
        self.window.geometry('1920x1080')  # 这里的乘是小x

        # 销毁其他子窗口
        for widget in self.window.winfo_children():
            widget.destroy()

        label = tk.Label(self.window, text='学生信息查看', bg='white', font=('Verdana', 20), width=30, height=2)
        label.pack(pady=20)

        self.id = '学号:' + ''
        self.name = '姓名:' + ''
        self.gender = '性别:' + ''
        self.college = '学院:' + ''
        self.adm_time = '入学时间' + ''
        
        # 打开数据库连接
        db = pymysql.connect(host="localhost", user="root", password="a1596s1596", database="school", port=3306)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM student WHERE stu_id = '%s'" % (student_id)  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.id = '学号:' + row[0]
                self.name = '姓名:' + row[1]
                self.gender = '性别:' + row[2]
                self.college = '学院:' + row[3]
                self.adm_time = '入学时间:' + str(row[4])
                
        except:
            print("Error: unable to fetch data")
        db.close()  # 关闭数据库连接

        Label(self.window, text=self.id, font=('Verdana', 18)).pack(pady=5)
        Label(self.window, text=self.name, font=('Verdana', 18)).pack(pady=5)
        Label(self.window, text=self.gender, font=('Verdana', 18)).pack(pady=5)
        Label(self.window, text=str(self.adm_time), font=('Verdana', 18)).pack(pady=5)
        Label(self.window, text=self.college, font=('Verdana', 18)).pack(pady=5)

        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=16), command=self.back).pack(pady=25)

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口


if __name__ == '__main__':
    try:
        # 实例化Application
        window = tk.Tk()
        StartPage(window)
        window.mainloop()
    except:
        messagebox.showinfo('错误！', '连接数据库失败！')