# \Frames\Admin\AdminFrame.py

import tkinter as tk
from include.constants import *


class AdminFrame(tk.Frame):
    def __init__(self, parent: tk.Frame, controller: tk.Tk):
        tk.Frame.__init__(self, parent)
        self.configure(background=P_COL) 

        leftFrame = tk.Frame(self, width=(WIN_W // 2), height=WIN_H, background=P_COL)
        image = tk.PhotoImage(file=PRI_IMG)
        imageLbl = tk.Label(leftFrame, image=image, width=(WIN_W // 2), background=P_COL)
        imageLbl.photo = image
        imageLbl.place(in_=leftFrame, anchor=tk.CENTER, relx=0.5, rely=0.5)
        
        credit = tk.Label(
            leftFrame,
            text="Developed By: Utpal",
            font=(FONT_FAM, VSM_FONT_SIZE),
            background=P_COL,
            foreground=TXT_COL,
        )
        credit.place(relx=0.5, rely=0.96, anchor="center")
        
        leftFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, ipadx=10, ipady=10)
    
        rightFrame = tk.Frame(self, width=(WIN_W // 2), height=WIN_H, background=P_COL)
    
        headFrame = tk.Frame(rightFrame, background=P_COL)
        self.test = True
        
    
        questBtn = tk.Button(
            headFrame, 
            text="Quiz Question Management", 
            font=(FONT_FAM, FONT_SIZE), 
            padx=10, 
            pady=5, 
            background=S_COL, 
            foreground=TXT_COL, 
            relief=tk.FLAT, 
            bd=0, 
            width=25, 
            command=lambda: controller.showQuizDetails()
            )
        questBtn.pack(padx=15, pady=15, anchor=tk.W)
        questBtn.bind('<Enter>', controller.hoverBtn)
        questBtn.bind('<Leave>', controller.unhoverBtn)
    
        resultBtn = tk.Button(
            headFrame, 
            text="Result Management", 
            font=(FONT_FAM, FONT_SIZE), 
            padx=10, pady=5, background=S_COL, 
            foreground=TXT_COL, 
            relief=tk.FLAT, 
            bd=0, 
            width=25, 
            command=controller.showUserDetails
            )
        resultBtn.pack(padx=15, pady=15, anchor=tk.W)
        resultBtn.bind('<Enter>', controller.hoverBtn)
        resultBtn.bind('<Leave>', controller.unhoverBtn)
        
        exportResultBtn = tk.Button(
            headFrame, 
            text="Export Result Data", 
            font=(FONT_FAM, FONT_SIZE), 
            padx=10, pady=5, background=S_COL, 
            foreground=TXT_COL, 
            relief=tk.FLAT, 
            bd=0, 
            width=25, 
            command=controller.exportResults
            )
        exportResultBtn.pack(padx=15, pady=15, anchor=tk.W)
        exportResultBtn.bind('<Enter>', controller.hoverBtn)
        exportResultBtn.bind('<Leave>', controller.unhoverBtn)
        
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
            width=25, 
            command=controller.logout
            )
        logoutBtn.pack(padx=15, pady=15, anchor=tk.W)
        logoutBtn.bind('<Enter>', controller.hoverBtn)
        logoutBtn.bind('<Leave>', controller.unhoverBtn)
        headFrame.pack(anchor=tk.CENTER)

        rightFrame.pack(side=tk.RIGHT, fill=tk.X, expand=True, ipadx=10, ipady=10)
