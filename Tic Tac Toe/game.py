from email.mime import image
from fileinput import filename
import tkinter
from tkinter import ttk
from tracemalloc import stop
from turtle import back, bgcolor, right
from typing import Container
import tk
import imghdr
from tkinter import *
import random
import tkinter as tk
from tkinter import ttk
import numpy as np 
import pygame
from PIL import Image,ImageTk
import os
import time
import cv2
import imutils
import pyautogui
from PIL import Image, ImageTk
from PIL import Image
import sys, pygame

GAME_HEIGHT=900
GAME_WIDTH=900
score1=0
score2=0
p=0
okk=0
ok=0
lst=[]
for i in range(10):
    lst.append(0)
lsty=[]
lstx=[]
lstyO=[]
lstxO=[]
lst[0]=1
print(lst)
def turnXsolo(event):
   print(lst)
   global x,y
   global ok
   x=event.x
   y=event.y
   ok+=1
   print("!")
   if x<300:
        x=300
   elif x<600:
        x=600
   else: x=900
   if y<300:
        y=300
   elif y<600:
        y=600
   else: y=900
   z=int(x/300+y/100-3)
   if(lst[z]!=0):
      turnXsolo(event)
   else:
      lstx.append(x)
      lsty.append(y)
      print (x,y)
      lst[z]=1
      if(lst[1]==lst[4]==lst[7]==1 or lst[2]==lst[5]==lst[8]==1 or lst[3]==lst[6]==lst[9]==1 or lst[1]==lst[2]==lst[3]==1 or lst[4]==lst[5]==lst[6]==1 or lst[7]==lst[8]==lst[9]==1 or lst[1]==lst[5]==lst[9]==1 or lst[7]==lst[5]==lst[3]==1 ):
        won()
      while lst[z]!=0 and ok!=5:
        x=random.randint(1,3)
        y=random.randint(1,3)
        x*=300
        
        y*=300
        
        z=int(x/300+y/100-3)
      z=int(x/300+y/100-3)
      lst[z]=2
      lstxO.append(x)
      lstyO.append(y)
      if(lst[1]==lst[4]==lst[7]==2 or lst[2]==lst[5]==lst[8]==2 or lst[3]==lst[6]==lst[9]==2 or lst[1]==lst[2]==lst[3]==2 or lst[4]==lst[5]==lst[6]==2 or lst[7]==lst[8]==lst[9]==2 or lst[1]==lst[5]==lst[9]==2 or lst[7]==lst[5]==lst[3]==2 ):
        lost()
      if(ok==1):
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        time()
      if(ok==2):
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        imga=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[1]-150,lsty[1]-150,image=imga)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        imga1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[1]-150,lstyO[1]-150,image=imga1)
        time()
      if(ok==3):
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        imga=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[1]-150,lsty[1]-150,image=imga)
        imgb=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[2]-150,lsty[2]-150,image=imgb)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        imga1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[1]-150,lstyO[1]-150,image=imga1)
        imgb1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[2]-150,lstyO[2]-150,image=imgb1)
        time()
      if(ok==4):
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        imga=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[1]-150,lsty[1]-150,image=imga)
        imgb=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[2]-150,lsty[2]-150,image=imgb)
        imgc=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[3]-150,lsty[3]-150,image=imgc)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        imga1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[1]-150,lstyO[1]-150,image=imga1)
        imgb1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[2]-150,lstyO[2]-150,image=imgb1)
        imgc1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[3]-150,lstyO[3]-150,image=imgc1)
        time()
      if(ok==5):
        print(lst)
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        imga=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[1]-150,lsty[1]-150,image=imga)
        imgb=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[2]-150,lsty[2]-150,image=imgb)
        imgc=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[3]-150,lsty[3]-150,image=imgc)
        imgd=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[4]-150,lsty[4]-150,image=imgd)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        imga1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[1]-150,lstyO[1]-150,image=imga1)
        imgb1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[2]-150,lstyO[2]-150,image=imgb1)
        imgc1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[3]-150,lstyO[3]-150,image=imgc1)
        time()

def turnXsoloh(event):
   print(lst)
   global x,y
   global ok
   global p
   x=event.x
   y=event.y
   ok+=1
   print("!")
   if x<300:
        x=300
   elif x<600:
        x=600
   else: x=900
   if y<300:
        y=300
   elif y<600:
        y=600
   else: y=900
   z=int(x/300+y/100-3)
   if(lst[z]!=0):
      turnXsolo(event)
   else:
      lstx.append(x)
      lsty.append(y)
      print (x,y)
      lst[z]=1
      if(lst[1]==lst[4]==lst[7]==1 or lst[2]==lst[5]==lst[8]==1 or lst[3]==lst[6]==lst[9]==1 or lst[1]==lst[2]==lst[3]==1 or lst[4]==lst[5]==lst[6]==1 or lst[7]==lst[8]==lst[9]==1 or lst[1]==lst[5]==lst[9]==1 or lst[7]==lst[5]==lst[3]==1 ):
        won()
      if(ok!=5):
       if(ok==1 and lst[5]==1):
         lstxO.append(300)
         lstyO.append(300)
         lst[1]=2
         p=1
       elif(ok==1 and (lst[8]==1 or lst[6]==1 or lst[4]==1 or lst[2]==1)):
         lstxO.append(600)
         lstyO.append(600)
         lst[5]=2
         p=1
       elif(ok==1 and (lst[1]==1 or lst[3]==1 or lst[9]==1 or lst[7]==1)):
         lstxO.append(600)
         lstyO.append(600)
         lst[5]=2
         p=1
       elif(ok==2 and lst[1]==lst[9]==1):
         lstxO.append(600)
         lstyO.append(300)
         lst[2]=2
         p=1
       elif(ok==2 and lst[3]==lst[7]==1):
         lstxO.append(600)
         lstyO.append(300)
         lst[2]=2
         p=1
       elif(ok==2 and lst[2]==lst[4]==1):
         lstxO.append(300)
         lstyO.append(300)
         lst[1]=2
         p=1
       elif(ok==2 and lst[2]==lst[6]==1):
         lstxO.append(900)
         lstyO.append(300)
         lst[3]=2
         p=1
       elif(ok==2 and lst[6]==lst[8]==1):
         lstxO.append(900)
         lstyO.append(900)
         lst[9]=2
         p=1
       elif(ok==2 and lst[8]==lst[4]==1):
         lstxO.append(300)
         lstyO.append(900)
         lst[7]=2
         p=1
       elif(lst[1]==lst[2]==2 and lst[3]==0):
         lstxO.append(900)
         lstyO.append(300)
         lst[3]=2
         p=1
       elif(lst[1]==lst[7]==2 and lst[4]==0):
         lstxO.append(300)
         lstyO.append(600)
         lst[4]=2
         p=1
       elif(lst[1]==lst[4]==2 and lst[7]==0):
         lstxO.append(300)
         lstyO.append(900)
         lst[7]=2
         p=1
       elif(lst[4]==lst[7]==2 and lst[1]==0):
         lstxO.append(300)
         lstyO.append(300)
         lst[1]=2
         p=1
       elif(lst[5]==lst[2]==2 and lst[8]==0):
         lstxO.append(600)
         lstyO.append(900)
         lst[8]=2
         p=1
       elif(lst[8]==lst[2]==2 and lst[5]==0):
         lstxO.append(600)
         lstyO.append(600)
         lst[5]=2
         p=1
       elif(lst[5]==lst[8]==2 and lst[2]==0):
         lstxO.append(600)
         lstyO.append(300)
         lst[2]=2
         p=1
       elif(lst[3]==lst[6]==2 and lst[9]==0):
         lstxO.append(900)
         lstyO.append(900)
         lst[9]=2
         p=1
       elif(lst[3]==lst[9]==2 and lst[6]==0):
         lstxO.append(900)
         lstyO.append(600)
         lst[6]=2
         p=1
       elif(lst[6]==lst[9]==2 and lst[3]==0):
         lstxO.append(900)
         lstyO.append(300)
         lst[3]=2
         p=1
       elif(lst[3]==lst[2]==2 and lst[1]==0):
         lstxO.append(300)
         lstyO.append(300)
         lst[1]=2
         p=1
       elif(lst[1]==lst[3]==2 and lst[2]==0):
         lstxO.append(600)
         lstyO.append(300)
         lst[2]=2
         p=1
       elif(lst[4]==lst[5]==2 and lst[6]==0):
         lstxO.append(900)
         lstyO.append(600)
         lst[6]=2
         p=1
       elif(lst[5]==lst[6]==2 and lst[4]==0):
         lstxO.append(300)
         lstyO.append(600)
         lst[4]=2
         p=1
       elif(lst[4]==lst[6]==2 and lst[5]==0):
         lstxO.append(600)
         lstyO.append(600)
         lst[5]=2
         p=1
       elif(lst[7]==lst[8]==2 and lst[9]==0):
         lstxO.append(900)
         lstyO.append(900)
         lst[9]=2
         p=1
       elif(lst[7]==lst[9]==2 and lst[8]==0):
         lstxO.append(600)
         lstyO.append(900)
         lst[8]=2
         p=1
       elif(lst[8]==lst[9]==2 and lst[7]==0):
         lstxO.append(300)
         lstyO.append(900)
         lst[7]=2
         p=1
       elif(lst[1]==lst[9]==2 and lst[5]==0):
         lstxO.append(600)
         lstyO.append(600)
         lst[5]=2
         p=1
       elif(lst[1]==lst[5]==2 and lst[9]==0):
         lstxO.append(900)
         lstyO.append(900)
         lst[9]=2
         p=1
       elif(lst[5]==lst[9]==2 and lst[1]==0):
         lstxO.append(300)
         lstyO.append(300)
         lst[1]=2
         p=1
       elif(lst[3]==lst[5]==2 and lst[7]==0):
         lstxO.append(900)
         lstyO.append(300)
         lst[7]=2
         p=1
       elif(lst[3]==lst[7]==2 and lst[5]==0):
         lstxO.append(600)
         lstyO.append(600)
         lst[5]=2
         p=1
       elif(lst[5]==lst[7]==2 and lst[3]==0):
         lstxO.append(300)
         lstyO.append(900)
         lst[3]=2
         p=1
       elif(lst[1]==lst[2]==1 and lst[3]==0):
         lstxO.append(900)
         lstyO.append(300)
         lst[3]=2
         p=1
       elif(lst[1]==lst[7]==1 and lst[4]==0):
         lstxO.append(300)
         lstyO.append(600)
         lst[4]=2
         p=1
       elif(lst[1]==lst[4]==1 and lst[7]==0):
         lstxO.append(300)
         lstyO.append(900)
         lst[7]=2
         p=1
       elif(lst[4]==lst[7]==1 and lst[1]==0):
         lstxO.append(300)
         lstyO.append(300)
         lst[1]=2
         p=1
       elif(lst[5]==lst[2]==1 and lst[8]==0):
         lstxO.append(600)
         lstyO.append(900)
         lst[8]=2
         p=1
       elif(lst[8]==lst[2]==1 and lst[5]==0):
         lstxO.append(600)
         lstyO.append(600)
         lst[5]=2
         p=1
       elif(lst[5]==lst[8]==1 and lst[2]==0):
         lstxO.append(600)
         lstyO.append(300)
         lst[2]=2
         p=1
       elif(lst[3]==lst[6]==1 and lst[9]==0):
         lstxO.append(900)
         lstyO.append(900)
         lst[9]=2
         p=1
       elif(lst[3]==lst[9]==1 and lst[6]==0):
         lstxO.append(900)
         lstyO.append(600)
         lst[6]=2
         p=1
       elif(lst[6]==lst[9]==1 and lst[3]==0):
         lstxO.append(900)
         lstyO.append(300)
         lst[3]=2
         p=1
       elif(lst[3]==lst[2]==1 and lst[1]==0):
         lstxO.append(300)
         lstyO.append(300)
         lst[1]=2
         p=1
       elif(lst[1]==lst[3]==1 and lst[2]==0):
         lstxO.append(600)
         lstyO.append(300)
         lst[2]=2
         p=1
       elif(lst[4]==lst[5]==1 and lst[6]==0):
         lstxO.append(900)
         lstyO.append(600)
         lst[6]=2
         p=1
       elif(lst[5]==lst[6]==1 and lst[4]==0):
         lstxO.append(300)
         lstyO.append(600)
         lst[4]=2
         p=1
       elif(lst[4]==lst[6]==1 and lst[5]==0):
         lstxO.append(600)
         lstyO.append(600)
         lst[5]=2
         p=1
       elif(lst[7]==lst[8]==1 and lst[9]==0):
         lstxO.append(900)
         lstyO.append(900)
         lst[9]=2
         p=1
       elif(lst[7]==lst[9]==1 and lst[8]==0):
         lstxO.append(600)
         lstyO.append(900)
         lst[8]=2
         p=1
       elif(lst[8]==lst[9]==1 and lst[7]==0):
         lstxO.append(300)
         lstyO.append(900)
         lst[7]=2
         p=1
       elif(lst[1]==lst[9]==1 and lst[5]==0):
         lstxO.append(600)
         lstyO.append(600)
         lst[5]=2
         p=1
       elif(lst[1]==lst[5]==1 and lst[9]==0):
         lstxO.append(900)
         lstyO.append(900)
         lst[9]=2
         p=1
       elif(lst[5]==lst[9]==1 and lst[1]==0):
         lstxO.append(300)
         lstyO.append(300)
         lst[1]=2
         p=1
       elif(lst[3]==lst[5]==1 and lst[7]==0):
         lstxO.append(300)
         lstyO.append(900)
         lst[7]=2
         p=1
       elif(lst[3]==lst[7]==1 and lst[5]==0):
         lstxO.append(600)
         lstyO.append(600)
         lst[5]=2
         p=1
       elif(lst[5]==lst[7]==1 and lst[3]==0):
         lstxO.append(900)
         lstyO.append(300)
         lst[3]=2
         p=1
      
       if p==0:
        while lst[z]!=0 and ok!=5:
         x=random.randint(1,3)
         y=random.randint(1,3)
         x*=300
        
         y*=300
        
         z=int(x/300+y/100-3)
        z=int(x/300+y/100-3)
        lst[z]=2
        lstxO.append(x)
        lstyO.append(y)
      p=0
      if(lst[1]==lst[4]==lst[7]==2 or lst[2]==lst[5]==lst[8]==2 or lst[3]==lst[6]==lst[9]==2 or lst[1]==lst[2]==lst[3]==2 or lst[4]==lst[5]==lst[6]==2 or lst[7]==lst[8]==lst[9]==2 or lst[1]==lst[5]==lst[9]==2 or lst[7]==lst[5]==lst[3]==2 ):
        print("!!!!!!!!!")
        print(lst)
        lost()
      if(ok==1):
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        time()
      if(ok==2):
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        imga=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[1]-150,lsty[1]-150,image=imga)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        imga1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[1]-150,lstyO[1]-150,image=imga1)
        time()
      if(ok==3):
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        imga=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[1]-150,lsty[1]-150,image=imga)
        imgb=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[2]-150,lsty[2]-150,image=imgb)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        imga1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[1]-150,lstyO[1]-150,image=imga1)
        imgb1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[2]-150,lstyO[2]-150,image=imgb1)
        time()
      if(ok==4):
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        imga=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[1]-150,lsty[1]-150,image=imga)
        imgb=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[2]-150,lsty[2]-150,image=imgb)
        imgc=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[3]-150,lsty[3]-150,image=imgc)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        imga1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[1]-150,lstyO[1]-150,image=imga1)
        imgb1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[2]-150,lstyO[2]-150,image=imgb1)
        imgc1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[3]-150,lstyO[3]-150,image=imgc1)
        time()
      if(ok==5):
        print(lst)
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        imga=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[1]-150,lsty[1]-150,image=imga)
        imgb=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[2]-150,lsty[2]-150,image=imgb)
        imgc=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[3]-150,lsty[3]-150,image=imgc)
        imgd=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[4]-150,lsty[4]-150,image=imgd)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        imga1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[1]-150,lstyO[1]-150,image=imga1)
        imgb1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[2]-150,lstyO[2]-150,image=imgb1)
        imgc1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[3]-150,lstyO[3]-150,image=imgc1)
        time()

def turnXsolom(event):
   print(lst)
   global x,y
   global ok
   global p
   x=event.x
   y=event.y
   ok+=1
   print("!")
   if x<300:
        x=300
   elif x<600:
        x=600
   else: x=900
   if y<300:
        y=300
   elif y<600:
        y=600
   else: y=900
   z=int(x/300+y/100-3)
   if(lst[z]!=0):
      turnXsolo(event)
   else:
      lstx.append(x)
      lsty.append(y)
      print (x,y)
      lst[z]=1
      if(lst[1]==lst[4]==lst[7]==1 or lst[2]==lst[5]==lst[8]==1 or lst[3]==lst[6]==lst[9]==1 or lst[1]==lst[2]==lst[3]==1 or lst[4]==lst[5]==lst[6]==1 or lst[7]==lst[8]==lst[9]==1 or lst[1]==lst[5]==lst[9]==1 or lst[7]==lst[5]==lst[3]==1 ):
        won()
      if(ok!=5):
       if(lst[1]==lst[2]==2 and lst[3]==0):
         lstxO.append(900)
         lstyO.append(300)
         lst[3]=2
         p=1
       elif(lst[1]==lst[7]==2 and lst[4]==0):
         lstxO.append(300)
         lstyO.append(600)
         lst[4]=2
         p=1
       elif(lst[1]==lst[4]==2 and lst[7]==0):
         lstxO.append(300)
         lstyO.append(900)
         lst[7]=2
         p=1
       elif(lst[4]==lst[7]==2 and lst[1]==0):
         lstxO.append(300)
         lstyO.append(300)
         lst[1]=2
         p=1
       elif(lst[5]==lst[2]==2 and lst[8]==0):
         lstxO.append(600)
         lstyO.append(900)
         lst[8]=2
         p=1
       elif(lst[8]==lst[2]==2 and lst[5]==0):
         lstxO.append(600)
         lstyO.append(600)
         lst[5]=2
         p=1
       elif(lst[5]==lst[8]==2 and lst[2]==0):
         lstxO.append(600)
         lstyO.append(300)
         lst[2]=2
         p=1
       elif(lst[3]==lst[6]==2 and lst[9]==0):
         lstxO.append(900)
         lstyO.append(900)
         lst[9]=2
         p=1
       elif(lst[3]==lst[9]==2 and lst[6]==0):
         lstxO.append(900)
         lstyO.append(600)
         lst[6]=2
         p=1
       elif(lst[6]==lst[9]==2 and lst[3]==0):
         lstxO.append(900)
         lstyO.append(300)
         lst[3]=2
         p=1
       elif(lst[3]==lst[2]==2 and lst[1]==0):
         lstxO.append(300)
         lstyO.append(300)
         lst[1]=2
         p=1
       elif(lst[1]==lst[3]==2 and lst[2]==0):
         lstxO.append(600)
         lstyO.append(300)
         lst[2]=2
         p=1
       elif(lst[4]==lst[5]==2 and lst[6]==0):
         lstxO.append(900)
         lstyO.append(600)
         lst[6]=2
         p=1
       elif(lst[5]==lst[6]==2 and lst[4]==0):
         lstxO.append(300)
         lstyO.append(600)
         lst[4]=2
         p=1
       elif(lst[4]==lst[6]==2 and lst[5]==0):
         lstxO.append(600)
         lstyO.append(600)
         lst[5]=2
         p=1
       elif(lst[7]==lst[8]==2 and lst[9]==0):
         lstxO.append(900)
         lstyO.append(900)
         lst[9]=2
         p=1
       elif(lst[7]==lst[9]==2 and lst[8]==0):
         lstxO.append(600)
         lstyO.append(900)
         lst[8]=2
         p=1
       elif(lst[8]==lst[9]==2 and lst[7]==0):
         lstxO.append(300)
         lstyO.append(900)
         lst[7]=2
         p=1
       elif(lst[1]==lst[9]==2 and lst[5]==0):
         lstxO.append(600)
         lstyO.append(600)
         lst[5]=2
         p=1
       elif(lst[1]==lst[5]==2 and lst[9]==0):
         lstxO.append(900)
         lstyO.append(900)
         lst[9]=2
         p=1
       elif(lst[5]==lst[9]==2 and lst[3]==0):
         lstxO.append(300)
         lstyO.append(300)
         lst[3]=2
         p=1
       elif(lst[3]==lst[5]==2 and lst[7]==0):
         lstxO.append(900)
         lstyO.append(300)
         lst[7]=2
         p=1
       elif(lst[3]==lst[7]==2 and lst[5]==0):
         lstxO.append(600)
         lstyO.append(600)
         lst[5]=2
         p=1
       elif(lst[5]==lst[7]==2 and lst[3]==0):
         lstxO.append(300)
         lstyO.append(900)
         lst[3]=2
         p=1
       elif(lst[1]==lst[2]==1 and lst[3]==0):
         lstxO.append(900)
         lstyO.append(300)
         lst[3]=2
         p=1
       elif(lst[1]==lst[7]==1 and lst[4]==0):
         lstxO.append(300)
         lstyO.append(600)
         lst[4]=2
         p=1
       elif(lst[1]==lst[4]==1 and lst[7]==0):
         lstxO.append(300)
         lstyO.append(900)
         lst[7]=2
         p=1
       elif(lst[4]==lst[7]==1 and lst[1]==0):
         lstxO.append(300)
         lstyO.append(300)
         lst[1]=2
         p=1
       elif(lst[5]==lst[2]==1 and lst[8]==0):
         lstxO.append(600)
         lstyO.append(900)
         lst[8]=2
         p=1
       elif(lst[8]==lst[2]==1 and lst[5]==0):
         lstxO.append(600)
         lstyO.append(600)
         lst[5]=2
         p=1
       elif(lst[5]==lst[8]==1 and lst[2]==0):
         lstxO.append(600)
         lstyO.append(300)
         lst[2]=2
         p=1
       elif(lst[3]==lst[6]==1 and lst[9]==0):
         lstxO.append(900)
         lstyO.append(900)
         lst[9]=2
         p=1
       elif(lst[3]==lst[9]==1 and lst[6]==0):
         lstxO.append(900)
         lstyO.append(600)
         lst[6]=2
         p=1
       elif(lst[6]==lst[9]==1 and lst[3]==0):
         lstxO.append(900)
         lstyO.append(300)
         lst[3]=2
         p=1
       elif(lst[3]==lst[2]==1 and lst[1]==0):
         lstxO.append(300)
         lstyO.append(300)
         lst[1]=2
         p=1
       elif(lst[1]==lst[3]==1 and lst[2]==0):
         lstxO.append(600)
         lstyO.append(300)
         lst[2]=2
         p=1
       elif(lst[4]==lst[5]==1 and lst[6]==0):
         lstxO.append(900)
         lstyO.append(600)
         lst[6]=2
         p=1
       elif(lst[5]==lst[6]==1 and lst[4]==0):
         lstxO.append(300)
         lstyO.append(600)
         lst[4]=2
         p=1
       elif(lst[4]==lst[6]==1 and lst[5]==0):
         lstxO.append(600)
         lstyO.append(600)
         lst[5]=2
         p=1
       elif(lst[7]==lst[8]==1 and lst[9]==0):
         lstxO.append(900)
         lstyO.append(900)
         lst[9]=2
         p=1
       elif(lst[7]==lst[9]==1 and lst[8]==0):
         lstxO.append(600)
         lstyO.append(900)
         lst[8]=2
         p=1
       elif(lst[8]==lst[9]==1 and lst[7]==0):
         lstxO.append(300)
         lstyO.append(900)
         lst[7]=2
         p=1
       elif(lst[1]==lst[9]==1 and lst[5]==0):
         lstxO.append(600)
         lstyO.append(600)
         lst[5]=2
         p=1
       elif(lst[1]==lst[5]==1 and lst[9]==0):
         lstxO.append(900)
         lstyO.append(900)
         lst[9]=2
         p=1
       elif(lst[5]==lst[9]==1 and lst[1]==0):
         lstxO.append(300)
         lstyO.append(300)
         lst[1]=2
         p=1
       elif(lst[3]==lst[5]==1 and lst[7]==0):
         lstxO.append(300)
         lstyO.append(900)
         lst[7]=2
         p=1
       elif(lst[3]==lst[7]==1 and lst[5]==0):
         lstxO.append(600)
         lstyO.append(600)
         lst[5]=2
         p=1
       elif(lst[5]==lst[7]==1 and lst[3]==0):
         lstxO.append(900)
         lstyO.append(300)
         lst[3]=2
         p=1
      
       if p==0:
        while lst[z]!=0 and ok!=5:
         x=random.randint(1,3)
         y=random.randint(1,3)
         x*=300
        
         y*=300
        
         z=int(x/300+y/100-3)
        z=int(x/300+y/100-3)
        lst[z]=2
        lstxO.append(x)
        lstyO.append(y)
      p=0
      if(lst[1]==lst[4]==lst[7]==2 or lst[2]==lst[5]==lst[8]==2 or lst[3]==lst[6]==lst[9]==2 or lst[1]==lst[2]==lst[3]==2 or lst[4]==lst[5]==lst[6]==2 or lst[7]==lst[8]==lst[9]==2 or lst[1]==lst[5]==lst[9]==2 or lst[7]==lst[5]==lst[3]==2 ):
        print("!!!!!!!!!")
        print(lst)
        lost()
      if(ok==1):
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        time()
      if(ok==2):
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        imga=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[1]-150,lsty[1]-150,image=imga)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        imga1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[1]-150,lstyO[1]-150,image=imga1)
        time()
      if(ok==3):
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        imga=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[1]-150,lsty[1]-150,image=imga)
        imgb=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[2]-150,lsty[2]-150,image=imgb)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        imga1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[1]-150,lstyO[1]-150,image=imga1)
        imgb1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[2]-150,lstyO[2]-150,image=imgb1)
        time()
      if(ok==4):
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        imga=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[1]-150,lsty[1]-150,image=imga)
        imgb=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[2]-150,lsty[2]-150,image=imgb)
        imgc=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[3]-150,lsty[3]-150,image=imgc)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        imga1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[1]-150,lstyO[1]-150,image=imga1)
        imgb1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[2]-150,lstyO[2]-150,image=imgb1)
        imgc1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[3]-150,lstyO[3]-150,image=imgc1)
        time()
      if(ok==5):
        print(lst)
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        imga=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[1]-150,lsty[1]-150,image=imga)
        imgb=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[2]-150,lsty[2]-150,image=imgb)
        imgc=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[3]-150,lsty[3]-150,image=imgc)
        imgd=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[4]-150,lsty[4]-150,image=imgd)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        imga1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[1]-150,lstyO[1]-150,image=imga1)
        imgb1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[2]-150,lstyO[2]-150,image=imgb1)
        imgc1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[3]-150,lstyO[3]-150,image=imgc1)
        time()

   
def turnX(event):
    global x,y
    global ok
    x=event.x
    y=event.y
    a=x 
    b=y
    print(ok)
    if ok%2==0:
     ok+=1
     print("!")
     if x<300:
        x=300
     elif x<600:
        x=600
     else: x=900
     if y<300:
        y=300
     elif y<600:
        y=600
     else: y=900
     z=int(x/300+y/100-3)
     if(lst[z]!=0):
        ok-=1
     if ok%2==1:
      lstx.append(x)
      lsty.append(y)
      print (x,y)
      lst[z]=1
      if(lst[1]==lst[4]==lst[7]==1 or lst[2]==lst[5]==lst[8]==1 or lst[3]==lst[6]==lst[9]==1 or lst[1]==lst[2]==lst[3]==1 or lst[4]==lst[5]==lst[6]==1 or lst[7]==lst[8]==lst[9]==1 or lst[1]==lst[5]==lst[9]==1 or lst[7]==lst[5]==lst[3]==1 ):
        won()
      if(ok==1):
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        time()
      if(ok==3):
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        imga=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[1]-150,lsty[1]-150,image=imga)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        imga1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[1]-150,lstyO[1]-150,image=imga1)
        time()
      if(ok==5):
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        imga=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[1]-150,lsty[1]-150,image=imga)
        imgb=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[2]-150,lsty[2]-150,image=imgb)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        imga1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[1]-150,lstyO[1]-150,image=imga1)
        imgb1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[2]-150,lstyO[2]-150,image=imgb1)
        time()
      if(ok==7):
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        imga=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[1]-150,lsty[1]-150,image=imga)
        imgb=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[2]-150,lsty[2]-150,image=imgb)
        imgc=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[3]-150,lsty[3]-150,image=imgc)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        imga1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[1]-150,lstyO[1]-150,image=imga1)
        imgb1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[2]-150,lstyO[2]-150,image=imgb1)
        imgc1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[3]-150,lstyO[3]-150,image=imgc1)
        time()
      if(ok==9):
        print(lst)
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        imga=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[1]-150,lsty[1]-150,image=imga)
        imgb=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[2]-150,lsty[2]-150,image=imgb)
        imgc=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[2]-150,lsty[2]-150,image=imgc)
        imgd=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[3]-150,lsty[3]-150,image=imgd)
        imge=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[4]-150,lsty[4]-150,image=imge)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        imga1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[1]-150,lstyO[1]-150,image=imga1)
        imgb1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[2]-150,lstyO[2]-150,image=imgb1)
        imgc1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[3]-150,lstyO[3]-150,image=imgc1)
        imgd1=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[3]-150,lsty[3]-150,image=imgd1)
        imge1=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[4]-150,lsty[4]-150,image=imge1)
        time()
     else: pass
    else:
     turnO(event)
    
def won():
    canvas.delete(ALL)
    canvas.config(background='black')
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas',70),text="PLAYER X WON",fill="white",tag="PLAYER X WON")
    canvas.pack()
    window.update()
    window_width=window.winfo_width()
    window_height=window.winfo_height()
    screen_width=window.winfo_screenwidth()
    screen_height=window.winfo_screenheight()

    x=int((screen_width/2)-(window_width/2))
    y=int((screen_height/2)-(window_height/2))
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")


    window.mainloop() 
    

def lost():
    canvas.delete(ALL)
    canvas.config(background='black')
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas',70),text="PLAYER O WON",fill="white",tag="PLAYER O WON")
    canvas.pack()
    window.update()
    window_width=window.winfo_width()
    window_height=window.winfo_height()
    screen_width=window.winfo_screenwidth()
    screen_height=window.winfo_screenheight()

    x=int((screen_width/2)-(window_width/2))
    y=int((screen_height/2)-(window_height/2))
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    

    window.mainloop()

def turnO(event):
    global x,y
    global ok
    x=event.x
    y=event.y
    a=x 
    b=y
    print(ok)
    print(ok)
    if ok%2==1:
     ok+=1
     print("!")
     if x<300:
        x=300
     elif x<600:
        x=600
     else: x=900
     if y<300:
        y=300
     elif y<600:
        y=600
     else: y=900
     z=int(x/300+y/100-3)
     if(lst[z]!=0):
        ok-=1
     if ok%2==0:
      lstxO.append(x)
      lstyO.append(y)
      print (x,y)
      lst[z]=2
      if(lst[1]==lst[4]==lst[7]==2 or lst[2]==lst[5]==lst[8]==2 or lst[3]==lst[6]==lst[9]==2 or lst[1]==lst[2]==lst[3]==2 or lst[4]==lst[5]==lst[6]==2 or lst[7]==lst[8]==lst[9]==2 or lst[1]==lst[5]==lst[9]==2 or lst[7]==lst[5]==lst[3]==2 ):
        lost()
      if(ok==2):
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        time()
      if(ok==4):
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        imga=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[1]-150,lsty[1]-150,image=imga)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        imga1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[1]-150,lstyO[1]-150,image=imga1)
        time()
      if(ok==6):
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        imga=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[1]-150,lsty[1]-150,image=imga)
        imgb=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[2]-150,lsty[2]-150,image=imgb)
        imgc=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[2]-150,lsty[2]-150,image=imgc)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        imga1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[1]-150,lstyO[1]-150,image=imga1)
        imgb1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[2]-150,lstyO[2]-150,image=imgb1)
        time()
      if(ok==8):
        img=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[0]-150,lsty[0]-150,image=img)
        imga=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[1]-150,lsty[1]-150,image=imga)
        imgb=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[2]-150,lsty[2]-150,image=imgb)
        imgc=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[2]-150,lsty[2]-150,image=imgc)
        imgd=PhotoImage(file="assets\X.png")
        my_image=canvas.create_image(lstx[3]-150,lsty[3]-150,image=imgd)
        img1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[0]-150,lstyO[0]-150,image=img1)
        imga1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[1]-150,lstyO[1]-150,image=imga1)
        imgb1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[2]-150,lstyO[2]-150,image=imgb1)
        imgc1=PhotoImage(file="assets\O.png")
        my_image=canvas.create_image(lstxO[3]-150,lstyO[3]-150,image=imgc1)
        time()
     else: pass
    else:
     turnX(event)

def single():
   P["state"] = DISABLED 
   H["state"] = DISABLED 
   X["state"] = DISABLED 
   T["state"] = DISABLED 
   window.bind('<Button-1>',  turnX)
   global okk
   okk=1

def two():
   P["state"] = DISABLED 
   H["state"] = DISABLED 
   X["state"] = DISABLED 
   T["state"] = DISABLED 
   window.bind('<Button-1>',  turnXsolo)
   global okk
   okk=2

def twom():
   P["state"] = DISABLED 
   H["state"] = DISABLED 
   X["state"] = DISABLED 
   T["state"] = DISABLED 
   window.bind('<Button-1>',  turnXsolom)
   global okk
   okk=3

def twoh():
   P["state"] = DISABLED 
   H["state"] = DISABLED 
   X["state"] = DISABLED 
   T["state"] = DISABLED 
   window.bind('<Button-1>',  turnXsoloh)
   global okk
   okk=3

window=Tk()

window.title("TicTacToe")
window.resizable(False,False)



canvas=Canvas(window, bg='green',height=GAME_HEIGHT,width=GAME_WIDTH)
label_frame = tk.Frame()
label_frame.pack(side = 'top', fill = 'x')
x=0
y=0
button_frame = tk.Frame()
button_frame.pack(side = 'top', fill = 'x')


P = tkinter.Button(button_frame, text ="2 Players",background='white', command = single)
P.pack(side = 'left', ipadx = 3, ipady = 1,padx=45)
H = tkinter.Button(button_frame, text ="Single Player Easy",background='white', command = two)
H.pack(side = 'left', ipadx = 3, ipady = 1,padx=45)
X = tkinter.Button(button_frame, text ="Single Player Medium",background='white', command = twom)
X.pack(side = 'left', ipadx = 3, ipady = 1,padx=45)
T = tkinter.Button(button_frame, text ="Single Player Hard",background='white', command = twoh)
T.pack(side = 'left', ipadx = 3, ipady = 1,padx=45)

imgi=PhotoImage(file="assets\Bara.png")
my_image=canvas.create_image(300,0,anchor=NW,image=imgi)
imgii=PhotoImage(file="assets\Bara.png")
my_image=canvas.create_image(600,0,anchor=NW,image=imgii)
imgior=PhotoImage(file="assets\Baraor.png")
my_image=canvas.create_image(0,300,anchor=NW,image=imgior)
imgiior=PhotoImage(file="assets\Baraor.png")
my_image=canvas.create_image(0,600,anchor=NW,image=imgiior)
print (okk)

canvas.pack()
window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

x=int((screen_width/2)-(window_width/2))
y=int((screen_height/2)-(window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")


window.mainloop()