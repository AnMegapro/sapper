
from tkinter import *
from random import randint as rnd
import time

window = Tk()
window.geometry("500x550")

#Made by Podrick Payne
#You can find other finished works on the website: http://349624-megapro253.tmweb.ru/

def boom(event):
    
    
    if event.widget.bomb:
        btns[event.widget.num]["text"]="●"
        print("You lose!")
        endL.place(x=0,y=250)
    else:
        countB=0
        
        
        if event.widget.num%10==0:
            print("1") 
            around=[event.widget.num-10,event.widget.num+10,event.widget.num+1,event.widget.num+11,event.widget.num-9]
        elif event.widget.num%10==9:
            print("2")
            around=[event.widget.num-10,event.widget.num-1,event.widget.num+10,event.widget.num-11,event.widget.num+9]
        else:
            print("3")
            around=[event.widget.num-11,event.widget.num-10,event.widget.num-9,event.widget.num-1,event.widget.num+11,event.widget.num+10,event.widget.num+9,event.widget.num+1]

        for all in around:
            if all>-1 and all<100 and btns[all].bomb:
                countB+=1;
        
        
        
        btns[event.widget.num]["text"]=countB
        #if countB==0:
        #    zero(around)
        
        checking()
        
        
def checking():
    endG=True
    for all in btns:
        if all["text"]=="":
            endG=False
            print(all["text"], "This")
    if endG==True:
        endl["text"]="You Won!"
        endL.place(x=0,y=250)
 
#def zero(aroundOlD):
#    countB=0
#    for y in aroundOlD:
#        if y>-1 and y<100:
#            if y%10==0:
#                print("1") 
#                around=[y-10,y+10,y+1,y+11,y-9]
#            elif y%10==9:
#                print("2")
#                around=[y-10,y-1,y+10,y-11,y+9]
#            else:
#                print("3")
#                around=[y-11,y-10,y-9,y-1,y+11,y+10,y+9,y+1]

#            for all in around:
#                if all>-1 and all<100 and btns[all].bomb:
#                    countB+=1;
#            btns[y]["text"]=countB
            
#            checking()


window.bind("<Button-1>", boom)

btns=[]

for y in range(10):
    a=rnd(0,10)
    for x in range(10):
        btn= Button(window, text="");
        print(x,y)
        btn.y=y
        btn.x=x
        btn.num=y*10+x
        if a==x:
            btn.bomb=True
            btn.config(font=("Courier", 40))
            btn["text"]=" "

        else:
            btn.bomb=False
            btn.config(font=("Courier", 20))
            btn["text"]=""
        btns.append(btn)

for btn in btns:
    btn.place(x=btn.x*50, y=btn.y*50+50, width=50,height=50)

name=Label(window, text="Sapper game")
endL=Label(window, text="Game Over!")
name.config(font=("Courier", 20))
endL.config(font=("Courier", 62))

name.pack()
window.mainloop()

