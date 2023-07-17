# \include\constants.py
from cryptography.fernet import Fernet

# WINDOWS CONFIGURATION
WIN_W, WIN_H = 900, 600
WIN_T = "Quiz Application"


# COLOR CONFIGURATION
BLACK = "#000000"
P_COL = "#0D1A1C"
S_COL = "#2E3532"
T_COL = "#7E9181"
TXT_COL = "#FFFFFF"


# PATH CONFIGURATIONS
PRI_IMG = "assets/quizImg.png"
GRADE_IMG = "assets/grade.png"


# FONT CONFIGURATION
FONT_FAM = "Arial"
GRADE_FONT = 54
FONT_SIZE_HEADING = 32
FONT_SIZE = 17
SM_FONT_SIZE = 15
VSM_FONT_SIZE = 12


# MYSQL CONFIGURATION
CONN_FILE = "include/db.bin"
CONN = [None, None, None]

DB = "quizdb"
AUTH_TABLE = "auth"
RESULT_TABLE = "result"
QUIZ_TABLE = "quiz"


# OTHERS
KEY = b'G1pSKvWMH1mWPdKSJ5pbNsqpzXZ2q3wX9iPTOmGrsYk='
CLASSES = [
    "None",
    "I A", "I B",
    "II A", "II B",
    "III A", "III B",
    "IV A", "IV B",
    "V A", "V B", 
    "VI A", "VI B", 
    "VII A", "VII B", 
    "VIII A", "VIII B", 
    "IX A", "IX B", 
    "X A", "X B", 
    "XI A", "XI B", 
    "XII A", "XII B"
]