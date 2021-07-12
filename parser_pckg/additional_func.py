def create_docx(docx_name):
    if docx_name[-5:] != ".docx":
        docx_name = docx_name + ".docx"
        return docx_name
    return docx_name

def if_file_name_empty(obj_, path_file_name):
    ecran_str = r"{}".format(path_file_name)
    if ecran_str[:-1] == r"/" or not path_file_name or path_file_name == " ":
        return obj_.get_name() + " Отчет Jira"
  # print("Path ", path_file_name)
    return path_file_name
