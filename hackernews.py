import requests
import pyfiglet as fig
from bs4 import BeautifulSoup



def filter(ln,st):
    hn=[]
    for i,data in enumerate(ln):
        title=data.getText()
        link=data.get('href',None)
        score = int(st[i].select('.score')[0].getText().split(' ')[0]) if len(st[i].select('.score')[0]) else None
        if score>100:
            hn.append({'title':title,'link':link,'score':score})
    return hn


def sortdata(data):
    return sorted(data,key=lambda k:k['score'],reverse=True)


def hackernews(data):
    print("    Today's rated Headlines: \n")
    for i,news in enumerate(data):
        print(f"{i+1}) {news['title']}   |  (score: {news['score']})\nread in:- {news['link']}")
        print("\n\n")

def main():
    print(fig.figlet_format(text="   Hacker  News", font="slant"))
    print(fig.figlet_format("       ( Highly voted news )", font="threepoint"))
    print("                                    By - V A I B H A V   H A S W A N I\n")
    try:
        res = requests.get("https://news.ycombinator.com/")
        res2=requests.get("https://news.ycombinator.com/news?p=2")
        mainres=res.text+res2.text
        soup = BeautifulSoup(mainres, "html.parser")
        sub = soup.select('.subtext')
        links = soup.select('.storylink')
        fdata=filter(links,sub)
        hackernews(sortdata(fdata))
    except:
        print("\n\n   ..... Please Check the internet connection .....")

if __name__=='__main__':
    main()

