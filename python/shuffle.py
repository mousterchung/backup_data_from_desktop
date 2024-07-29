from time import *
from random import *
cards=[]
people=None
while True:
    people=eval(input("please enter people(2~4):"))
    if people>=2 and people<=4:
        break
if people==2:
    list1=list2=[]







if people==2:
    list1=list2=[]
elif people==3:
    list1=list2=list3=[]
elif people==4:
    list1=list2=list3=list4=[]
suits=["♠","♥","♦","♣"]
numbers=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
for i in suits:
    for j in numbers:
        cards.append([i,j])
shuffle(cards)
if people==2:
    for i in range(26):
        list1.append(cards[i+0])
        list2.append(cards[i+1])
    print("list1=",list1,"\n")
    print("list2=",list2,"\n")
elif people==3:
    for i in range(17):
        list1.append(cards[i+0])
        list2.append(cards[i+1])
        list3.append(cards[i+2])
    print("list1=",list1,"\n")
    print("list2=",list2,"\n")
    print("list3=",list3,"\n")
    print("last:",cards[-1],"\n")
elif people==4:
    for i in range(13):
        list1.append(cards[i+0])
        list2.append(cards[i+1])
        list3.append(cards[i+2])
        list4.append(cards[i+3])
    print("list1=",list1,"\n")
    print("list2=",list2,"\n")
    print("list3=",list3,"\n")
    print("list4=",list4,"\n")
sleep(20)
