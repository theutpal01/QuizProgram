# \Frames\Both\AuthFrame.py

import tkinter as tk
from tkinter import ttk
from include.constants import *


class RegisterFrame(tk.Frame):
    def __init__(self, parent: tk.Frame, controller: tk.Tk):
        tk.Frame.__init__(self, parent)

        self.id = tk.StringVar(self, None)
        self.name = tk.StringVar(self, None)
        self.classVal = tk.StringVar(self, "None")
        self.pwd = tk.StringVar(self, None)
        self.confPwd = tk.StringVar(self, None)
        self.configure(background=P_COL)

        leftFrame = tk.Frame(self, width=(WIN_W // 2), height=WIN_H, background=P_COL)

        image = tk.PhotoImage(file=PRI_IMG)
        imageLbl = tk.Label(
            leftFrame, image=image, width=(WIN_W // 2), background=P_COL
        )
        imageLbl.place(relx=0.5, rely=0.5, anchor="center")
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
            text="Register Pannel",
            font=(FONT_FAM, FONT_SIZE_HEADING),
            background=P_COL,
            foreground=TXT_COL,
        )
        heading.pack(pady=(0, 30))

        inputFrame = tk.Frame(rightFrame, padx=5, background=P_COL)
        
        useridLbl = tk.Label(
            inputFrame,
            text="Enter a user id:",
            font=(FONT_FAM, SM_FONT_SIZE),
            anchor=tk.W,
            background=P_COL,
            foreground=TXT_COL,
        )
        useridLbl.pack(pady=2, fill=tk.X)
        userid = tk.Entry(
            inputFrame, textvariable=self.id, font=(FONT_FAM, FONT_SIZE), width=25
        )
        userid.pack(pady=2, fill=tk.X)
        
        userLbl = tk.Label(
            inputFrame,
            text="Enter a name:",
            font=(FONT_FAM, SM_FONT_SIZE),
            anchor=tk.W,
            background=P_COL,
            foreground=TXT_COL,
        )
        userLbl.pack(pady=2, fill=tk.X)
        username = tk.Entry(
            inputFrame, textvariable=self.name, font=(FONT_FAM, FONT_SIZE), width=25
        )
        username.pack(pady=2, fill=tk.X)
        
        classLbl = tk.Label(
            inputFrame,
            text="Select a class:",
            font=(FONT_FAM, SM_FONT_SIZE),
            anchor=tk.W,
            background=P_COL,
            foreground=TXT_COL,
        )
        classLbl.pack(pady=2, fill=tk.X)
        classBox = ttk.Combobox(
            inputFrame, textvariable=self.classVal, font=(FONT_FAM, FONT_SIZE), values=CLASSES, state="readonly", width=25
        )
        classBox.pack(pady=2, fill=tk.X)

        # Set an initial value for the select box
        classBox.set("None")

        passwordLbl = tk.Label(
            inputFrame,
            text="Enter a password:",
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
        
        confPasswordLbl = tk.Label(
            inputFrame,
            text="Re-enter your password:",
            font=(FONT_FAM, SM_FONT_SIZE),
            anchor=tk.W,
            background=P_COL,
            foreground=TXT_COL,
        )
        confPasswordLbl.pack(pady=2, fill=tk.X)
        confPassword = tk.Entry(
            inputFrame,
            show="*",
            textvariable=self.confPwd,
            font=(FONT_FAM, FONT_SIZE),
            width=25,
        )
        confPassword.pack(pady=2, fill=tk.X)
        inputFrame.pack(pady=5, padx=30, fill=tk.X, expand=True)

        submitFrame = tk.Frame(rightFrame, padx=10, background=P_COL)
        self.registerBtn = tk.Button(
            submitFrame,
            text="Sign Up",
            font=(FONT_FAM, SM_FONT_SIZE),
            width=11,
            pady=5,
            command=lambda: controller.registerUser(),
            background=S_COL,
            foreground=TXT_COL,
            relief=tk.FLAT,
            bd=0,
        )
        self.registerBtn.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
        self.registerBtn.bind("<Enter>", controller.hoverBtn)
        self.registerBtn.bind("<Leave>", controller.unhoverBtn)
        
        self.bulkRegisterBtn = tk.Button(
            submitFrame,
            text="Bulk Register",
            font=(FONT_FAM, SM_FONT_SIZE),
            width=11,
            pady=5,
            command=lambda: controller.bulkRegister((self.registerBtn, self.bulkRegisterBtn)),
            background=S_COL,
            foreground=TXT_COL,
            relief=tk.FLAT,
            bd=0,
        )
        self.bulkRegisterBtn.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
        self.bulkRegisterBtn.bind("<Enter>", controller.hoverBtn)
        self.bulkRegisterBtn.bind("<Leave>", controller.unhoverBtn)
        submitFrame.pack(padx=10, pady=5, fill=tk.X, expand=True)

        rightFrame.pack(side=tk.LEFT, fill=tk.X, expand=True, ipadx=10, ipady=10)
