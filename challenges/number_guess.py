#!/usr/bin/env python3

import random
import shutil

def stars():
        print ((col//2)*'*')

col,line=shutil.get_terminal_size()

def banner(str):
        print (str.center((col//2),'*'))

great="   Hello Welcome to Number Guess Game    "

#print (great.center((col//2),'*'))
#banner(great)

banner("   Hello Welcome to Number Guess Game    ")
stars()
#print ((col//2)*'*')

name=input("Hello whats your name: ")
gender=input(" And Gender Please : ")
stars()
print ("Lets start game")
sec_num=int(10 * random.random())+100
#print (sec_num)
num=0
count=0
while sec_num != num :
        num=int(input("Enter your guess number:"))
        count=count+1
        if sec_num > num:
                print("You have entered littile low , try little higher")
        elif sec_num < num:
                print("you have entered little higher, try little lower")

else:
    if gender=="Male":
        title="Mr"
    else:
        title="Miss"
    print("aah! you finally made it %s.%s in %d attempts" %(title,name,count))
