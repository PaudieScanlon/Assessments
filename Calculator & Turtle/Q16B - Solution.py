from turtle import *
#Name:

for j in range (10):
   for i in range(6): #This will iterate as many times as listed
       forward((j+1)*20) #Will move the turtle forward by the calculated amount
       left(60) #Will rotate left by specified degrees   
   right(135)
   penup()
   forward(10)
   pendown()
   left(135)

