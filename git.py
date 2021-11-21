import os
import __version__
def upload():
    os.system('git add .')
    os.system('git commit -m "%s"'%__version__.__version__)
    os.system('git push lib main')
if __name__=='__main__':upload()
