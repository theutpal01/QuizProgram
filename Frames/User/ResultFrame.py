# Frames/User/ResultFrame.py

import tkinter as tk
from include.constants import *


class ResultFrame(tk.Frame):
    data = None

    def __init__(self, parent: tk.Frame, controller: tk.Tk):
        tk.Frame.__init__(self, parent)
        self.configure(background=P_COL)
        self.COMPARING = False
        self.userVar = tk.StringVar(self, None)
        self.classVar = tk.StringVar(self, None)
        self.gradeVar = tk.StringVar(self, None)
        self.scoreVar = tk.StringVar(self, None)
        self.percentVar = tk.StringVar(self, None)

        leftFrame = tk.Frame(self, width=(WIN_W // 2), height=WIN_H, background=P_COL)
        image = tk.PhotoImage(file=GRADE_IMG)
        imageLbl = tk.Label(
            leftFrame, 
            image=image, 
            width=(WIN_W // 2), 
            background=P_COL)
        imageLbl.photo = image
        imageLbl.place(in_=leftFrame, relx=0.5, rely=0.5, anchor="center")


        self.grade = tk.Label(
            leftFrame, 
            textvariable=self.gradeVar, 
            font=(FONT_FAM, GRADE_FONT), 
            background=BLACK, 
            foreground=TXT_COL)
        self.grade.place(in_=leftFrame, relx=0.5, rely=0.46, anchor="center")
        leftFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, ipadx=10, ipady=10)
    
        rightFrame = tk.Frame(self, width=(WIN_W // 2), height=WIN_H, bg=P_COL)
        inputFrame = tk.Frame(rightFrame, padx=5, background=P_COL)
        user = tk.Label(
            inputFrame, 
            text="Username:", 
            font=(FONT_FAM, SM_FONT_SIZE), 
            anchor=tk.W, 
            background=P_COL, 
            foreground=TXT_COL)
        user.pack(pady=2, fill=tk.X)
        self.user = tk.Entry(
            inputFrame, 
            textvariable=self.userVar, 
            font=(FONT_FAM, FONT_SIZE), 
            width=25, 
            state=tk.DISABLED, 
            disabledforeground=P_COL)
        self.user.pack(pady=2, fill=tk.X)
    
        dummyLbl = tk.Label(inputFrame, background=P_COL)
        dummyLbl.pack(pady=2, fill=tk.X)
       
        classLbl = tk.Label(
            inputFrame, 
            text="Class:", 
            font=(FONT_FAM, SM_FONT_SIZE), 
            anchor=tk.W, 
            background=P_COL, 
            foreground=TXT_COL)
        classLbl.pack(pady=2, fill=tk.X)
        self.classTxt = tk.Entry(
            inputFrame, 
            textvariable=self.classVar, 
            font=(FONT_FAM, FONT_SIZE), 
            width=25, 
            state=tk.DISABLED, 
            disabledforeground=P_COL)
        self.classTxt.pack(pady=2, fill=tk.X)
    
        dummyLbl = tk.Label(inputFrame, background=P_COL)
        dummyLbl.pack(pady=2, fill=tk.X)

        score = tk.Label(
            inputFrame, 
            text="Your Score:", 
            font=(FONT_FAM, SM_FONT_SIZE), 
            anchor=tk.W, 
            background=P_COL, 
            foreground=TXT_COL)
        score.pack(pady=2, fill=tk.X)
        
        self.score = tk.Entry(
            inputFrame, 
            textvariable=self.scoreVar, 
            font=(FONT_FAM, SM_FONT_SIZE), 
            width=25, 
            state=tk.DISABLED, 
            disabledforeground=P_COL)
        self.score.pack(pady=2, fill=tk.X)
    
        dummyLbl = tk.Label(inputFrame, background=P_COL)
        dummyLbl.pack(pady=2, fill=tk.X)

        percent = tk.Label(
            inputFrame, 
            text="Your Percentage:", 
            font=(FONT_FAM, SM_FONT_SIZE), 
            anchor=tk.W, 
            background=P_COL, 
            foreground=TXT_COL)
        percent.pack(pady=2, fill=tk.X)
        self.percent = tk.Entry(
            inputFrame, 
            textvariable=self.percentVar, 
            font=(FONT_FAM, SM_FONT_SIZE), 
            width=25, 
            state=tk.DISABLED, 
            disabledforeground=P_COL)
        self.percent.pack(pady=2, fill=tk.X)
    
        dummyLbl = tk.Label(inputFrame, background=P_COL)
        dummyLbl.pack(pady=2, fill=tk.X)
        inputFrame.pack(anchor=tk.CENTER, fill=tk.X, padx=30, expand=1)
    
        submitFrame = tk.Frame(rightFrame, padx=10, background=P_COL)
        compareBtn = tk.Button(
            submitFrame, 
            text="Compare Answers", 
            font=(FONT_FAM, SM_FONT_SIZE), 
            width=24, 
            pady=5, 
            background=S_COL, 
            foreground=TXT_COL, 
            relief=tk.FLAT, 
            bd=0)
        compareBtn.pack(padx=5, pady=5)
        compareBtn.bind('<Enter>', controller.hoverBtn)
        compareBtn.bind('<Leave>', controller.unhoverBtn)

        backBtn = tk.Button(
            submitFrame, 
            text="Go Back", 
            font=(FONT_FAM, SM_FONT_SIZE), 
            width=24, 
            pady=5, 
            background=S_COL, 
            foreground=TXT_COL, 
            relief=tk.FLAT, 
            bd=0, 
            command=lambda: controller.showFrame("menu"))
        backBtn.pack(padx=5, pady=5)
        backBtn.bind('<Enter>', controller.hoverBtn)
        backBtn.bind('<Leave>', controller.unhoverBtn)
        submitFrame.pack(anchor=tk.CENTER, fill=tk.X, expand=1)
        rightFrame.pack(side=tk.RIGHT, fill=tk.X, expand=True, ipadx=10, ipady=10)
        compareBtn.config(command=lambda: self.compare(controller, (compareBtn, backBtn)))


    @classmethod
    def initData(cls, self, data):
        cls.data = data
        self.setData()

    
    def setData(self):
        self.userVar.set(ResultFrame.data[0])
        self.classVar.set(ResultFrame.data[1])
        self.gradeVar.set(ResultFrame.data[3])
        self.scoreVar.set(ResultFrame.data[4])
        self.percentVar.set(ResultFrame.data[5])


    def compare(self, controller, btns):
        if not self.COMPARING:
            self.COMPARING = True

            for btn in btns:
                btn.config(state=tk.DISABLED)

            controller.compareWin(self, controller, controller.id, btns)
