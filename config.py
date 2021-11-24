import sys,os,json
path=os.path.join(*sys.executable.split(os.sep),'xes_user_configs')
try:os.mkdir(path)
except:pass
class Config:
    pid=sys.argv[0].split(os.sep)[-1].split('/')[0]
    def __init__(self,name:str=''):
        try:os.mkdir(os.path.join(path,pid))
        except:pass
        self.path=os.path.join(path,pid,'')+name+'.json'
        try:self.attrs=json.load(open(self.path,'r'))
        except FileNotFoundError:
            with open(self.path,'w+') as f:pass
            self.attrs=dict()
    __getitem__=lambda self,key:self.attrs[key]
    def __setitem__(self,key,value):self.attrs[key]=value
    def __delitem__(self,key):del self.attrs[key]
    def save(self):
        f=open(self.path,'w+')
        f.write(json.dumps(self.attrs))
        f.close()
    def read(self):
        try:self.attrs=json.load(open(self.path,'r'))
        except FileNotFoundError:
            with open(self.path,'w+') as f:pass
            self.attrs=dict()
