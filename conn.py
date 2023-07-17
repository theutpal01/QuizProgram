from include.constants import CONN_FILE, CONN
from include.helper import saveData

def initConnction():
    global CONN
    host = input("Enter the hostname or ip: ")
    user = input("Enter the username: ")
    pwd = input("Enter the password: ")
    CONN = str([host, user, pwd])
    saveData(CONN_FILE, CONN)
    
    

if __name__ == '__main__':
    initConnction()