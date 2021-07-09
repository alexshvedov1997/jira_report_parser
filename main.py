from parser_pckg.parser_jira import JiraReport
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from parser_pckg.additional_func import create_docx, if_file_name_empty

file_name = None

def extract_text():
    global file_name
    file_name = fd.askopenfilename(filetypes=(
                   ("HTML files", "*.html"),))

def create_report():
    global file_name
    obj_ = JiraReport()
    try:
        obj_.get_file_data(r"{}".format(file_name))
    except:
        mb.showinfo("Отчет не создан", "Отчет не создан. Попробуйте еще раз.")
        return
    obj_.fill_document()
    file_name_save = fd.asksaveasfilename(filetypes=(("Docx files", "*.docx"),))
    if not file_name_save:
        mb.showinfo("Отчет не создан", "Отчет не создан. Попробуйте еще раз.")
        return
    file_name_save = if_file_name_empty(obj_, file_name_save)
    file_name_save = create_docx(file_name_save) # при закрытии создаст отчет
    mb.showinfo("Отчет создан", "Отчет создан")
    print(file_name_save)
    obj_.create_doc(file_name_save)


root = Tk()
root.title("Формирование отчета Jira")
root.geometry("300x200")
button1 = Button(root, text="Открыть Jira\n файл", height=2,
          width=10, command=extract_text)
button2 = Button(root, text="Создать отчет", height=2,
          width=10, command=create_report)
button1.pack(side=LEFT)
button2.pack(side=RIGHT)

root.mainloop()
