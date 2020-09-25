#!python3
import re
import requests
import time
import os
import io
import getpass
from requests import get
from bs4 import BeautifulSoup

#######################Methods######################################
def link_list(index):
  d={}
  #modify the index into book
  book=index.replace("http://gravitytales.com", '').replace("/chapters",'')
  #getting website into variable
  r=requests.get(index)
  soup = BeautifulSoup(r.content, 'html.parser')
  links = soup.find_all('a')

#adding individual urls into the listl
  for link in links:
    #print (link)
    if (book) in (link.get("href")):
        #dictionary made holds link and chapter name
      d[link.get("href")] = link.get_text()
  print(book+" dictionary created")
  time.sleep(1)
  return d
##########################################
def get_content(url):
  r = requests.get(url)
  soup = BeautifulSoup(r.content, 'html.parser')
  content=soup.find_all("div","fr-view")
  #print("Chapter obtained")
  return (max(content, key=len).get_text())

def Scrapper(index):
    ##########this part makes the book folder######################################
    book=(index.replace("http://gravitytales.com/novel/", '').replace("/chapters",""))
    #Change path to whatever you desire
    #print("drag and drop targeted folder here")
    path = '/Users/{}/OneDrive/Documents/LightNovels/'.format(getpass.getuser())+'{}'.format(book)
    if not os.path.isdir(path):
        os.mkdir(path)
    ##############################################33333

    d=link_list(index)

    for key in d:
      body=" "
      newPath= (d[key])
      newPath=newPath.strip()
      newPath=newPath.replace(":"," ")
      newPath=newPath.replace("?"," ")
      newPath=newPath.replace('"'," ")
      newPath=newPath.replace('*'," ")
      newPath=newPath.replace('/p>'," ")
      newPath=newPath.replace('/',"-")
      newPath=newPath.replace('>'," ")
      newPath=newPath.replace('<'," ")
      newPath+=".txt"

      if not os.path.isfile(path + '/' + newPath):
        try:
            body=get_content(key)
            body=re.sub('<.*?>', ' ', body)
            body=body.replace("Previous Chapter", "")
            body=body.replace("Next Chapter", "")
            body=body.replace("PreviousChapter", "")
            body=body.replace("NextChapter", "")
            file = open(path + '/' +newPath, 'w', encoding="utf-8")
            file.write(body)
            file.close()
            print(path)
            #print(d[key]+"has been made")
            #time.sleep(3)
            print("-----------------------------------------")
        except:
            print("There is a broken chapter on "+newPath)
            pass
      #else:
        #print(d[key]+"exsists")
#####################################
choice=0
while choice != "3":
    print("----------------------------GravityTales Scrapper----------------------------")
    choice=input("What would you like to do?\n1) Update chapters \n2) Add a new book to index\n3) Quit")
    print("---------------------------------------------------------------------------")
    if choice == "1":
        List = open("GravityIndex.txt").read().splitlines()
        for i in List:
            Scrapper(i)
        # get text file and make the srapper work

    if choice =="2":
        #add a way t edit textfile menue
        ind=input("Please enter the novel url")
        Scrapper(ind)
