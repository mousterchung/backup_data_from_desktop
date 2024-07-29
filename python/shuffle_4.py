from time import *
from random import *
cards=list1=list2=list3=list4=[]
suits=["♠","♥","♦","♣"]
numbers=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
for i in suits:
    for j in numbers:
        cards.append([i,j])
shuffle(cards)
list1=cards[0]+cards[4]+cards[8]+cards[12]+cards[16]+cards[20]+cards[24]+cards[28]+cards[32]+cards[36]+cards[40]+cards[44]+cards[48]
list2=cards[1]+cards[5]+cards[9]+cards[13]+cards[17]+cards[21]+cards[25]+cards[29]+cards[33]+cards[37]+cards[41]+cards[45]+cards[49]
list3=cards[2]+cards[6]+cards[10]+cards[14]+cards[18]+cards[22]+cards[26]+cards[30]+cards[34]+cards[38]+cards[42]+cards[46]+cards[50]
list4=cards[3]+cards[7]+cards[11]+cards[15]+cards[19]+cards[23]+cards[27]+cards[31]+cards[35]+cards[39]+cards[43]+cards[47]+cards[51]
print("list1=",list1,"\n")
print("list2=",list2,"\n")
print("list3=",list3,"\n")
print("list4=",list4,"\n")
sleep(20)
