# Frames/User/QuizFrame.py

import tkinter as tk
from include.constants import *


class QuizFrame(tk.Frame):
    data = None
    index = 0
    maxLen = None
    uAnswers = None


    def __init__(self, parent: tk.Frame, controller: tk.Tk):
        tk.Frame.__init__(self, parent)
        self.configure(background=P_COL)
        self.answer = tk.StringVar(self, "     ")

        leftFrame = tk.Frame(self, background=P_COL)
        self.prevBtn = tk.Button(
            leftFrame, 
            text="<", 
            font=(FONT_FAM, FONT_SIZE), 
            padx=5, 
            background=S_COL, 
            foreground=TXT_COL, 
            relief=tk.FLAT, 
            bd=0)
        self.prevBtn.pack(fill=tk.Y, expand=True)
        self.prevBtn.bind('<ButtonRelease-1>', self.updateIndex)
        self.bind('<KeyRelease-Left>', self.updateIndex)
        self.prevBtn.bind('<Enter>', controller.hoverBtn)
        self.prevBtn.bind('<Leave>', controller.unhoverBtn)
        leftFrame.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y)
        

        middleFrame = tk.Frame(self, padx=20, pady=5, bg="white", background=P_COL)
        self.questionLbl = tk.Label(
            middleFrame, 
            background=P_COL, 
            foreground=TXT_COL, 
            text="Question 1", 
            font=(FONT_FAM, FONT_SIZE), 
            wraplength=600, 
            justify=tk.LEFT)
        self.questionLbl.pack(anchor=tk.W, pady=30)
        
        options = tk.Frame(middleFrame, background=P_COL, padx=10, pady=10)
        self.option1 = tk.Radiobutton(
            options, 
            background=P_COL, 
            foreground=TXT_COL, 
            selectcolor=S_COL, 
            text="", 
            value="", 
            variable=self.answer, 
            font=(FONT_FAM, FONT_SIZE), 
            relief=tk.FLAT, 
            border=0, 
            command=self.updateAnswer)
        self.option1.pack(anchor=tk.W, pady=5)
        
        self.option2 = tk.Radiobutton(
            options, 
            background=P_COL, 
            foreground=TXT_COL, 
            selectcolor=S_COL, 
            text="", 
            value="", 
            variable=self.answer, 
            font=(FONT_FAM, FONT_SIZE), 
            relief=tk.FLAT, 
            border=0, 
            command=self.updateAnswer)
        self.option2.pack(anchor=tk.W, pady=5)
        
        self.option3 = tk.Radiobutton(
            options, 
            background=P_COL, 
            foreground=TXT_COL, 
            selectcolor=S_COL, 
            text="", 
            value="", 
            variable=self.answer, 
            font=(FONT_FAM, FONT_SIZE), 
            relief=tk.FLAT, 
            border=0, 
            command=self.updateAnswer)
        self.option3.pack(anchor=tk.W, pady=5)
        
        self.option4 = tk.Radiobutton(
            options, 
            background=P_COL, 
            foreground=TXT_COL, 
            selectcolor=S_COL, 
            text="", 
            value="", 
            variable=self.answer, 
            font=(FONT_FAM, FONT_SIZE), 
            relief=tk.FLAT, 
            border=0, 
            command=self.updateAnswer)
        self.option4.pack(anchor=tk.W, pady=5)
        options.pack(padx=30, pady=20, anchor=tk.W)

        self.submitBtn = tk.Button(
            middleFrame, 
            text="Submit Your Test", 
            font=(FONT_FAM, FONT_SIZE), 
            padx=15, 
            pady=8, 
            background=S_COL, 
            foreground=TXT_COL, 
            relief=tk.FLAT, 
            bd=0, 
            command=lambda: self.submitQuiz(controller))
        self.submitBtn.pack(side=tk.BOTTOM, anchor=tk.CENTER, pady=20)
        self.submitBtn.bind('<Enter>', controller.hoverBtn)
        self.submitBtn.bind('<Leave>', controller.unhoverBtn)
        middleFrame.pack(side=tk.LEFT, anchor=tk.CENTER, fill=tk.BOTH, expand=True)
          
        rightFrame = tk.Frame(self, background=P_COL)
        self.nextBtn = tk.Button(
            rightFrame, 
            text=">", 
            font=(FONT_FAM, FONT_SIZE), 
            padx=5, 
            background=S_COL, 
            foreground=TXT_COL, 
            relief=tk.FLAT, 
            bd=0)
        self.nextBtn.pack(fill=tk.Y, expand=True)
        self.nextBtn.bind('<ButtonRelease-1>', self.updateIndex)
        self.bind('<KeyRelease-Right>', self.updateIndex)
        self.nextBtn.bind('<Enter>', controller.hoverBtn)
        self.nextBtn.bind('<Leave>', controller.unhoverBtn)
        rightFrame.pack(side=tk.RIGHT, anchor=tk.E, fill=tk.Y)

        self.changeStateUpdater()



    @classmethod
    def initData(cls, self, data):
        cls.index = 0
        cls.data = data
        cls.uAnswers = {}
        cls.maxLen = len(data) - 1
        self.setData(cls.data[cls.index][1])


    def updateIndex(self, event):
        if event.keysym in ["Left", "Right"]:
            if event.keysym == "Left" and self.prevBtn.cget("state") == "normal" and QuizFrame.index > 0:
                QuizFrame.index -= 1

            elif event.keysym == "Right" and self.nextBtn.cget("state") == "normal" and QuizFrame.index < QuizFrame.maxLen:
                QuizFrame.index += 1
        

        else:
            if event.widget['state'] == "active":
                if event.widget["text"] == "<" and QuizFrame.index > 0:
                    QuizFrame.index -= 1
                elif event.widget["text"] == ">" and QuizFrame.index < QuizFrame.maxLen:
                    QuizFrame.index += 1
        self.answer.set("    ")
        self.setData(QuizFrame.data[QuizFrame.index][1])

        self.changeStateUpdater()
        self.focus_set()


    def changeStateUpdater(self):
        if 0 < QuizFrame.index < QuizFrame.maxLen:
            self.prevBtn.config(state=tk.NORMAL)
            self.nextBtn.config(state=tk.NORMAL)
        
        elif QuizFrame.index == 0:
            self.prevBtn.config(state=tk.DISABLED)
            self.nextBtn.config(state=tk.NORMAL)
        
        elif QuizFrame.index == QuizFrame.maxLen:
            self.prevBtn.config(state=tk.NORMAL)
            self.nextBtn.config(state=tk.DISABLED)


    def updateAnswer(self):
        if self.answer.get not in QuizFrame.uAnswers.values():
            QuizFrame.uAnswers.update({QuizFrame.data[QuizFrame.index][1][0]: self.answer.get()})


    def setData(self, data):
        self.update_idletasks()

        if data[0] in QuizFrame.uAnswers.keys():
            self.answer.set(QuizFrame.uAnswers.get(data[0]))

        self.questionLbl["text"] = str(QuizFrame.index + 1) + ") " + str(data[0])
        self.option1["text"] = data[1]
        self.option2["text"] = data[2]
        self.option3["text"] = data[3]
        self.option4["text"] = data[4]
        self.option1["value"] = data[1]
        self.option2["value"] = data[2]
        self.option3["value"] = data[3]
        self.option4["value"] = data[4]


    @staticmethod
    def getGrade(percent:float):
        grade = None
        if 80 <= percent <= 100:
            grade = "A+"
        elif 75 <= percent < 80:
            grade = "A"
        elif 70 <= percent < 75:
            grade = "B"
        elif 60 <= percent < 90:
            grade = "C"
        elif 50 <= percent < 87:
            grade = "D"
        elif 40 <= percent < 83:
            grade = "E"
        elif percent < 40:
            grade = "F"
        return grade
    
    
    def submitQuiz(self, controller):


        maxScroe = len(QuizFrame.data)
        userScore = 0

        for quest in QuizFrame.data:
            if QuizFrame.uAnswers.get(quest[1][0]) == quest[1][5]:
                userScore += 1

        score = (str(userScore) + "/" + str(maxScroe))
        percentage = round((userScore / maxScroe) * 100, 2)
        grade = self.getGrade(percentage)
        percentage = str(percentage) + "%"

        if len(QuizFrame.uAnswers) < len(QuizFrame.data):
            if controller.box.showYesNoBox("Want to continue?", "All the questions are not answered! Do you wish to continue?"):
                controller.quizComplete(QuizFrame.uAnswers, score, percentage, grade)
            else: self.focus_set()
        else:
            controller.box.showBox("Info", "All the questions are answered! Quiz has been submitted.", "i")
            controller.quizComplete(QuizFrame.uAnswers, score, percentage, grade)
