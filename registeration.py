# \main.py

from include.constants import *
import tkinter as tk
from tkinter import filedialog
from Frames.Both.RegisterFrame import RegisterFrame
from Frames.Both.DialogFrame import DialogFrame
from include.database import Database
from include.helper import getData
from pandas import read_excel
from os.path import exists


class App(tk.Tk):
    name = None

    def __init__(self):
        tk.Tk.__init__(self)

        scrWidth = self.winfo_screenwidth()
        scrHeight = self.winfo_screenheight()

        x = (scrWidth // 2) - (WIN_W // 2)
        y = (scrHeight // 2) - (WIN_H // 2)

        
        self.title(WIN_T)
        self.minsize(WIN_W, WIN_H)
        self.geometry(f"{WIN_W}x{WIN_H}+{x}+{y}")
        self.resizable(True, True)
        self.iconbitmap("assets/icon.ico")

        self.configure(background=P_COL)
        self.bind("<Configure>", self.refresh)
        self.protocol("WM_DELETE_WINDOW", self.on_quit)
        self.box = DialogFrame(self)
        self.initDB()
        

        container = tk.Frame(self)
        container.pack(fill="both", expand=True, padx=2, pady=2)
        container.grid_rowconfigure(0, weight=1)    
        container.grid_columnconfigure(0, weight=1)
        
        self.register = RegisterFrame(container, self)
        self.register.grid(row=0, column=0, sticky="nsew")



    def initDB(self):
        global CONN
        if exists(CONN_FILE):
            CONN = eval(getData(CONN_FILE))
        print(CONN)
        
        self.database = Database(CONN[0], CONN[1], CONN[2], DB)
        info = self.database.connect()

        if info[0] == "Success":
            info = self.database.initTables(AUTH_TABLE, RESULT_TABLE, QUIZ_TABLE)
        else:
            self.box.showBox("Error", info[1], "e")

        if self.database.myDB.is_connected():
            self.database.disconnect()


    # SHOW THE FRAME ON THE MAIN APP
    def showFrame(self, toShowCont):
        frame = self.frames.get(toShowCont)
        frame.tkraise()


    # WHEN ANY BUTTON IS HOVERED
    def hoverBtn(self, event):
        event.widget["bg"] = T_COL


    # WHEN ANY BUTTON IS UNHOVERED
    def unhoverBtn(self, event):
        event.widget["bg"] = S_COL


    # METHOD TO REFRESH THE GUI
    def refresh(self, e=None):
        self.update_idletasks()


    # METHOD TO PROMPT QUIT DIALOG
    def on_quit(self):
        if self.box.showYesNoBox("Close App", "Do you really want to quit the application?"):
            if self.database.myDB.is_connected():
                self.database.disconnect()
            self.destroy()



    # ================= AUTH FUNCTIONS ======================= #
    def registerUser(self):
        id, name, classVal, pwd, confPwd = self.register.id.get(), self.register.name.get(), self.register.classVal.get(), self.register.pwd.get(), self.register.confPwd.get()
        
        if len(id) != 0 and len(name) != 0 and len(classVal) != 0 and len(pwd) != 0 and len(confPwd) != 0:
            
            if len(pwd) < 8 or len(pwd) > 20:
                return self.box.showBox(
                    "Error", 
                    "Password must be of 8 to 20 letters.", 
                    "e")
                
            elif pwd != confPwd:
                return self.box.showBox(
                    "Error", 
                    "Password donot match.", 
                    "e")
            
            info = self.database.connect()
            if info[0] == "Success":
                info = self.database.insertIntoAuthTable(AUTH_TABLE, (id, name, pwd, classVal))

                if info[0] == "Error":
                    if info[1][0] == 1062:
                        self.register.pwd.set("")
                        self.register.confPwd.set("")
                        return self.box.showBox(
                            "Error", 
                            "Userid already taken! Please use a different userid.", 
                            "e")
                        
                    else:
                        return self.box.showBox(
                            "Error", 
                            "Something went wrong! Please restart the program.", 
                            "e")
                else:
                    self.register.id.set("")
                    self.register.name.set("")
                    self.register.classVal.set("None")
                    self.register.pwd.set("")
                    self.register.confPwd.set("")
                    return self.box.showBox("Info", "Registeration successful!", "i")
            else:
                return self.box.showBox("Error", "Something went wrong! Please restart the aprogram.", "e")
                
        else:
            self.box.showBox("Warning", "Please fill all fields.", "w")
                
        if self.database.myDB.is_connected():
            self.database.disconnect()
            
            
    def bulkRegister(self, widgets):
        for widget in widgets:
            widget.configure(state=tk.DISABLED)
            
        filepath = filedialog.askopenfilename(
            title="Select an Excel file",
            filetypes=[("Excel Files", "*.xlsx *.xls *.xlsm")]
        )
    
        if filepath:
            try:
                df = read_excel(filepath).sort_index()
                for index, row in df.iterrows():
                    row = list(row)
                    print(row)
                    
                    if len(row) != 4:
                        for widget in widgets:
                            widget.configure(state=tk.NORMAL)
                            
                        return self.box.showBox(f"Error at row: {index + 1}", "Row should only contain 4 cell data in this order: (id, name, password, class)", "e")

                    else:
                        row = [str(item) for item in row]
                        info = self.database.connect()
                        if info[0] == "Success":
                            info = self.database.insertIntoAuthTable(AUTH_TABLE, row)

                            if info[0] == "Error":
                                if info[1][0] == 1062:
                                    self.box.showBox(
                                        f"Error at row {index + 1}", 
                                        "Userid already taken! Please use a different userid.", 
                                    "e")
                        
                                else:
                                    for widget in widgets:
                                        widget.configure(state=tk.NORMAL)
                                        
                                    return self.box.showBox(
                                        f"Error at row {index + 1}", 
                                        "Something went wrong! Please restart the program.", 
                                    "e")
                
                for widget in widgets:
                    widget.configure(state=tk.NORMAL)
                
                return self.box.showBox("Info", "Bulk registeration completed!", "i")

            except Exception as e:
                print(e)
                for widget in widgets:
                    widget.configure(state=tk.NORMAL)
                self.box.showBox("Error", "Something went wrong!", "e")


def main():
    app = App()
    app.mainloop()
    
    
if __name__ == '__main__':
    main()
