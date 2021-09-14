import re
from re import match
class my(str):
    def get(self,to_match):
        if self=='' or to_match=='':
            raise Exception(r"UseError:You can't use it like that")
        else:
            a=match('<'+to_match+'>',self)
            for i in range(a.index('<'+to_match+'>')):
                i=a.pop(index=i)
            a=match('</'+to_match+'>',a)
            return a[0]
