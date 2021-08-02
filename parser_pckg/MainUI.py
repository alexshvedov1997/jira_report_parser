from tkinter import Tk, Text, BOTH, W, N, E, S, StringVar
from tkinter.ttk import Frame, Button, Label, Style, Entry
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from parser_pckg.parser_jira import JiraReport
from parser_pckg.additional_func import create_docx, if_file_name_empty


class GuiJiraParser(Frame):

    def __init__(self):
        super().__init__()
        self.__work_time = StringVar()
        self.__department = StringVar()
        self.__dep_boss = StringVar()
        self.initGui()
        self.__file_name = None
        self.__jira_report = None
        self.__file_name_save = None


    def initGui(self):
        self.master.title("Формирование отчета Jira")
        label_time = Label(text="Количество рабочих часов: ")
        label_time.grid(row=0, column=0, pady=5, padx=5)
        time_entry = Entry(textvariable=self.__work_time)
        time_entry.grid(row=0, column=1, pady=5, padx=5)
        label_department = Label(text="Название отдела: ")
        label_department.grid(row=1, column=0, pady=5, padx=5)
        department_entry = Entry(textvariable=self.__department)
        department_entry.grid(row=1, column=1, pady=5, padx=5)
        label_department = Label(text="Начальник отдела: ")
        label_department.grid(row=2, column=0, pady=5, padx=5)
        department_entry = Entry(textvariable=self.__dep_boss)
        department_entry.grid(row=2, column=1, pady=5, padx=5)
        button1 = Button(text="Открыть Jira\n файл",  command=self.__extract_text, width=12, height=2)
        button1.grid(row=3, column=0,  sticky=W, pady=20, padx=10)
        button2 = Button(text="Создать отчет", command=self.__create_report, width=12, height=2)
        button2.grid(row=3, column=1, sticky=E, pady=20, padx=10)

    def __extract_text(self):
        self.__file_name = fd.askopenfilename(filetypes=(
             ("HTML files", "*.html"),))

    def __create_report(self):
        self.__jira_report = JiraReport()
        try:
             self.__jira_report.get_file_data(r"{}".format(self.__file_name))
        except:
            mb.showinfo("Отчет не создан", "Отчет не создан. Попробуйте еще раз.")
            return
        self.__jira_report.fill_document()
        self.__file_name_save = fd.asksaveasfilename(filetypes=(("Docx files", "*.docx"),))
        if not self.__file_name_save:
             mb.showinfo("Отчет не создан", "Отчет не создан. Попробуйте еще раз.")
             return
        self.__file_name_save = create_docx(self.__file_name_save)  # при закрытии создаст отчет
        var_time = str(self.__work_time.get())
        if not var_time.isdigit() or int(var_time) < 0 or not var_time:
            mb.showinfo("Отчет не создан", "Отчет не создан. Введите число.")
            return
        self.__jira_report.set_time(var_time)
        self.__jira_report.set_boss(self.__dep_boss.get())
        self.__jira_report.set_department(self.__department.get())
        self.__jira_report.create_table_docx(self.__file_name_save)
        mb.showinfo("Отчет создан", "Отчет создан")
