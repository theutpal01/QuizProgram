# \Frames\Admin\QuizManageFrame.py

import tkinter as tk
from tkinter import filedialog
from include.constants import *
import pandas as pd


class QuizManageFrame(tk.Frame):
    Preview = None
    data = None
    quests = None


    def __init__(self, parent: tk.Frame, controller: tk.Tk):
        tk.Frame.__init__(self, parent)
        self.configure(background=P_COL)

        leftFrame = tk.Frame(self, width=WIN_W // 2.5, height=WIN_H, background=P_COL)
        
        heading = tk.Label(
            leftFrame, 
            background=P_COL, 
            foreground=TXT_COL, 
            text="| QUIZ QUESTIONS |", 
            font=(FONT_FAM, FONT_SIZE, "bold"), 
            justify=tk.CENTER
            )
        heading.pack(pady=5)

        self.listView = tk.Listbox(
            leftFrame, 
            bg=P_COL, 
            fg=TXT_COL, 
            font=(FONT_FAM, 10), 
            activestyle=tk.NONE, 
            relief=tk.FLAT, 
            highlightthickness=1, 
            width=45, 
            height=20
            )
        self.listView.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

        self.previewBtn = tk.Button(
            leftFrame, 
            text="Start Preview", 
            font=(FONT_FAM, VSM_FONT_SIZE), 
            command=lambda: self.previewText(controller), 
            width=22, 
            pady=5, 
            background=S_COL, 
            foreground=TXT_COL, 
            bd=0,
            relief=tk.FLAT
            )
        self.previewBtn.pack(pady=5)
        self.previewBtn.bind('<Enter>', controller.hoverBtn)
        self.previewBtn.bind('<Leave>', controller.unhoverBtn)

        self.delBtn = tk.Button(
            leftFrame, 
            text="Delete Question", 
            font=(FONT_FAM, VSM_FONT_SIZE), 
            command=lambda: self.delQuest(controller), 
            width=22, 
            pady=5, 
            background=S_COL, 
            foreground=TXT_COL, 
            bd=0,
            relief=tk.FLAT
            )
        self.delBtn.pack(pady=5)
        self.delBtn.bind('<Enter>', controller.hoverBtn)
        self.delBtn.bind('<Leave>', controller.unhoverBtn)
        leftFrame.pack(side=tk.LEFT, fill=tk.X, expand=True, ipadx=10, ipady=10)

        rightFrame = tk.Frame(self, width=WIN_W // 1.5, height=WIN_H, background=P_COL)

        inputFrame = tk.Frame(rightFrame, background=P_COL)
        questLbl = tk.Label(
            inputFrame, 
            text="Enter question body:", 
            font=(FONT_FAM, VSM_FONT_SIZE), 
            anchor=tk.W, 
            background=P_COL, 
            foreground=TXT_COL
            )
        questLbl.pack(pady=2, fill=tk.X)
        self.quest = tk.Text(
            inputFrame, 
            font=(FONT_FAM, VSM_FONT_SIZE), 
            width=46, 
            height=5
            )
        self.quest.pack(pady=(2, 10), fill=tk.X)
                
        setFrame1 = tk.Frame(inputFrame, background=P_COL)
        opt1Frame = tk.Frame(setFrame1, background=P_COL)
        opt1Lbl = tk.Label(
            opt1Frame, 
            text=f"Enter option 1:", 
            font=(FONT_FAM, VSM_FONT_SIZE), 
            anchor=tk.W, 
            justify=tk.LEFT, 
            background=P_COL, 
            foreground=TXT_COL
            )
        self.opt1 = tk.Entry(
            opt1Frame, 
            font=(FONT_FAM, VSM_FONT_SIZE), 
            width=22, 
            disabledforeground=P_COL, 
            disabledbackground=TXT_COL
            )
        opt1Lbl.pack(pady=2, padx=2, fill=tk.X)
        self.opt1.pack(pady=2, padx=2, fill=tk.X)
        opt1Frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor=tk.E)

        opt2Frame = tk.Frame(setFrame1, background=P_COL)
        opt2Lbl = tk.Label(
            opt2Frame, 
            text=f"Enter option 2:", 
            font=(FONT_FAM, VSM_FONT_SIZE), 
            anchor=tk.W, 
            justify=tk.LEFT, 
            background=P_COL, 
            foreground=TXT_COL
            )
        self.opt2 = tk.Entry(
            opt2Frame, 
            font=(FONT_FAM, VSM_FONT_SIZE), 
            width=22, 
            disabledforeground=P_COL, 
            disabledbackground=TXT_COL
            )
        opt2Lbl.pack(pady=2, fill=tk.X)
        self.opt2.pack(pady=2, padx=2, fill=tk.X)
        opt2Frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
        setFrame1.pack(fill=tk.BOTH, expand=1, anchor=tk.W)

        setFrame2 = tk.Frame(inputFrame, background=P_COL)
        opt3Frame = tk.Frame(setFrame2, background=P_COL)
        opt3Lbl = tk.Label(
            opt3Frame, 
            text=f"Enter option 3:", 
            font=(FONT_FAM, VSM_FONT_SIZE), 
            anchor=tk.W, 
            justify=tk.LEFT, 
            background=P_COL, 
            foreground=TXT_COL
            )
        self.opt3 = tk.Entry(
            opt3Frame, 
            font=(FONT_FAM, VSM_FONT_SIZE), 
            width=22, 
            disabledforeground=P_COL, 
            disabledbackground=TXT_COL
            )
        opt3Lbl.pack(pady=2, fill=tk.X)
        self.opt3.pack(pady=2, padx=2, fill=tk.X)
        opt3Frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor=tk.E)

        opt4Frame = tk.Frame(setFrame2, background=P_COL)
        opt4Lbl = tk.Label(
            opt4Frame, 
            text=f"Enter option 4:", 
            font=(FONT_FAM, VSM_FONT_SIZE), 
            anchor=tk.W, 
            justify=tk.LEFT, 
            background=P_COL, 
            foreground=TXT_COL
            )
        self.opt4 = tk.Entry(
            opt4Frame, 
            font=(FONT_FAM, VSM_FONT_SIZE), 
            width=22, 
            disabledforeground=P_COL, 
            disabledbackground=TXT_COL
            )
        opt4Lbl.pack(pady=2, fill=tk.X)
        self.opt4.pack(pady=2, padx=2, fill=tk.X)
        opt4Frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
        setFrame2.pack(fill=tk.BOTH, expand=1, anchor=tk.W)

        ansLbl = tk.Label(
            inputFrame, 
            text=f"Enter an answer:", 
            font=(FONT_FAM, VSM_FONT_SIZE), 
            anchor=tk.W, 
            background=P_COL, 
            foreground=TXT_COL
            )
        ansLbl.pack(pady=(10, 2), fill=tk.X)
        self.ans = tk.Entry(
            inputFrame, 
            font=(FONT_FAM, VSM_FONT_SIZE), 
            width=46, 
            disabledforeground=P_COL, 
            disabledbackground=TXT_COL
            )
        self.ans.pack(pady=2, fill=tk.X)
        inputFrame.pack(padx=10, fill=tk.BOTH, expand=1)

        submitFrame = tk.Frame(rightFrame, padx=20, background=P_COL)
        innerSubmitFrame = tk.Frame(submitFrame, background=P_COL)
        self.saveBtn = tk.Button(
            innerSubmitFrame, 
            text="Save Question", 
            font=(FONT_FAM, VSM_FONT_SIZE), 
            command=lambda: controller.saveQuest(self.getData()), 
            width=21, 
            pady=5, 
            background=S_COL, 
            foreground=TXT_COL, 
            relief=tk.FLAT, 
            bd=0
            )
        self.saveBtn.pack(side=tk.LEFT, fill=tk.X, expand=1, padx=5, pady=5)
        self.saveBtn.bind('<Enter>', controller.hoverBtn)
        self.saveBtn.bind('<Leave>', controller.unhoverBtn)

        backBtn = tk.Button(
            innerSubmitFrame, 
            text="Go Back", 
            font=(FONT_FAM, VSM_FONT_SIZE), 
            width=21, 
            pady=5, 
            background=S_COL, 
            foreground=TXT_COL, 
            relief=tk.FLAT, 
            bd=0, 
            command=lambda: controller.showFrame("admin")
            )
        backBtn.pack(side=tk.RIGHT, fill=tk.X, expand=1, padx=5, pady=5)
        backBtn.bind('<Enter>', controller.hoverBtn)
        backBtn.bind('<Leave>', controller.unhoverBtn)
        innerSubmitFrame.pack(side=tk.BOTTOM, pady=5, fill=tk.X, expand=1)

        self.multiSaveBtn = tk.Button(
            submitFrame, 
            text="Save Multiple Questions", 
            font=(FONT_FAM, VSM_FONT_SIZE), 
            width=45, 
            pady=5, 
            background=S_COL, 
            foreground=TXT_COL, 
            relief=tk.FLAT, 
            bd=0, 
            command=lambda: self.saveMultiple(controller)
            )
        submitFrame.pack(pady=(30, 0), fill=tk.X, expand=1)
        self.multiSaveBtn.pack(padx=5, pady=(0, 5), fill=tk.X, expand=1)
        self.multiSaveBtn.bind('<Enter>', controller.hoverBtn)
        self.multiSaveBtn.bind('<Leave>', controller.unhoverBtn)

        rightFrame.pack(side=tk.RIGHT, fill=tk.X, expand=True, ipadx=10, ipady=10)

        note = tk.Label(
            self, 
            text="Note: Any changes in the \questions will clear the previous results of users!", 
            font=(FONT_FAM, 9), 
            bg=P_COL, 
            fg=TXT_COL
            )
        note.place(in_=self, relx=0.01, rely=0.95)


    @classmethod
    def initData(cls, controller, self, data):
        cls.Preview = False
        self.switchState(controller)
        self.clearData()
        cls.data = data
        cls.quests = []

        for _, entry in data:
            cls.quests.append(entry[1])
        cls.quests = tuple(enumerate(cls.quests))
       
        self.setData()

    
    @staticmethod
    def formatText(text, limit):
        if len(text) > limit:
            return text[:limit + 1] + "..."
        return text


    def setData(self):
        self.update_idletasks()
        self.listView.delete(0, tk.END)
        for i, quest in QuizManageFrame.quests:
            self.listView.insert(i, " " + str(i + 1) + ") " + quest)


    def clearData(self):
        self.update_idletasks()
        self.quest.delete(1.0, tk.END)
        self.opt1.delete(0, tk.END)
        self.opt2.delete(0, tk.END)
        self.opt3.delete(0, tk.END)
        self.opt4.delete(0, tk.END)
        self.ans.delete(0, tk.END)


    def getData(self, update:bool=False):
        data = [self.quest.get(1.0, tk.END)[:-1], self.opt1.get(), self.opt2.get(), self.opt3.get(), self.opt4.get(), self.ans.get()]
        
        if update:
            try:
                print(self.listView.curselection())
                data.append(QuizManageFrame.data[self.listView.curselection()[0]][1][0])
            except: pass
        return tuple(data)


    def switchState(self, controller, indexS=None):
        widgets = (self.delBtn, self.multiSaveBtn)
        if QuizManageFrame.Preview and indexS is not None:
            self.quest.insert(1.0, QuizManageFrame.data[indexS][1][1])
            self.opt1.insert(0, QuizManageFrame.data[indexS][1][2])
            self.opt2.insert(0, QuizManageFrame.data[indexS][1][3])
            self.opt3.insert(0, QuizManageFrame.data[indexS][1][4])
            self.opt4.insert(0, QuizManageFrame.data[indexS][1][5])
            self.ans.insert(0, QuizManageFrame.data[indexS][1][6])
            self.previewBtn.config(text="Stop Preview")

            for widget in widgets:
                widget.configure(state=tk.DISABLED)
                
            self.saveBtn.configure(text="Update Question", command=lambda: controller.saveQuest(self.getData(update=True), update=True))
        
        elif not QuizManageFrame.Preview:
            self.previewBtn.config(text="Start Preview")
            for widget in widgets:
                widget.configure(state=tk.NORMAL)
            self.saveBtn.configure(text="Save Question", command=lambda: controller.saveQuest(self.getData()))
            self.clearData()


    def previewText(self, controller):
        selected = self.listView.curselection()
        selected = selected[0] if len(selected) != 0 else None

        if selected is not None and not QuizManageFrame.Preview:
            QuizManageFrame.Preview = True
            self.switchState(controller, selected)
        elif QuizManageFrame.Preview:
            QuizManageFrame.Preview = False
            self.switchState(controller)
        else:
            controller.box.showBox(
                "Warning", 
                "Please first select a question to preview it.", 
                "w"
                )
        

    def delQuest(self, controller:tk.Tk):
        selected = self.listView.curselection()
        selected = selected[0] if len(selected) != 0 else None

        availUsers = True
        doChange = True

        if selected is not None:
            qName = QuizManageFrame.quests[selected][1]
            info = controller.database.connect()
            if info[0] == "Success":
                
                info = controller.database.fetchUsers(RESULT_TABLE)
                availUsers = False if info[0] != "Success" else True

                if availUsers:
                    doChange = controller.box.showYesNoBox(\
                        "Want to continue?", 
                        "Deleting a question will clear the data of users who have given the quiz. Do you wish to continue?"
                        )
        
                if doChange:
                    info = controller.database.delQuestById(QUIZ_TABLE, QuizManageFrame.data[selected][1][0])
                    if info[0] == "Success":
                        if controller.database.clearTable(RESULT_TABLE)[0] == "Success":
                            info = controller.database.updateAttemptAll(AUTH_TABLE, 0)
                            if info[0] == "Success":
                                controller.box.showBox(
                                    "Info", "The question has been deleted successfully!", "i"
                                )
                    else:
                        controller.box.showBox(
                            "Error", "Something went wrong! Please restart the program.", "e"
                        )
                    controller.showQuizDetails()
            else:
                controller.box.showBox(
                    "Error", 
                    "Something went wrong! Please restart the program.", 
                    "e"
                    )
            
            if controller.database.myDB.is_connected():
                controller.database.disconnect()
                
    
    def saveMultiple(self, controller: tk.Tk):
        filepath = filedialog.askopenfilename(
            title="Select an Excel file",
            filetypes=[("Excel Files", "*.xlsx *.xls *.xlsm")]
        )
        if filepath:
            try:
                data = []
                df = pd.read_excel(filepath)
                for index, row in df.iterrows():
                    row = list(row)
                    
                    if len(row) != 6:
                        return controller.box.showBox(f"Error at row: {index + 1}", "Row should only contain 6 cell data in this order: (question, opttion A, option B, option C, option D, answer)", "e")

                    else:
                        row = [str(item) for item in row]
                        data.append(row)
                
                controller.saveQuestMultiple(tuple(data))
                        
            except Exception as e:
                print(e)
                controller.box.showBox("Error", "Something went wrong!", "e")            
            
