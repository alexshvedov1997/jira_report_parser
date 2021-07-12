from tkinter import *
from parser_pckg.additional_func import create_docx, if_file_name_empty
from parser_pckg.MainUI import GuiJiraParser


# file_name = None
#
#
# def extract_text():
#     global file_name
#     file_name = fd.askopenfilename(filetypes=(
#                    ("HTML files", "*.html"),))
#
#
# def create_report():
#     global file_name
#     obj_ = JiraReport()
#     try:
#         obj_.get_file_data(r"{}".format(file_name))
#     except:
#         mb.showinfo("Отчет не создан", "Отчет не создан. Попробуйте еще раз.")
#         return
#     obj_.fill_document()
#     file_name_save = fd.asksaveasfilename(filetypes=(("Docx files", "*.docx"),))
#     if not file_name_save:
#         mb.showinfo("Отчет не создан", "Отчет не создан. Попробуйте еще раз.")
#         return
#     file_name_save = if_file_name_empty(obj_, file_name_save)
#     file_name_save = create_docx(file_name_save) # при закрытии создаст отчет
#     mb.showinfo("Отчет создан", "Отчет создан")
#     print(file_name_save)
#     obj_.create_doc(file_name_save)


# root = Tk()
# TIME_WORK =  StringVar()
# root.title("Формирование отчета Jira")
# root.geometry("600x400")
# button1 = Button(root, text="Открыть Jira\n файл", height=2,
#                  width=10, command=extract_text)
# button2 = Button(root, text="Создать отчет", height=2,
#                  width=10, command=create_report)
# time_label = Label(text="Введите количество рабочих часов: ")
#
# time_label.grid(row=3, column=0, sticky="w")
# time = Entry(textvariable=TIME_WORK)
# time.grid(row=3, column=1, padx=5, pady=5)
# #button1.pack(side=LEFT)
# #button2.pack(side=RIGHT)
# button1.grid(row=10, column=0)
# button2.grid(row=10, column=1)
#
# root.mainloop()

def main():
    root = Tk()
   # root.geometry("400x200+300+300")
    root.geometry("390x128")
    app = GuiJiraParser()
    root.mainloop()


if __name__ == '__main__':
    main()