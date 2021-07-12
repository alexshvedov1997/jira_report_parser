from bs4 import BeautifulSoup
from copy import deepcopy
import docx
from docx.shared import Inches


class JiraReport:

    def __init__(self):
        self.__lst_report = []
        self.__html_data = None
        self.__mydoc = docx.Document()
        self.__name = None
        self.__work_time = None
        self.__table = None

    def get_file_data(self, path):
        with open(path) as f:
            self.__html_data = f.read()

    def __parse_labels(self, labels):
        str_label = str(labels)
        lst_label = str_label.split(",")
        lst_res = []
        for elem in lst_label:
            new_elem = elem.strip()
            if '.' in new_elem:
                lst_res.append(new_elem[: new_elem.find('.')])
                continue
            lst_res.append(new_elem)
        set_ = set(lst_res)
        return ', '.join(list(set_))

    def __parse_data(self):
        soup = BeautifulSoup(self.__html_data, 'lxml')
        get_all_row = soup.find('table', id="issuetable").find_all('tr')
        count = 0
        count_name = 0
        for elem in get_all_row:
            if count == 0:
                count = 1
                continue
            project = elem.find('td', class_="project").get_text().strip()
            summary = elem.find('td', class_="summary").find('p')
            created = elem.find('td', class_="created").get_text()
            updated = elem.find('td', class_="updated").get_text()
            status = elem.find('td', class_="status").find("span").get_text()
            labels = elem.find('td', class_="labels").get_text()
            if not count_name:
                self.__name = elem.find('td', class_="assignee").get_text()
                if self.__name:
                    count_name += 1
            dict_ = {}
            dict_['Project'] = project
            dict_['Summary'] = self.__parser(summary)
            dict_["Created"] = created
            dict_["Updated"] = updated
            dict_["Status"] = status
            dict_["Labels"] = self.__parse_labels(labels)
            if dict_["Status"] == "Done":
                self.__lst_report.append(dict_)

    def __parser(self, elem):
        elem = str(elem)
        pos = elem.find("</span>")
        pos_close = elem.find("</p>")
        return elem[pos + len("</span>"): pos_close].strip()

    def fill_document(self):
        self.__parse_data()

    def read_data(self):
        return deepcopy(self.__lst_report)

    def create_doc(self, path):
        count = 0
       # self.__mydoc.add_table(num)
        self.__add_time_to_project()
        self.__mydoc.add_paragraph("ФИО: " + self.__name)
        self.__mydoc.add_paragraph("Количество часов: " + self.__work_time)
        for elem in self.__lst_report:
            count += 1
            str_2_head = "Задача " + str(count) + " :\n"
            str_ = "Проект: " + elem["Project"] + "\n" + "Задача: " + elem["Summary"] + "\n" \
                  + "Затраченное время: " + elem["Time"]  + \
                   "\n" + "Статус: " + elem["Status"] + "\n" + "Список проектов: " + elem["Labels"] + "\n"
            self.__mydoc.add_heading(str_2_head, 3)
            self.__mydoc.add_paragraph(str_)
        self.__mydoc.save(r"{}".format(path))

    def create_table_docx(self, path):
        self.__add_time_to_project()
        self.__mydoc.add_paragraph("ФИО: " + self.__name)
        self.__mydoc.add_paragraph("Количество часов: " + self.__work_time)
        self.__table = self.__mydoc.add_table(rows=(len(self.__lst_report) + 1), cols=4)
       # self.__set_columns_inches(self.__table)
        autofit = False
        for cell in self.__table.columns[0].cells:
            cell.width = Inches(0.5)
        self.__mydoc.save(r"{}".format(path))

    def get_name(self):
        return self.__name

    def set_time(self, str_):
        self.__work_time = str_

    def __add_time_to_project(self):
        count_of_task = len(self.__lst_report)
        hours = int(self.__work_time) // count_of_task
        counter = 0
        for elem in self.__lst_report:
            counter += 1
            if counter == count_of_task and count_of_task * hours < int(self.__work_time):
                hours += int(self.__work_time) - count_of_task * hours
            elem["Time"] = str(hours)

    def __set_columns_inches(self, table):
        widths = (Inches(1), Inches(3), Inches(1), Inches(2))
        for row in table.rows:
            for idx, width in enumerate(widths):
                row.cells[idx].width = width
