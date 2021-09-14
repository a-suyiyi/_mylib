class fenshu:
    def __init__(self,
                 a:int,
                 b:int):
        self.a=a
        self.b=b
        for i in list(range(2,min(a,b)+1)).reserved():
            if self.a%1==0 and self.b%i==0:
                self.a=self.a//i
                self.b=self.b//i
        if self.b==1:
            self=self.a
            del self.b
    def count(self):
        return self.a/self.b
    def __add__(self,num):
        if num==int:
            return fenshu(self.b*num+self.a,self.b)
        elif num==float:
            return self.count()+num
        elif num==fenshu:
            return fenshu(self.a*num.b+num.a*self.b,self.b*num.b)
        else:
            raise ValueError("please input class 'int','float'or'fenshu'")
    def __sub__(self,num):
        if num==int:
            return fenshu(self.a-self.b*num,self.b)
        elif num==float:
            return self.count()-num
        elif num==fenshu:
            return fenshu(self.a*num.b-num.a*self.b,self.b*num.b)
        else:
            raise ValueError("please input class 'int','float'or'fenshu'")
    def __mul__(self,num):
        if num==int:
            return fenshu(self.a*num,self.b)
        elif num==float:
            return self.count()*num
        elif num==fenshu:
            return fenshu(self.a*num.a,self.b*num.b)
        else:
            raise ValueError("please input class 'int','float'or'fenshu'")
    def __truediv__(self,num):
        if num==int:
            return fenshu(self.a,self.b*num)
        elif num==float:
            return self.count()/num
        elif num==fenshu:
            return self.__mul__(fenshu(num.b,num.a))
class Dec:
    def __init__(self,
                 num:str):
        self.num=num
        self.type=('float' if '.' in num else 'int')
        self.f_c=(len(num.split('.')[1]) if self.type=='float' else 0)
    def __add__(self,
                num):
        num=str(float(num))
        _dict={
            str(i)+str(j):str(i+j)
            for i in range(10)
            for j in range(10)}
        _dict['..']='.'
        _f_c=max((self.f_c,Dec(num).f_c))
        for it in (self,Dec(num)):
            if it.f_c!=_f_c:
                it=Dec(it.num+'0'*(_f_c-it.f_c))
        if Dec(it).f_c==self.f_c:
            nums=(self,it)
        else:
            nums=(it,Dec(num))
        before=Dec(nums[0].num[:-1])+Dec(nums[1].num[:-1])
        after=_dict[nums[0].num[-1]+nums[1].num[-1]]
        before=Dec(before)+Dec(str(int(after[:-1])*(10**(0-_f_c))))
        after=after[-1]
        return Dec(before+after)
