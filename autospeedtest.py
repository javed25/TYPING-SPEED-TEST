from tkinter import *
from tkinter import messagebox as msg
import time
from text import *
import random
from threading import Timer

root=Tk()
root.title("TYPING SPEED TEST")
root.geometry("450x450")
root.config(bg="black")


def again():
    global win
    win.destroy()
    game()

def start(event):
    global start_time
    start_time=time.time()
    Timer(30,stop).start()

def stop():
    done("e")
    

def done(e):
    end_time=time.time()
    global text,errors,j,text1,start_time,hs1
    total_time=end_time-start_time
    total_time=total_time/60
    errors=0
    j=0
    result=text1.get(1.0,"end-1c")
    print("result len = ",len(result))
    print("text len = ",len(text))

    if len(result)>len(text):
        errors=len(result)-len(text)
        for i in result:
            if j<len(text):
                if i==text[j]:
                    pass
                else:
                    errors+=1
            j+=1

    elif len(text)>=len(result):
        # errors=len(text)-len(result)
        for i in text:
            # if j==len(result):
            #     break
            if j<len(result):
                if i==result[j]:
                    pass
                else:
                    errors+=1
            j+=1
    print("errors= ",errors)
    print("total time= ",total_time)
    gross_wpm=(len(result)/5)/total_time
    print("gross speed= ",gross_wpm)
    net_wpm=gross_wpm-(errors/total_time)
    print("net speed= ",net_wpm)
    accuracy=(net_wpm/gross_wpm)*100
    print("accuracy= ",accuracy)
    if net_wpm>hs2:
        with open("hs.txt","w") as f:
            f.write(str(net_wpm))
    
    msg.showinfo("SPEED",f"YOUR SPEED WAS {net_wpm} WPM")

x=0
def game():
    global x,win,text,text1
    if x==0:
        root.destroy()
        x+=1

    index=random.randint(0,len(words)-1)
    text=words[index]

    win=Tk()
    win.title("TEST")
    win.geometry("850x650")
    win.config(bg="black")

    l3=Label(win,text="START TYPING THE TEXT IN THE BOX",bg="black",font=("",24,"bold"),fg="YELLOW")
    l3.place(x=130,y=5)

    l2=Label(win,text=text,bg="black",font=("",15,"bold"),fg="white",wraplength=810,height=7)
    l2.place(x=20,y=50)

    text1=Text(win,wrap=WORD,font=("arial",13),padx=15,pady=14,height=10,bg="#161e45",fg="white",insertbackground="white")
    text1.place(x=50,y=250)

    text1.bind('<Button-1>',start)
    text1.bind('<Escape>',done)

    b3=Button(win,text="DONE",width=10,font=("",16,"bold"),bg="#fcba03",fg="black",command=done)
    b3.place(x=50,y=500)

    b4=Button(win,text="TRY AGAIN",width=10,font=("",16,"bold"),bg="#fcba03",fg="black",command=again)
    b4.place(x=350,y=500)

    b5=Button(win,text="EXIT TYPING",font=("",16,"bold"),bg="#fcba03",fg="black",width=10,command=win.destroy)
    b5.place(x=660,y=500)
    win.mainloop()
    

with open("hs.txt","r") as f:
    hs1=f.read()

hs2=float(hs1)



l1=Label(root,text="TYPING SPEED TEST",fg="#03fcf8",bg="black",font=("",24,"bold"))
l1.place(x=70,y=10)

b1=Button(root,text="BEGIN TEST",width=10,font=("",16,"bold"),bg="#fcba03",fg="black",command=game)
b1.place(x=10,y=200)

b2=Button(root,text="EXIT",font=("",16,"bold"),bg="#fcba03",fg="black",width=10,command=root.destroy)
b2.place(x=300,y=200)


Label(root,text=f"HIGH SCORE",bg="red",wraplength=900,fg="white",font=("",24,"bold")).place(x=120,y=320)
Label(root,text=str(hs1)+" WPM",bg="black",wraplength=900,fg="white",font=("",24,"bold")).place(x=150,y=370)



root.mainloop()
