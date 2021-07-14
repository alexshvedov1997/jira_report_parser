from tkinter import *
from parser_pckg.MainUI import GuiJiraParser


def main():
    root = Tk()
    root.geometry("390x128")
    app = GuiJiraParser()
    root.mainloop()


if __name__ == '__main__':
    main()
