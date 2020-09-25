import re
import requests
import time
import os
import io
import getpass
from requests import get
from bs4 import BeautifulSoup

#variables

#pip install lxml
def Logger(input):
    with open("log.txt","a") as file:
        file.write(input+"\n")
#getting the story table of contents
def get_Index(URL):
    Logger("METHOD: get_index Ran")
    r=get(URL)
    #Logger("r.content: "+str(r.content))
    #soup = BeautifulSoup(r.content, 'xml')

    soup = BeautifulSoup(r.content, 'lxml')
    Logger("ran")
    #for i in soup.find_all("p"):
    story = soup.find_all("dd")
    #story = soup.find_all("a")
    title=soup.find_all("h1")
    x1=title[0].get_text()
    x1=x1.replace(" ","-")
    #x1=x1.replace("?","-")
    Index={}
    for i in story:
        re1='.*?'	# Non-greedy match on filler
        re2='(\\d+)'	# Integer Number 1
        rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)
        m = rg.search(str(i))
        i_chapters=m.group(1)+".html"
        key="https://www.wuxiaworld.co/"+x1+"/"+i_chapters
        Index[key] = (i.get_text())
    return Index

#getting the story
def create_chapter(C_URL,path,newPath):
    r=get(C_URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    story=soup.find_all("div")
    _x1=soup.find("div", { "id" : "content" })
    file = open(path + '/' +newPath+".txt", 'w', encoding="utf-8")
    for i in _x1:
        if "br" in str(i):
            pass
        elif "Translator" in str(i) and "Editor" in str(i):
            pass
        elif "<script>" in str(i):
            pass
        else:
            file.write(i)
    file.close()

def Worker(I_URL):
    Logger("METHOD Worker started")
    book=(I_URL.replace("https://www.wuxiaworld.co/", '').replace("/",""))
    Logger("I_URL: "+ str(I_URL))
    #replace this
    path = '/Users/topsn/Desktop/LightNovels'.format(getpass.getuser())+'{}'.format(book)
    if not os.path.isdir(path):
        path=path.replace("\t","")
        os.mkdir(path)
        Logger(" Directory created: "+ str(path))
    Index = get_Index(I_URL)
    print("---------------------------------------")
    print(book)
    print("---------------------------------------")
    for key in Index:
        newPath= (Index[key])
        newPath=newPath.strip()
        newPath=newPath.replace(":"," ")
        newPath=newPath.replace("?"," ")
        newPath=newPath.replace('"'," ")
        newPath=newPath.replace('*'," ")
        newPath=newPath.replace('/',"-")
        newPath=newPath.replace('>',"")
        newPath=newPath.replace('<',"")
        newPath=newPath.replace("|","")
        newPath=newPath.replace("\t","")
        newPath=newPath.replace("’"," ' ")
        newPath=newPath.replace("Find authorized novels in Webnovel，faster updates, better experience，Please click www.webnovel.com  for visiting."," ' ")

        if not os.path.isfile(path + '/' + newPath+".txt"):
            print(newPath)
            create_chapter(key,path,newPath)
        else:
            pass
    #print(Index)
#    for i in soup.find_all("p"):
    #print(soup.get_text())




#URL="https://www.lightnovelbastion.com/release.php?p=275"
#C_URL="https://www.wuxiaworld.co/Super-Gene/1118481.html"
#C_URL="https://www.wuxiaworld.co/Library-of-Heaven-is-Path/1049179.html"
C_URL="https://www.wuxiaworld.co/Super-Gene/1118482.html"

#indexe
#URL="https://www.wuxiaworld.co/Super-Gene/"
I_URL = "https://www.wuxiaworld.co"

#Worker(I_URL)


####################################
choice=0

while choice != "3":
    print("----------------------------Wuxiaworld Scrapper----------------------------")
    choice=input("What would you like to do?\n1) Update chapters \n2) Add a new book to index\n3) Quit\n")
    print("---------------------------------------------------------------------------")
    if choice == "1":
        List = open("QidanIndex.txt").read().splitlines()
        for i in List:
            Worker(i)
        # get text file and make the srapper work

    if choice =="2":
        #add a way t edit textfile menue
        ind=input("Please enter the novel url")
        Worker(ind)

#get_Index(URL)

#print(Index)
