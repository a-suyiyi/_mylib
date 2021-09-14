from tools import case,swich,lmap
class world_frame:
    def __init__(self,id_:int,high=60):
        self.dixing={0:None,
            1:'glass',
            2:'hill'
            }
        self.type_=self.dixing[id_]
        self.high=high
        self.to()
    def to(self):
        swich(self.type_)
        if case('glass'):
            return [[1+self.high for j in range(3)] for i in range(3)]
        elif case('hill'):
            return lmap(lambda x:x+self.high,[
                [1,2,1],
                [2,3,2],
                [1,2,1]
                ])
        elif case(None):
            return [[0 for j in range(3)] for i in range(3)]
