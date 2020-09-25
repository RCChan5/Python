import re
import requests
import time
import os
import io
import getpass
from requests import get
from bs4 import BeautifulSoup
import pickle
from time import sleep


def logger(input):
    with open("QidanLog.txt","a") as file:
        file.write(input+"\n")


#when stating new run be sure to add to logger time

# print(os.getcwd())
# print(os.listdir())

#start up method
#makes/checks for settings file



#Global Variables
settingsCheck = False
#be surea / is at the end
##change this
LightNovelFolder = "/Users/topsn/Desktop/LightNovels/"
delay=1
Index_URL = "https://www.wuxiaworld.co"
C_URL="https://www.wuxiaworld.co/Super-Gene/1118482.html"

test_index = "https://www.wuxiaworld.co/My-Vampire-System/"
test_chapter = "https://www.wuxiaworld.co/My-Vampire-System/5064886.html"

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False
def startUpWithOption():
    if(os.path.isfile("QidanSettings.txt")):
        print("settings file exsist")
        #read the txt file and update gloabl variables
    else:
        if(yes_or_no("Do you want to create the settings file?")):
            with open("QidanSettings.txt", "w") as file:
            #create file here
                file.write("hello")
                print("create file here")
                settingsCheck = True
        else:
            print("Setting File creation canceled")

def startUp():
    choice = 0

    while choice != "3":
        print("----------------------------Wuxiaworld Scrapper----------------------------")
        choice = input("What would you like to do?\n1) Update chapters \n2) Add a new book to index\n3) Quit\n")
        print("---------------------------------------------------------------------------")
        if choice == "1":
            List = open("QidanIndex.txt").read().splitlines()
            for i in List:
                Worker(i)
            # get text file and make the srapper work

        if choice == "2":
            # add a way t edit textfile menue
            ind = input("Please enter the novel url")
            Worker(ind)

#This method takes the Novels index as its input and returns a list of all the novels chapters as a list
#update retunn a dictionary with a key value of url and name
def get_Index(URL):

    logger("METHOD: get_index Ran")
    r=get(URL)
    index={}
    soup = BeautifulSoup(r.content, 'lxml')

    #variable used to look for relevant links
    keyword=URL.replace("https://www.wuxiaworld.co","")

    #Grabs all possible links from index page and selects only those that contians the keyword
    for link in soup.find_all('a'):

        if keyword in str(link.get('href')):
            if link.get_text() != "READ":
                index["https://www.wuxiaworld.com/"+link.get("href")] = link.get_text()


    return index

#This method creates a text file from the inputed url
#this needs a url and a destination folder
def create_chapter(C_URL,path,chapter_name):
    r=get(C_URL)
    soup = BeautifulSoup(r.content, "html.parser")
    #title = (str(soup.title)).replace("<title>", "").replace("</title>", "").replace("_", " ").replace("- Wuxiaworld","").replace(chapter_name,"")

    soup=soup.find("div", class_="chapter-entity")#.get_text()
    story=""
    #maybe add a try except block here?
    for i in soup:
        if "br" in str(i):
            pass
        elif "<script>" in str(i):
            pass
        else:
            story+="\n"+str(i)
            pass
    file = open(path + '/' + chapter_name + ".txt", 'w', encoding="utf-8")
    file.write(story)


##takes index url
def Worker(Index_URL):
    #getting book name
    book = (Index_URL.replace("https://www.wuxiaworld.co/", '').replace("/", "")).replace("-"," ")
    path=LightNovelFolder+book

    #making the storys folder
    print(book+" is being updated")
    try:
        if not os.path.isdir(path):
            os.mkdir(path)
            logger(" Directory created: "+ str(book))
    except:
        logger("WORKER: did not create directory for "+str(book))

    #getting the index
    try:
        index=get_Index(Index_URL)
    except:
        logger("WORKER: Probelm when using the index method")

    #creating each book
    for url in index:
        try:
            create_chapter(url,path,book)

            print(book)
        except:
            logger("Worker: failed to create specific chapter"+url)
#handels the index and creates folders



#    for i in soup.find_all("p"):
    #print(soup.get_text())

#print(os.getcwd())

#print(os.path.isfile("QidanSettings.txt"))
#startUp()
print("==================TESTING SUITE START results shown here============================")
print(get_Index(test_index))
#print(create_chapter(test_chapter,"/Users/topsn/Desktop/Python Stuff","My Vampire System"))
#Worker(test_index)
#url , save location
#todo
#get index works
# create chapter
# worker
# overall running aloong with destination where to save
