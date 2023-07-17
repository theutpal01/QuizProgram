# \Frames\Both\LoginFrame.py

import tkinter as tk
from include.constants import *


class LoginFrame(tk.Frame):
    def __init__(self, parent: tk.Frame, controller: tk.Tk):
        tk.Frame.__init__(self, parent)

        self.id = tk.StringVar(self, None)
        self.pwd = tk.StringVar(self, None)
        self.configure(background=P_COL)

        leftFrame = tk.Frame(self, width=(WIN_W // 2), height=WIN_H, background=P_COL)

        image = tk.PhotoImage(file=PRI_IMG)
        imageLbl = tk.Label(
            leftFrame, image=image, width=(WIN_W // 2), background=P_COL
        )
        imageLbl.place(in_=leftFrame, relx=0.5, rely=0.5, anchor="center")
        imageLbl.photo = image

        credit = tk.Label(
            leftFrame,
            text="Developed By: Utpal",
            font=(FONT_FAM, VSM_FONT_SIZE),
            background=P_COL,
            foreground=TXT_COL,
        )
        credit.place(relx=0.5, rely=0.96, anchor="center")

        leftFrame.pack(side=tk.LEFT, ipadx=5, ipady=5, fill=tk.BOTH, expand=True)

        rightFrame = tk.Frame(self, width=(WIN_W // 2), height=WIN_H, background=P_COL)

        heading = tk.Label(
            rightFrame,
            text="Login Pannel",
            font=(FONT_FAM, FONT_SIZE_HEADING),
            background=P_COL,
            foreground=TXT_COL,
        )
        heading.pack(pady=(0, 30))

        inputFrame = tk.Frame(rightFrame, padx=5, background=P_COL)
        userLbl = tk.Label(
            inputFrame,
            text="Enter your user id:",
            font=(FONT_FAM, SM_FONT_SIZE),
            anchor=tk.W,
            background=P_COL,
            foreground=TXT_COL,
        )
        userLbl.pack(pady=2, fill=tk.X)
        userid = tk.Entry(
            inputFrame, textvariable=self.id, font=(FONT_FAM, FONT_SIZE), width=25
        )
        userid.pack(pady=2, fill=tk.X)

        dummyLbl = tk.Label(inputFrame, background=P_COL)
        dummyLbl.pack(pady=5, fill=tk.X)

        passwordLbl = tk.Label(
            inputFrame,
            text="Enter your password:",
            font=(FONT_FAM, SM_FONT_SIZE),
            anchor=tk.W,
            background=P_COL,
            foreground=TXT_COL,
        )
        passwordLbl.pack(pady=2, fill=tk.X)
        password = tk.Entry(
            inputFrame,
            show="*",
            textvariable=self.pwd,
            font=(FONT_FAM, FONT_SIZE),
            width=25,
        )
        password.pack(pady=2, fill=tk.X)
        inputFrame.pack(pady=5, padx=30, fill=tk.X, expand=1)

        submitFrame = tk.Frame(rightFrame, padx=10, background=P_COL)
        login = tk.Button(
            submitFrame,
            text="Sign In",
            font=(FONT_FAM, SM_FONT_SIZE),
            width=20,
            pady=5,
            command=lambda: controller.loginUser(),
            background=S_COL,
            foreground=TXT_COL,
            relief=tk.FLAT,
            bd=0,
        )
        login.pack(side=tk.RIGHT, padx=5, pady=5)
        login.bind("<Enter>", controller.hoverBtn)
        login.bind("<Leave>", controller.unhoverBtn)
        submitFrame.pack(padx=10, pady=5)

        rightFrame.pack(side=tk.LEFT, fill=tk.X, expand=True, ipadx=10, ipady=10)
