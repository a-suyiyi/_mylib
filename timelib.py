from re import*
from tkinter import*
from time import*
from bs4 import*
import sys
class xml:
    def __init__(self,s:str):
        self.string=BeautifulSoup(s,'xml')
    def get(self,keyword,**kwargs):
        return self.string.find_all(keyword,kwargs)
def log_in():
    global use
    use=Tk()
    use.geometry('500x300')
    b=Label(use,text='用户名')
    b.pack()
    name=Entry(use,show=None)
    name.pack()
    c=Label(use,text='密码')
    c.pack()
    password=Entry(use,show='*')
    password.pack()
    def a():
        if name.get()!='' and password.get()!='':
            use.quit()  
    to_log_in=Button(use,bg='green',text='登入',command=a)
    to_log_in.pack()
    use.mainloop()
    return [name.get(),password.get()]
r_print=print
def print(*text:str,time=0.1,sign=[None],special={}):
    for _text in text:
        for i,t in enumerate(_text):
            if i in special.keys():
                _sign=special[i]
            elif str(i) in special.keys():
                _sign=special[str(i)]
            else:
                _sign=sign[i%len(sign)]
            if _sign=='r':
                sys.stdout('\033[31m'+t)
            elif _sign=='g':
                sys.stdout('\033[32m'+t)
            elif _sign=='b':
                sys.stdout('\033[34m'+t)
            elif _sign=='y':
                sys.stdout('\033[33m'+t)
            elif _sign==None:
                sys.stdout('\033[0m'+t)
            elif _sign=='w':
                sys.stdout('\033[0m'+t)
            elif _sign.isdecimal()==True:
                sys.stdout('\033[{}m'.format(_sign)+t)
            sleep(time)
    sys.stdout('\n')
