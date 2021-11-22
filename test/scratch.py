import threading as th
import time
import pygame
from pygame import*
from PIL import Image
from math import*
pygame.init()
class stage:
    def __init__(self,width=480,height=360):
        self.start_time=time.time()
        self.width=width
        self.height=height
        self.sprites=list()
        self.events=dict()
    def add_sprite(self,sprite:sprite):
        self.sprites.append(sprite)
    def run(self):
        for sprite in sprites:
            th.Thread(sprite.func).start()
            global screen
            screen=pygame.display.set_mode((self.width,self.height))
            while 1:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        exit()
                for sprite in sprites:
                    if sprite.show==True:
                        img=pygame.image.load(sprite.costumes[sprite.now_costumes])
                        i_x,i_y=Image.open(sprite.costumes[sprite.now_costumes]).size
                        x=sprite.x+self.width/2-i_x/2
                        y=self.height/2-sprite.y-i_y/2
                        screen.blit(img,(x,y))
                pygame.display.update()
class sprite:
    def __init__(self,x,y,direction=0,show=True):
        self.x=x
        self.y=y
        self.show=show
        self.direction=direction
        self.costumes={None:''}
        self.now_costumes=None
    def switch_costumes(self,name:str):
        self.now_costumes=name
    def add_costumes(self,name:str,image):
        self.costumes[name]=image
        self.now_costumes=name
    def bind(self,func):
        self.func=func
    def show(self):
        self.show=True
    def hide(self):
        self.show=False
    def go_to(self,x,y):
        self.x=x
        self.y=y
    def go_to_in(self,x,y,time=1,div=1/1000):
        s_time=time.time()
        s_x=self.x
        s_y=self.y
        steps=time/div
        moved=1
        while moved<=steps:
            if time.time()-s_time>moved*div:
                self.x=(x-s_x)*moved/steps+s_x
                self.y=(y-s_y)*moved/steps+s_y
                moved+=1
    def set(self,**namedata):
        keys=namedata.keys()
        if 'x' in keys:
            self.x=namedata['x']
        if 'y' in keys:
            self.y=namedata['y']
        if 'direction' in keys:
            self.direction=namedata['direction']
    def move_steps(self,steps:int):
        self.x+=sin(radians(self.direction))*steps
        self.y+=cos(radians(self.direction))*steps
    def _(self):
        pass
