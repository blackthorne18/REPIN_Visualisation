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
tbx,dbx,sbx,bbx=0.12,0.36,0.57,0.8
by=0.6
tsx,tsy=0.33,0.35
dsx,dsy=0.465,0.445
ssx,ssy=0.685,0.53


def repinapi(n1,n2,key):
    if(key==1):
        entry=n1
        rep_label="green 12345678..12345678"
        genes=["GeneA","GeneB"]
    if(key==2):
        entry=n1
        rep_label="green 12345678..12345678\ngreen 12345678..12345678"
        genes=["GeneA","GeneB"]
    return rep_label,entry,genes

def addrepin(entry,rep_label,genes):
    setx,sety=0.09,0.125
    stag=0
    mx=0.02
    
    gs1="Gene Before: {}".format(genes[0])
    gs2="Gene Before: {}".format(genes[1])
    
    if(entry==1):
        tk.Label(lakme_frame,text=rep_label).place(relx=tbx-setx,rely=by+sety)
    elif(entry==2):
        tk.Label(lakme_frame,text=rep_label).place(relx=tbx-setx,rely=by+sety)
        tk.Label(lakme_frame,text=rep_label).place(relx=dbx-setx,rely=by+sety)
    elif(entry==3):
        tk.Label(lakme_frame,text=rep_label).place(relx=tbx-setx,rely=by+sety)
        tk.Label(lakme_frame,text=rep_label).place(relx=dbx-setx,rely=by+sety)
        tk.Label(lakme_frame,text=rep_label).place(relx=bbx-setx+mx,rely=by+sety)
        #rep_label.place(relx=sbx-setx,rely=by+sety)
    elif(entry==4):
        tk.Label(lakme_frame,text=rep_label).place(relx=tbx-setx,rely=by+sety)
        tk.Label(lakme_frame,text=rep_label).place(relx=dbx-setx,rely=by+sety)
        tk.Label(lakme_frame,text=rep_label).place(relx=sbx-setx+mx,rely=by+sety)
    elif(entry==5):
        tk.Label(lakme_frame,text=rep_label).place(relx=tbx-setx,rely=by+sety)
        tk.Label(lakme_frame,text=rep_label).place(relx=dbx-setx,rely=by+sety)
        tk.Label(lakme_frame,text=rep_label).place(relx=sbx-setx+mx,rely=by+sety)
        tk.Label(lakme_frame,text=rep_label).place(relx=bbx-setx+mx,rely=by+sety)
    if(entry>-1):
        tk.Label(lakme_frame,font=("Helvetica", 16,'bold'),text=gs1).place(relx=tbx+0.15,rely=by+0.3)
        tk.Label(lakme_frame,font=("Helvetica", 16,'bold'),text=gs2).place(relx=dbx+0.15,rely=by+0.3)

def addreddot(entry):
    dotr_pil=(Image.open("reddot.png")).resize((25,25))
    dotr=ImageTk.PhotoImage(dotr_pil)
    rd = tk.Label(lakme_frame,image=dotr)
    rd.image=dotr
    mx=0.045
    if(entry==1):
        rd.place(relx=dsx+mx,rely=dsy)
        tk.Label(lakme_frame,text="Lost Here").place(relx=dsx+mx-0.02,rely=dsy+0.07)
        #rd.place(relx=tbx,rely=by)
    elif(entry==2):
        rd.place(relx=ssx+mx-0.025,rely=ssy)
        tk.Label(lakme_frame,text="Lost Here").place(relx=ssx-0.02+mx-0.025,rely=ssy+0.07)
        #rd.place(relx=dbx,rely=by)
    elif(entry==3):
        rd.place(relx=sbx,rely=by)
        tk.Label(lakme_frame,text="Lost Here").place(relx=sbx+0.03,rely=by+0.01)
    elif(entry==4):
        rd.place(relx=bbx+mx,rely=by)
        tk.Label(lakme_frame,text="Lost Here").place(relx=bbx+0.03+mx,rely=by+0.01)

def tree_init():
    global lakme_frame
    lakme_frame= tk.Frame(root,bg="black",highlightbackground=blue,highlightcolor=blue, highlightthickness=2)
    lakme_frame.place(relx=0.3,rely=0.05,relheight=0.9,relwidth=0.65)
    
    gentree=ImageTk.PhotoImage(Image.open("gentree.jpg"))
    g_label= tk.Label(lakme_frame,image=gentree)
    g_label.image=gentree
    g_label.place(relwidth=1,relheight=1)
    
    tk.Label(lakme_frame,text="Pseudomonas chlororaphis REPINs Clade",font=("Courier", 20)).place(relx=0.12,rely=0.04)
    
    tk.Label(s_frame,font=("Helvetica", 16,'bold'),text="Active Selection: ",bg=blue).place(relx=0,rely=0.65,relwidth=0.5)

def generate(entry):
    tree_init()
    rep_label,entry,genes=repinapi(int(entry),0,1)
    addreddot(entry)
    addrepin(entry,rep_label,genes)

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
    for i in range(7):
        h.append("Hotspot #{}".format(i+1))
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
    generate(-1)

def locgen(x):
    tree_init()
    m= (re.findall('(\d+)..(\d+)',str(x)))
    rep_label,entry,genes=repinapi(int(m[0][0]),int(m[0][1]),2)
    m=str(entry)
    tk.Label(s_frame,text=m).place(relx=0.45,rely=0.65,relwidth=0.15)
    addreddot(entry)
    addrepin(entry,rep_label,genes)

def locationinit():
    sbox1=tk.Entry(s_frame,font=40)
    sbox1.place(relx=0.1,rely=0.1,relwidth=0.5,relheight=0.05)
    
    go_button1 = tk.Button(s_frame,text="Set Range",font=40,command= lambda:locgen(sbox1.get()))
    go_button1.place(relx=0.12,rely=0.16)
    
    tk.Label(s_frame,text="Enter ONLY in the format 12345..12345.",bg=blue).place(relx=0.13,rely=0.25)
    
def maininit():
    #tk.Label(s_frame,bg=blue).place(relx=0,rely=0,relwidth=1,relheight=1)
    tk.Label(s_frame,text=f"Footnote:\nRed Dot-> Lost in evolution\nGreen Dot-> Gained in evolution",font=("Courier", 14)).place(relx=0.1,rely=0.85)
    
    lakme_frame= tk.Frame(root,bg="black",highlightbackground=blue,highlightcolor=blue, highlightthickness=2)
    lakme_frame.place(relx=0.3,rely=0.05,relheight=0.9,relwidth=0.65)
    
    gentree=ImageTk.PhotoImage(Image.open("gentree.jpg"))
    g_label= tk.Label(lakme_frame,image=gentree)
    g_label.image=gentree
    g_label.place(relwidth=1,relheight=1)
    
    tk.Label(lakme_frame,text="Pseudomonas chlororaphis REPINs Clade",font=("Courier", 20)).place(relx=0.12,rely=0.04)

def clear_s_frame():
    tk.Label(s_frame,bg=blue).place(relx=0,rely=0.1,relwidth=0.8,relheight=0.65)

def selected(event):
    maininit()
    if(event.count("Hotspot")!=0):
        clear_s_frame()
        hotspotinit()
    if(event.count("Location")!=0):
        clear_s_frame()
        locationinit()
    return

def main():
    canvas = tk.Canvas(root,height=500,width=1250,bg="white")
    canvas.pack()
    
    #Adding Frame for Search Panel
    ##From Here
    global s_frame
    s_frame = tk.Frame(root, bg=blue)
    s_frame.place(relwidth=0.25,relheight=1,relx=0)
    
    options=["Choose Search Method","Search REPIN by Hotspot","Search REPIN by Location Range"]
    clicked= tk.StringVar()
    clicked.set(options[0])
    
    drop = tk.OptionMenu(s_frame,clicked, *options,command=selected)
    drop.place(relx=0.1,rely=0.04,relwidth=0.7,relheight=0.05)
    
    maininit()
    
    """
    tk.Label(s_frame,text=f"Footnote:\nRed Dot-> Lost in evolution\nGreen Dot-> Gained in evolution",font=("Courier", 14)).place(relx=0.1,rely=0.85)
    
    
    slab=tk.Label(s_frame,text="Search REPIN by Hotspot")
    slab.place(relx=0.1,rely=0.04,relwidth=0.7,relheight=0.05)
    
    #Search Entry
    sbox1=tk.Entry(s_frame,font=40)
    sbox1.place(relx=0.09,rely=0.1,relwidth=0.35,relheight=0.05)
    
    go_button1 = tk.Button(s_frame,text="Set GeneA",font=40,command= lambda:generate(sbox1.get()))
    go_button1.place(relx=0.12,rely=0.16)
    
    sbox2=tk.Entry(s_frame,font=40)
    sbox2.place(relx=0.46,rely=0.1,relwidth=0.35,relheight=0.05)
    
    go_button2 = tk.Button(s_frame,text="Set GeneB",font=40,command= lambda:generate(sbox2.get()))
    go_button2.place(relx=0.49,rely=0.16)
    
    
    #Listbox for hotspots
    h=[]
    for i in range(7):
        h.append("Hotspot #{}".format(i+1))
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
    ##Till Here
    
    generate(-1)
    
    #Adding Frame for Tree Image
    ##From Here
    global tree_frame
    tree_frame= tk.Frame(root,bg="black",highlightbackground=blue,highlightcolor=blue, highlightthickness=2)
    tree_frame.place(relx=0.4,rely=0.05,relheight=0.9,relwidth=0.55)
    
    
    #Adding main Image
    gentree=ImageTk.PhotoImage(Image.open("gentree.jpg"))
    g_label= tk.Label(tree_frame,image=gentree)
    g_label.image=gentree
    g_label.place(relwidth=1,relheight=1)
    
    #Tree Title
    canopy1 = tk.Label(tree_frame,text="Pseudomonas chlororaphis REPINs Clade",font=("Courier", 20))
    canopy1.place(relx=0.12,rely=0.04)
    ##Till Here
    """

if __name__ == '__main__':
    main()
    root.mainloop()