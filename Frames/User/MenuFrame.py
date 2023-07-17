# F\rames\User\MenuFrame.py

import tkinter as tk
from include.constants import *


class MenuFrame(tk.Frame):
    attempted = None

    def __init__(self, parent: tk.Frame, controller: tk.Tk):
        tk.Frame.__init__(self, parent)
        self.configure(background=P_COL)

        leftFrame = tk.Frame(self, width=(WIN_W // 2), height=WIN_H, background=P_COL)
        image = tk.PhotoImage(file=PRI_IMG)
        imageLbl = tk.Label(leftFrame, image=image, width=(WIN_W // 2), background=P_COL)
        imageLbl.photo = image
        imageLbl.place(in_=leftFrame, relx=0.5, rely=0.5, anchor="center")
        
        credit = tk.Label(
            leftFrame,
            text="Developed By: Utpal",
            font=(FONT_FAM, VSM_FONT_SIZE),
            background=P_COL,
            foreground=TXT_COL,
        )
        credit.place(relx=0.5, rely=0.96, anchor="center")
        
        leftFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, ipadx=5, ipady=5)
    
        rightFrame = tk.Frame(self, width=(WIN_W // 2), height=WIN_H, background=P_COL)
        headFrame = tk.Frame(rightFrame, background=P_COL)
    
        testBtn = tk.Button(
            headFrame, 
            text="Attempt The Test", 
            font=(FONT_FAM, FONT_SIZE), 
            padx=10, 
            pady=5, 
            background=S_COL, 
            foreground=TXT_COL, 
            relief=tk.FLAT, 
            bd=0, 
            width=20, 
            command=lambda: controller.playQuiz(MenuFrame.attempted))
        testBtn.pack(padx=15, pady=15, anchor=tk.W)
        testBtn.bind('<Enter>', controller.hoverBtn)
        testBtn.bind('<Leave>', controller.unhoverBtn)
    
        resBtn = tk.Button(
            headFrame, 
            text="Get Your Result", 
            font=(FONT_FAM, FONT_SIZE), 
            padx=10, 
            pady=5, 
            background=S_COL, 
            foreground=TXT_COL, 
            relief=tk.FLAT, 
            bd=0, 
            width=20, 
            command=controller.showResult)
        resBtn.pack(padx=15, pady=15, anchor=tk.W)
        resBtn.bind('<Enter>', controller.hoverBtn)
        resBtn.bind('<Leave>', controller.unhoverBtn)
    
        logoutBtn = tk.Button(
            headFrame, 
            text="Logout Quiz App", 
            font=(FONT_FAM, FONT_SIZE), 
            padx=10, 
            pady=5, 
            background=S_COL, 
            foreground=TXT_COL, 
            relief=tk.FLAT, 
            bd=0, 
            width=20, 
            command=controller.logout) 
        logoutBtn.pack(padx=15, pady=15, anchor=tk.W)
        logoutBtn.bind('<Enter>', controller.hoverBtn)
        logoutBtn.bind('<Leave>', controller.unhoverBtn)
        headFrame.pack(anchor=tk.CENTER)
        rightFrame.pack(side=tk.RIGHT, fill=tk.X, expand=True, ipadx=10, ipady=10)

    @classmethod
    def initData(cls, data:int):
        cls.attempted = data
