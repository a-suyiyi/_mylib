from urllib.request import*
from bs4 import*
class xes_people:
    def __init__(self,id:int):
        headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)AppleWebKit 537.36 (KHTML, like Gecko) Chrome","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
        self.id=id
        self.mainpage=BeautifulSoup(urlopen(Request('https://code.xueersi.com/space/'+str(self.id),headers=headers)))
        self.name=self.mainpage.find_all('div',class_='user-name').span[0][-10:-6].replace('>','')
        self.description=self.mainpage.find_all('div',class_='user-description').span.get_text()
        self.count_fans=self.mainpage.find_all('div',class_='user-fans_cont').find_all('span')[1].get_text()
        self.count_focus=self.mainpage.find_all('div',class_='user-focus_count').find_all('span')[1].get_text()
    def setid(self,id:int):
        self.__init__(id)
    
