#!python3
import os
import re
import sys
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    this is not mine
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False

choice1=yes_or_no("Is chapter name and number in the text files")
path=input("Drag novel folder here:")
list=(os.listdir(path))
list.sort(key=natural_keys)
name=input("Enter combined Name here:")

with open( name+".txt", 'w', encoding="utf-8" ) as result:
    for fname in list:
        print(path+"/"+fname)
        with open(path+"/"+fname, encoding="utf-8") as infile:
            if choice1 == False:
                result.write(fname.replace(".txt",""))
            result.write(infile.read())
            result.write("\n")




yes_or_no(" would you like to pretify the textfile? (y/n)")
file=input("please drag and drop original file: ")
newName=input("what is the new name of the file?")
#import plotly.plotly as py
with open(newName+".txt", "w", encoding="utf-8") as x:
    with open(file, encoding="utf-8") as f:
        for line in f:
            if not line.isspace():
                x.replace("’" ,"'")
                x.write(line)
