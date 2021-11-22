
class array:
    __doc__='''\
array(value)-> array object
array()-> new empty array object
'''
    def __init__(self,value:list=[0]):
        self.w=len(value)
        self.v=value
    def __mul__(self,a):
        pass
    __getitem__=lambda self:self.v.__getitem__
    def __add__(self,a):
        arr=array()
        arr.w=self.w
        arr.v=self.v
        for i in range(len(arr.v)):arr.v[i]+=a
        return arr
    __radd__=lambda self,a:self.__add__(a)
    __sub__=lambda self,a:self.__add__(0-a)
    __rsub__=lambda self,a:self.__sub__(a)
    __rmul__=lambda self,a:self.__mul__(a)
    def __repr__(self):
        if self.w<=6:return str(self.v)
        return '[\n'+',\n'.join(map(repr,self.v[0:3]))+'\n...\n'+',\n'.join(map(repr,self.v[-3:]))+'\n]\n'
#####

