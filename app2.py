import tkinter as tk
from tkinter import filedialog, Text
from PIL import ImageTk, Image
import os,time,re

root=tk.Tk()
root.title("REPINs Through Time")
blue="#0F97EF"
white="#FFFFFF"
tree_frame=None
main_lbx=None
s_frame=None
lakme_frame=None
repin=[]
treedot1=[
    "TAM",
    "DSM",
    "189", "174"
]
treedot2=[0,0,0,0]
cx=[0.135,0.375,0.595,0.875]
cy=0.56

def brain():
    global repin
    f=(open("build/repDSMTAM.txt",'r')).readlines()
    for i in f:
        s=i.split(' ')
        s[0]=int(s[0])
        s[3]=int(s[3])
        s[4]=int(s[4])
        
        if(s[2]=='red'):
            s[2]=0
        elif(s[2]=='blue'):
            s[2]=1
        elif(s[2]=='green'):
            s[2]=2
        elif(s[2]=='pink'):
            s[2]=3
                
        if(s[5][len(s[5])-1]=='\n'):
            s[5]=s[5][:-1]
        repin.append(s)

def repinapi(n1,n2,key):
    if(key==1):
        temp=[]
        for i in range(len(repin)):
            if(repin[i][0]==n1):
                temp.append(repin[i])
    if(key==2):
        entry=n1
        temp="green 12345678..12345678\ngreen 12345678..12345678"
    return temp

def repdot(col,pos,dsl):
    ddcol=[]
    
    dotr_pil=(Image.open("build/ddred.png")).resize((25,25))
    dotr=ImageTk.PhotoImage(dotr_pil)
    ddcol.append( tk.Label(lakme_frame,image=dotr) )
    ddcol[0].image=dotr
    
    dotb_pil=(Image.open("build/ddblue.png")).resize((25,25))
    dotb=ImageTk.PhotoImage(dotb_pil)
    ddcol.append(tk.Label(lakme_frame,image=dotb))
    ddcol[1].image=dotb
    
    dotg_pil=(Image.open("build/ddgreen.png")).resize((25,25))
    dotg=ImageTk.PhotoImage(dotg_pil)
    ddcol.append(tk.Label(lakme_frame,image=dotg))
    ddcol[2].image=dotg
    
    dotg_pil=(Image.open("build/ddpink.png")).resize((25,25))
    dotg=ImageTk.PhotoImage(dotg_pil)
    ddcol.append(tk.Label(lakme_frame,image=dotg))
    ddcol[3].image=dotg

    fx=0.06
    fy=0.1
    
    scol=[]
    
    dotr_pil=(Image.open("build/sred.png")).resize((25,25))
    dotr=ImageTk.PhotoImage(dotr_pil)
    scol.append( tk.Label(lakme_frame,image=dotr) )
    scol[0].image=dotr
    
    dotb_pil=(Image.open("build/sblue.png")).resize((25,25))
    dotb=ImageTk.PhotoImage(dotb_pil)
    scol.append(tk.Label(lakme_frame,image=dotb))
    scol[1].image=dotb
    
    dotg_pil=(Image.open("build/sgreen.png")).resize((25,25))
    dotg=ImageTk.PhotoImage(dotg_pil)
    scol.append(tk.Label(lakme_frame,image=dotg))
    scol[2].image=dotg
    
    dotg_pil=(Image.open("build/spink.png")).resize((25,25))
    dotg=ImageTk.PhotoImage(dotg_pil)
    scol.append(tk.Label(lakme_frame,image=dotg))
    scol[2].image=dotg

    if(dsl==1):
        ddcol[col].place(relx=cx[pos]-fx,rely=cy+fy)
    elif(dsl==0):
        scol[col].place(relx=cx[pos]-fx,rely=cy+fy)
    else:
        print(dsl)
    

def addrepin(rep_label):
    ty=0.11
    tx=-0.015
    for i in range(len(rep_label)):
        for j in range(len(treedot1)):
            if(rep_label[i][1].count(treedot1[j])!=0):
                repdot(rep_label[i][2],j,1)
                txt= str(rep_label[i][3])+".."+str(rep_label[i][4])
                tk.Label(lakme_frame,text=txt).place(relx=cx[j]+tx,rely=cy+ty)

def addreddot(entry,key):
    #Called addreddot but actually adds a blackdot xD
    dotr_pil=(Image.open("build/blackdot.png")).resize((25,25))
    dotr=ImageTk.PhotoImage(dotr_pil)
    #0.490-0.447=0.043
    dcy=0.005
    mx=[0.73,0.525]
    my=[0.515,0.455]
        
    for i in range(len(entry)):
        rd = tk.Label(lakme_frame,image=dotr)
        rd.image=dotr
        if(key[0]==0):
            if(entry[i]==2 or entry[i]==3):
                rd.place(relx=cx[entry[i]],rely=cy-dcy)
        if(key[1]==0):
            if(entry[i]==1 or entry[i]==0):
                rd.place(relx=cx[entry[i]],rely=cy-dcy)
        
        if(entry[i]==110):
            rd.place(relx=mx[0],rely=my[0])
        elif(entry[i]==120):
            rd.place(relx=mx[1],rely=my[1])

def tree_init():
    global lakme_frame
    lakme_frame= tk.Frame(root,bg="black",highlightbackground=blue,highlightcolor=blue, highlightthickness=2)
    lakme_frame.place(relx=0.313,rely=0.05,relheight=0.9,relwidth=0.65)
    
    gentree=ImageTk.PhotoImage(Image.open("build/gentree1.jpg"))
    g_label= tk.Label(lakme_frame,image=gentree)
    g_label.image=gentree
    g_label.place(relwidth=1,relheight=1)
    
    tk.Label(lakme_frame,text="Pseudomonas chlororaphis REPINs Clade",font=("Courier", 20)).place(relx=0.12,rely=0.04)
    
    tk.Label(s_frame,font=("Helvetica", 16,'bold'),text="Active Selection: ",bg=blue).place(relx=0,rely=0.65,relwidth=0.5)

def generate(entry):
    tree_init()
    rep_label=repinapi(int(entry),0,1)
    
    #rep_label=[[0,"chlT5",1234567,1234567,0],[0,"chlfdfS23",1234567,1234567,1],[0,"chl66",1234567,1234567,2]]
    
    global treedot2
    treedot2=[0,0,0,0]
    for i in range(len(rep_label)):
        for j in range(len(treedot1)):
            if(rep_label[i][1].count(treedot1[j])):
                treedot2[j]+=1
    
    
    entry=[]
    #110,120,130,200,150
    key=[0,0]
    if(treedot2[2]==0 and treedot2[3]==0 and treedot2[1]==0):
        entry.append(120)
        key[1]+=1
        key[0]+=1
    elif(treedot2[2]==0 and treedot2[3]==0):
        entry.append(110)
        key[0]+=1
    
    for i in range(len(treedot2)):
        if(treedot2[i]==0):
            entry.append(i)
    
    #print(rep_label)
    #print(entry, key)
    addreddot(entry,key)
    addrepin(rep_label)

def fetch(evt):
    global main_lbx,s_frame
    w = evt.widget
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    m=re.search('(\d+)',value).group()
    tk.Label(s_frame,font=("Helvetica", 16,'bold'),text="Active Selection: ",bg=blue).place(relx=0,rely=0.65,relwidth=0.5)
    tk.Label(s_frame,text=m).place(relx=0.45,rely=0.65,relwidth=0.15)
    generate(m)

def hotspotinit():
    h=[]
    global repin
    nom=repin[len(repin)-1][0]
    for i in range(nom):
        h.append("Hotspot #{}".format(i))
    global main_lbx

    main_lbx = tk.Listbox(s_frame)
    main_lbx.place(relx=0.1,rely=0.11,relwidth=0.5,relheight=0.5)
    
    sbr= tk.Scrollbar(main_lbx)
    sbr.pack(side="right",fill='y')
    sbr.config(command=main_lbx.yview)
    main_lbx.config(yscrollcommand=sbr.set)
    
    for i in range(len(h)):
        main_lbx.insert(i,h[i])
    
    main_lbx.bind('<<ListboxSelect>>', fetch)
    #generate(-1)

def locgen(x):
    tree_init()
    m= (re.findall('(\d+)..(\d+)',str(x)))
    rep_label=repinapi(int(m[0][0]),int(m[0][1]),2)
    m=str(entry)
    tk.Label(s_frame,text=m).place(relx=0.45,rely=0.65,relwidth=0.15)
    #addreddot(entry)
    #addrepin(entry,rep_label)

def locationinit():
    x_pil=(Image.open("build/construction.jpg")).resize((250,130))
    x=ImageTk.PhotoImage(x_pil)
    x1 = tk.Label(s_frame,image=x,bg=blue)
    x1.image=x
    x1.place(relx=0,rely=0.15,relheight=0.5,relwidth=1)
    
    """
    sbox1=tk.Entry(s_frame,font=40)
    sbox1.place(relx=0.1,rely=0.1,relwidth=0.5,relheight=0.05)
    
    go_button1 = tk.Button(s_frame,text="Set Range",font=40,command= lambda:locgen(sbox1.get()))
    go_button1.place(relx=0.12,rely=0.16)
    
    tk.Label(s_frame,text="Enter ONLY in the format 12345..12345.",bg=blue).place(relx=0.13,rely=0.25)
    """
    
def maininit():
    #tk.Label(s_frame,bg=blue).place(relx=0,rely=0,relwidth=1,relheight=1)
    tk.Label(s_frame,bg=white,text=f"Footnote:\nBlack Dot-> Lost in evolution\nDouble Dot-> REPINS\nSingle Dot-> REP",font=("Courier", 14,"bold")).place(relx=0.05,rely=0.75)
    
    lakme_frame= tk.Frame(root,bg="black",highlightbackground=blue,highlightcolor=blue, highlightthickness=2)
    lakme_frame.place(relx=0.313,rely=0.05,relheight=0.9,relwidth=0.65)
    
    gentree=ImageTk.PhotoImage(Image.open("build/gentree1.jpg"))
    g_label= tk.Label(lakme_frame,image=gentree)
    g_label.image=gentree
    g_label.place(relwidth=1,relheight=1)
    
    tk.Label(lakme_frame,text="Pseudomonas chlororaphis REPINs Clade",font=("Courier", 20)).place(relx=0.12,rely=0.04)

def clear_s_frame():
    tk.Label(s_frame,bg=blue).place(relx=0,rely=0.1,relwidth=1,relheight=0.65)

def selected(event):
    maininit()
    if(event.count("Hotspot")!=0):
        clear_s_frame()
        hotspotinit()
    if(event.count("Location")!=0):
        clear_s_frame()
        locationinit()
    return

def firstsetup():
    canvas = tk.Canvas(root,height=700,width=1200,bg="white")
    canvas.pack()
    
    #Adding Frame for Search Panel
    ##From Here
    global s_frame
    s_frame = tk.Frame(root, bg=blue)
    s_frame.place(relwidth=0.27,relheight=1,relx=0)
    
    options=["Choose Search Method","Search REPIN by Hotspot","Search REPIN by Location Range"]
    clicked= tk.StringVar()
    clicked.set(options[0])
    
    drop = tk.OptionMenu(s_frame,clicked, *options,command=selected)
    drop.place(relx=0.08,rely=0.04,relwidth=0.86,relheight=0.05)
    #Till Here

def main():
    brain()
    firstsetup()
    maininit()
    root.mainloop()

if __name__ == '__main__':
    main()