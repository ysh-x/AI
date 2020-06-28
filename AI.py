from gtts import gTTS
from PyDictionary import PyDictionary
from datetime import datetime
import requests
from googlesearch import search
from bs4 import BeautifulSoup
import subprocess
import random
import os

def Print(text):
     print('\t\t\t'+text)
     
def speak(text):
     speech = gTTS(text)
     speech.save('AI.mp3')
     return_code = subprocess.call(['afplay','AI.mp3'])
     os.remove('AI.mp3')

def time():
     date = datetime.now().time()
     datey = 'The time now is '+ str(date)
     Print('LA: THE TIME NOW IS: '+str(date))
     speak(datey)
     
def date():
    time = datetime.now().date()
    speaktime = 'Today is' + str(time)
    Print('LA: TODAY IS: '+str(time))
    speak(speaktime)
    
def meaning():
     dict = PyDictionary()
     word = input('WORD: ')
     phrase =((dict.meaning(word)))
     speakphrase = word+'REFERS TO'+str(phrase['Noun'])
     print('\n\n')
     print('LA: POSSIBLE MEANINGS\n\n')
     for x in phrase['Noun']:
          Print(x)

     speak(str(phrase))
    
def scraper():
     q = input('SEARCH\t')
     Print('LA:TOP HITS')
     speak('These are the top hits for the search')
     for j in search(query=q, tld='co.in', num=10, stop=10, pause=2):
          Print('\t'+j)
     print('\n\n')
     
def jokes():
     n = random.randint(1,5)
     if(n==1):
          speak('What do you get when you cross a snowman with a vampire?       Frostbite!')
     elif(n==2):
          speak('What do dentists call an astronaut\'s cavity?            A black hole!')
     elif(n==3):
         speak('I invented a new word!                Plagiarism!')
     elif(n==4):
          speak('Why do we tell actors to "break a leg?              Because every play has a cast.')
     elif(n==5):
         speak('Hear about the new restaurant called Karma?                 There’s no menu: You get what you deserve.')

def main():
    print('\n\n\t\t\tLA: LOCAL ASSISTANT\n\t\t\tVersion 1.0\n\t\t\t[PRIVATE CONSOLE]')
    speak('Hello! I am your local assistant. VERSION 1.0')
    speak(' Welcome back boss! Happy to see you once again. How may I help you?')
    print('\n')
    
    
def second_main():
    Print('1.SAY THE DATE')
    Print('2.SAY THE TIME')
    Print('3.CRACK A JOKE')
    Print('4.I NEED A MEANING OF A WORD')
    Print('5.LET"S SEARCH!')
    Print('6.LET"S CALCULATE')
    n = int(input())
    if(n==1):
         date()
    elif(n==2):
         time()
    elif(n==3):
         jokes()
    elif(n==4):
         meaning()
    elif(n==5):
         scraper()
    elif(n==6):
         print('6')
    else:
         Print('ERROR!')
         speak('Sorry! I am not sure how to help you boss! See you soon')
    
    

    
     
#--------------------------------------------------MAIN MENU ------------------------
main()
Print('PASSWORD:_-_')
ans = True
pwd = (input())
if(pwd=='****'):
     
     while(ans == True):
         second_main()
         
         speak('Should I help you more? Yes or No')
         n = input()
         if(n=='n' or n=='N'):
              ans = False
              speak('See you soon boss! Bye')
              Print('LA: BYE')
         

     
     




