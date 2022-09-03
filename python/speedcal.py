from numbers import Rational
from time import *
import random as r
from turtle import home    #to work upon multiple string 


def mistake(t1,t2):
   error=0
   for i in range(0,len(t1)):
       try:
         if(t1[i]!=t2[i]):
            error=error+ 1

       except:
           error=error+1
         
   return error


def delay(tim1,tim2,user):
    time_delap=tim2-tim1
    time_roundoff=round(time_delap,2)
    speed=len(user)/time_roundoff
    return speed



test =["my name is rati","welcome to home","coming home "]

test1=r.choice(test)

print("*************typing speed calculator***********")
print(test1)
print()
print()
time1=time()
testinput=input("enter: ")
time2=time()

print("nuber of error in the  file   ")
print(mistake(test1,testinput))


print("the time taken to type")
print(delay(time1,time2,testinput))

 
