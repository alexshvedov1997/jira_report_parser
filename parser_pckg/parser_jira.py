from bs4 import BeautifulSoup
from copy import deepcopy
import docx


class JiraReport:

    def __init__(self):
        self.__lst_report = []
        self.__html_data = None
        self.__mydoc = docx.Document()

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
            dict_ = {}
            dict_['Project'] = project
            dict_['Summary'] = self.__parser(summary)
            dict_["Created"] = created
            dict_["Updated"] = updated
            dict_["Status"] = status
            dict_["Labels"] = self.__parse_labels(labels)
            self.__lst_report.append(dict_)
            self.__create_doc()

    def __parser(self, elem):
        elem = str(elem)
        pos = elem.find("</span>")
        pos_close = elem.find("</p>")
        return elem[pos + len("</span>"): pos_close].strip()

    def fill_document(self):
        self.__parse_data()

    def read_data(self):
        return deepcopy(self.__lst_report)

    def __create_doc(self):
        count = 0
       # self.__mydoc.add_table(num)
        for elem in self.__lst_report:
            count += 1
            str_2_head = "???????????? " + str(count) + " :\n"
            str_ = "????????????: " + elem["Project"] + "\n" + "????????????: " + elem["Summary"] + "\n" \
                   +"???????? ????????????????: " + elem["Created"] + "\n" + "???????? ????????????????: " + elem["Updated"] + \
                   "\n" + "????????????: " + elem["Status"] + "\n" + "???????????? ????????????????: " + elem["Labels"] + "\n"
        self.__mydoc.add_heading(str_2_head, 3)
        self.__mydoc.add_paragraph(str_)
        self.__mydoc.save("text.docx")

