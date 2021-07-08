from parser_pckg.parser_jira import JiraReport

obj_ = JiraReport()
obj_.get_file_data("Task monthly report (Jira) 2021-07-08T09_19_07+0300.html")
obj_.fill_document()
for elem in obj_.read_data():
    print(elem)




