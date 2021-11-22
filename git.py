import os
import __init__
def add(s:str):
    os.system('git add '+s)
def push(s:str):
    os.system('git push origin '+s)
def remote(s:str):
    os.system('git remote '+s)
def pull(s:str):
    os.system('git pull '+s)
if __name__=='__main__':
    os.system('git add .')
    os.system('git commit -m "%s"'%__init__.__version__)
    os.system('git push lib main')
