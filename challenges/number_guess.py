#!/usr/bin/env python3
import random




name=input("Hello whats your name: ")
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
        print("aah! you finally mate it Mr.%s in %d attempts" %(name,count))

