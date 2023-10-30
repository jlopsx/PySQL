from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk 
from SQL import DataBase
import glob
import os

class Application():
    def  __init__(self, x, y):
        self.x = x
        self.y = y
        self.win = Tk()
        self.win.geometry(str(self.x)+"x"+str(self.y))
        self.win.title("Application")

        self.entries()
        self.labels()
        self.listbox()  
        self.buttons()

        self.verify_databases()
    def labels(self):
        title = Label(self.win, text="PySQL", font="arial 25")
        title.grid(padx=15, pady=25)

        resultquery = Label(self.win, text= "RESULT QUERY: ", font="arial 20")
        resultquery.place(x=200, y=500)
    def entries(self):
        self.txtcommand = ScrolledText(self.win, width = 120)
        self.txtcommand.place(x=200, y= 100)

        resultcommand = ScrolledText(self.win,  width= 120)
        resultcommand.place(x=200, y=550)
        resultcommand["yscrollcommand"] = None
    def buttons(self):
        bt = Button(self.win, text="RUN", width=5, command=self.init_connection)
        bt.place(x=1100,y=500)

    def init_connection(self):
        txt = self.txtcommand.get("1.0", "end-1c")
        db_name = txt.split()
        db = open(str(db_name[2])+".db", "w")
        db.close()
        
        self.database = DataBase(db_name[2]+".db")

        db_n = self.tw.insert(self.mydb, "end", text=db_name[2])

    def verify_databases(self):
        archives = glob.glob("D:/PySQL/*.db")

        if archives:
            for arch in archives:
                db_n = self.tw.insert(self.mydb, "end", text=os.path.basename(arch))
        else:
            return


    def listbox(self):
        self.tw = ttk.Treeview(self.win)
        self.tw.grid(pady=15)

        self.mydb = self.tw.insert("", "end", text="My Databases: ")
    
    
    def main(self):
        self.win.mainloop()

if __name__ == '__main__':
    app = Application(1200, 800)
    app.main()