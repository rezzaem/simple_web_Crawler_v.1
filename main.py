#Librarys
from msvcrt import getch
from time import sleep
from os import system
from bs4 import BeautifulSoup
from urllib.request import urlopen

#--------------------------------------------------------------
system("cls")
print("""
██████╗░███████╗███████╗░█████╗░░█████╗░░░░███████╗███╗░░░███╗
██╔══██╗██╔════╝╚════██║██╔══██╗██╔══██╗░░░██╔════╝████╗░████║
██████╔╝█████╗░░░░███╔═╝███████║███████║░░░█████╗░░██╔████╔██║
██╔══██╗██╔══╝░░██╔══╝░░██╔══██║██╔══██║░░░██╔══╝░░██║╚██╔╝██║
██║░░██║███████╗███████╗██║░░██║██║░░██║██╗███████╗██║░╚═╝░██║
╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝╚═╝░░░░░╚═╝
->simple Web Crawler
->coded by Reza Emamhasani
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
""")
sleep(3)
#------------------------------------------------------------
def main (x):
    #catigorys
    art =["theatre","music","film","movie","paint","art"]
    sport=["world cup","tennis","basketball","ball","football"]
    computer = ["Microsoft","apple","software","hardware","iPhone","dell","desktop","laptop"]
    buss=["finance","payment","sale","tax","bank","stock market","business"]
    #object_counter
    art_c=0
    sport_c=0
    computer_c=0
    bus_c=0
    word_c=0
    for i in x : # for each index in main list
        i=i.lower() # if there is any capital , it cames to small for counting
        i=i.split() # split the string to list of words

        for a in i : #for each word in list
             # if word is in catigory
            if a in art:
                art_c+=1
            elif a in sport:
                sport_c+=1
            elif a in computer:
                computer_c+=1
            elif a in buss:
                bus_c+=1
                
            if a not in [" ",",",".","*","-"]: # word counting
                word_c+=1

    #find main catigory        
    max=art_c
    max_name="" 
    if sport_c>max:
        max=sport_c
        max_name="sport"
    if computer_c>max:
        max=computer_c
        max_name="computer"
    if bus_c>max:
        max=bus_c
        max_name="business"
    if max==0:
        max_name="other"                    

    return (f"counts of all word :{word_c}\n--------\nart :{art_c}\nsport :{sport_c}\ncomputer :{computer_c}\nbusiness :{bus_c}\n--------\ncatigory of this site is :{max_name}")        

def link_to_text(link):
    html = urlopen(link).read() # open the url and read it
    soup = BeautifulSoup(html,"lxml") #parsed and scraped the file (html) with Beautiful Soup with format of lxml .notice : can use format of html.parser or lxml
    for script in soup(["script", "style"]): # remove all <script> and <style> tags
       script.decompose()

    return( list(soup.stripped_strings))  # get all the text in the file . notice : this is a list of strings

try :
    lst_txt=link_to_text(input("please Enter the link look like this -> (https://abcdefg.com) : "))
    print("--------")
    print(main(lst_txt))
    getch()
except :
    system("cls")
    print("there is some error , please try again ")
    print("note : may the link is incorrect or the site is unreadable ")