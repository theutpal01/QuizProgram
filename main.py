# \main.py

from include.constants import *
import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from tkinter.ttk import Style, Treeview
from json import loads, dumps
from os.path import exists
from pandas import DataFrame
from Frames.Both.DialogFrame import DialogFrame
from Frames.Both.LoginFrame import LoginFrame
from Frames.User.MenuFrame import MenuFrame
from Frames.User.QuizFrame import QuizFrame
from Frames.User.ResultFrame import ResultFrame
from Frames.Admin.AdminFrame import AdminFrame
from Frames.Admin.ResultManageFrame import ResultManageFrame
from Frames.Admin.QuizManageFrame import QuizManageFrame
from include.database import Database
from include.helper import getData


class App(tk.Tk):
    id = None
    name = None
    classVal = None

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
        
        self.frames = {}
        self.initFrames(container)
        self.showFrame("login")
        
        
    def initFrames(self, container):
        login = LoginFrame(container, self)
        login.grid(row=0, column=0, sticky="nsew")
        
        menu = MenuFrame(container, self)
        menu.grid(row=0, column=0, sticky="nsew")

        result = ResultFrame(container, self)
        result.grid(row=0, column=0, sticky="nsew")

        quiz = QuizFrame(container, self)
        quiz.grid(row=0, column=0, sticky="nsew")

        admin = AdminFrame(container, self)
        admin.grid(row=0, column=0, sticky="nsew")

        rManage = ResultManageFrame(container, self)
        rManage.grid(row=0, column=0, sticky="nsew")

        qManage = QuizManageFrame(container, self)
        qManage.grid(row=0, column=0, sticky="nsew")

        self.frames.update(
            {"login": login, "menu": menu, "quiz": quiz, "result": result, "admin": admin, "rManage": rManage, "qManage": qManage}
        )


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
        if self.box.showYesNoBox("Close app", "Do you really want to quit the application?"):
            if self.database.myDB.is_connected():
                self.database.disconnect()
            self.destroy()



    # ================= AUTH FUNCTIONS ======================= #
    def loginUser(self):
        id, pwd = self.frames.get("login").id.get(), self.frames.get("login").pwd.get()

        if len(id) != 0 and len(pwd) != 0:
            info = self.database.connect()
            
            if info[0] == "Success":
                info = self.database.getFromAuthTable(AUTH_TABLE, id, pwd)

                if info[0] == "Success":
                    
                    if info[1][-2] == "admin":
                        self.box.showBox("Info", "Welcome back Admin! You will be redirected to Admin Pannel.", "i")
                        self.showFrame("admin")

                    elif info[1][-2] == "user":
                        self.box.showBox("Info", "You have successfully logged in! You will be redirected to Main Menu", "i")
                        MenuFrame.initData(info[1][-1])
                        self.showFrame("menu")
                    
                    self.frames.get("login").id.set("")
                    self.frames.get("login").pwd.set("")
                    App.id = info[1][0]
                    App.name = info[1][1]
                    App.classVal = info[1][2]
                
                elif info[0] == "Warn":
                    self.box.showBox("Warning", info[1], "w")
                    self.frames.get("login").pwd.set("")
            
            else:
                self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")
        
        else:
            self.box.showBox("Warning", "Please fill all fields.", "w")

        if self.database.myDB.is_connected():
            self.database.disconnect()


    def logout(self):
        App.id = None
        App.name = None
        App.classVal = None
        self.showFrame("login")


    # ================= ADMIN FUNCTIONS ======================= #
    def showUserDetails(self):
        info = self.database.connect()
            
        if info[0] == "Success":
            info = self.database.fetchUsers(RESULT_TABLE)
            
            if info[0] == "Error":
                self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")

            elif info[0] == "Warn":
                self.box.showBox("Warning", info[1], "w")
                self.showFrame("admin")

            else:
                info = info[1]
                info = tuple(enumerate(info))
                ResultManageFrame.initData(self.frames.get("rManage"), info)
                self.showFrame("rManage")
        
        else:
            self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")
        
        if self.database.myDB.is_connected():
            self.database.disconnect()


    def showQuizDetails(self):
        info = self.database.connect()
            
        if info[0] == "Success":
            info = self.database.fetchQuests(QUIZ_TABLE)

            if info[0] == "Error":
                self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")

            else:
                info = info[1]
                info = tuple(enumerate(info)) if len(info) != 0 else tuple()
                QuizManageFrame.initData(self, self.frames.get("qManage"), info)
                self.showFrame("qManage")
        
        else:
            self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")
        
        if self.database.myDB.is_connected():
            self.database.disconnect()


    def saveQuest(self, data, update:bool=False):
        print("DATA: ", data)
        canSave = True
        availUsers = True
        doChange = True

        for i in data[:len(data)-1]:
            if len(i) == 0 or i.isspace():
                canSave = False
        
        if canSave:
            info = self.database.connect()
            
            if info[0] == "Success":

                info = self.database.fetchUsers(RESULT_TABLE)
                availUsers = False if info[0] != "Success" else True

                if availUsers:
                    doChange = self.box.showOkBox(
                        "Alert", 
                        "Saving" if not update else "Updating" + "the question will clear the users data who have attempted the quiz till now!")
        
                if doChange:
                    info = self.database.saveQuests(QUIZ_TABLE, data) if not update else self.database.saveQuests(QUIZ_TABLE, data, update=True)
                    if info[0] == "Success":
                        if self.database.clearTable(RESULT_TABLE)[0] == "Success":
                            info = self.database.updateAttemptAll(AUTH_TABLE, 0)
                            if info[0] == "Success":
                                self.box.showBox("Info", "Question " + ("added" if not update else "updated") + " successfully.", "i")
                                self.showQuizDetails()
                        else:
                            return self.box.showBox("Error", "Something went wrong while clearing results.", "e")
        
            else:
                self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")
        
            if self.database.myDB.is_connected():
                self.database.disconnect()

    
    def saveQuestMultiple(self, values):
        canSave = True
        availUsers = True
        doChange = True

        for value in values:
            for i in value:
                if len(i) == 0 or i.isspace():
                    canSave = False

        if canSave:
            info = self.database.connect()
            
            if info[0] == "Success":
                availUsers = False if info[0] != "Success" else True

                if availUsers:
                    doChange = self.box.showOkBox(
                        "Alert", 
                        "Saving the questions will clear the users data who have attempted the quiz till now!")
        
                if doChange:
                    info = self.database.saveQuests(QUIZ_TABLE, values, True)
                    if info[0] == "Success":
                        if self.database.clearTable(RESULT_TABLE)[0] == "Success":
                            info = self.database.updateAttemptAll(AUTH_TABLE, 0)
                            if info[0] == "Success":
                                self.box.showBox("Info", "Successfully added all the questions.", "i")
                                self.showQuizDetails()
                    else:
                        self.box.showBox("Error", "Something went wrong! Please recheck the format of questions.", "e")
            
            else:
                self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")
        
            if self.database.myDB.is_connected():
                self.database.disconnect()


    def delUserRes(self, tbName:str, id:int, value:int):
        info = self.database.connect()
            
        if info[0] == "Success":
            info = self.database.delResultById(tbName, id)
            if info[0] == "Success":
                info = self.database.updateAttempt(AUTH_TABLE, value, id)
                if info[0] == "Success":
                    self.box.showBox("Info", "Successfully deleted the user data!", "i")
                    self.showUserDetails()
                else:
                    self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")
            else:
                self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")
        else:
            self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")

        if self.database.myDB.is_connected():
            self.database.disconnect()


    def exportResults(self):
        info = self.database.connect()
            
        if info[0] == "Success":
            info = self.database.fetchUsers(RESULT_TABLE)
            
            if info[0] == "Error":
                self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")

            elif info[0] == "Warn":
                self.box.showBox("Warning", info[1], "w")
                self.showFrame("admin")

            else:
                info = info[1]
                
                data = {'Id': [data[0] for data in info], 
                        'Name': [data[1] for data in info], 
                        'Class': [data[2] for data in info],
                        'Score': [data[5] for data in info],
                        'Grade': [data[4] for data in info],
                        'Percentage': [data[6] for data in info],
                        }
                df = DataFrame(data)
                file_path = asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])

                if file_path:
                    df.to_excel(file_path, index=False)
                    self.box.showBox("Info", "Results succesfully exported!", "i")
                else:
                    self.box.showBox("Error", "Failed to export results!", "e")
        
        else:
            self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")
        
        if self.database.myDB.is_connected():
            self.database.disconnect()


    # ================= USER FUNCTIONS ======================= #
    def playQuiz(self, attempted:int):
        if attempted == 0:
            info = self.database.connect()
            
            if info[0] == "Success":
                info = self.database.fetchQuests(QUIZ_TABLE)

                if info[0] == "Error":
                    self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")

                else:
                    info = info[1]
                    info = [row[1:] for row in info]
                    info = tuple(enumerate(info)) if len(info) != 0 else ()
                    if len(info) != 0:
                        QuizFrame.initData(self.frames.get("quiz"), info)
                        self.frames.get("quiz").focus_set()
                        self.showFrame("quiz")
                    else:
                        self.box.showBox("Info", "No Quiz for the time being.", "i")
            else:
                self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")
            
            if self.database.myDB.is_connected():
                self.database.disconnect()
        
        else:
            self.box.showBox("Info", "You have already given the quiz.", "i")

    
    def quizComplete(self, answers:dict, score:str, percent:str, grade:str):
        answers = dumps(answers)
        info = self.database.connect()
        print(App.id, App.name, App.classVal, answers, grade, score, percent)
        if info[0] == "Success":
            info = self.database.insertIntoResultTable(RESULT_TABLE, (App.id, App.name, App.classVal, answers, grade, score, percent))
            if info[0] == "Success":
                info = self.database.updateAttempt(AUTH_TABLE, 1, App.id)

                if info[0] == "Success":
                    MenuFrame.initData(1)
                    self.showFrame("menu")
                    self.box.showBox("Info", "To check the result click the GET YOUR RESULT button.", "i")
            
            else:
                self.box.showBox("Error", "Something went wrong!! Please restart the program.", "e")
        else:
            self.box.showBox("Error", "Something went wrong!~~ Please restart the program.", "e")
            
        if self.database.myDB.is_connected():
            self.database.disconnect()


    def showResult(self):
        info = self.database.connect()

        if info[0] == "Success":
            info = self.database.fetchUsers(RESULT_TABLE, App.id)

            if info[0] == "Error":
                self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")

            elif info[0] == "Warn":
                self.box.showBox("Warning", info[1], "w")

            else:
                info = info[1][0]
                ResultFrame.initData(self.frames.get("result"), info)
                self.showFrame("result")
        else:
            self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")

        if self.database.myDB.is_connected():
            self.database.disconnect()



    # ======================== ADMIN AND USER FUNCTIONS ========================= #
    @staticmethod
    def compareWin(self, controller, id, btns):

        def close():
            self.COMPARING = False

            for btn in btns:
                btn.config(state=tk.NORMAL)

            win.destroy()

        win = tk.Toplevel(self)
        win.protocol("WM_DELETE_WINDOW", close)
        win.resizable(False, False)
        win.title("Compare Answers")

        tableFrame = tk.Frame(win, background=P_COL)
        columns = ('Question', 'Your Answer', 'Correct Answer')
        info = controller.database.connect()

        if info[0] == "Success":
            info = controller.database.fetchQandA(QUIZ_TABLE, RESULT_TABLE, id)

            if info[0] == "Success":
                realAns, myAns = info[1][0], loads(info[1][1][0][0])

                Style().configure("Treeview", background=T_COL,foreground=TXT_COL)
                table = Treeview(win, columns=columns)

                table.column("#0", width=0, stretch=tk.NO)
                table.column(columns[0], anchor=tk.W, width=400, minwidth=300)
                table.column(columns[1], anchor=tk.W, width=200, minwidth=150)
                table.column(columns[2], anchor=tk.W, width=200, minwidth=150)

                table.heading("#0", text="", anchor=tk.W)
                table.heading(columns[0], text=columns[0], anchor=tk.W)
                table.heading(columns[1], text=columns[1], anchor=tk.W)
                table.heading(columns[2], text=columns[2], anchor=tk.W)

                for i in range(len(realAns)):
                    quest, ans = realAns[i]
                    table.insert("", index=tk.END, iid=str(i), values=(quest, "Not answered" if myAns.get(quest) is None else myAns.get(quest), ans))

                table.pack()
                tableFrame.pack(expand=True, fill=tk.BOTH, anchor=tk.CENTER)
            else:
                close()
                self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")
        else:
            self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")

        if controller.database.myDB.is_connected():
            controller.database.disconnect()



def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()
