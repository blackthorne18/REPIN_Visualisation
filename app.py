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
tbx,dbx,sbx,bbx=0.12,0.36,0.57,0.8
by=0.6
tsx,tsy=0.33,0.35
dsx,dsy=0.465,0.445
ssx,ssy=0.685,0.53

def addrepin(entry):
    setx,sety=0.09,0.125
    stag=0.05
    rep_label = tk.Label(tree_frame,text="blue 1234567..1234567")
    if(entry=="tbx"):
        rep_label.place(relx=tbx-setx,rely=by+sety)
    elif(entry=="dbx"):
        rep_label.place(relx=dbx-setx,rely=by+sety+stag)
    elif(entry=="sbx"):
        rep_label.place(relx=sbx-setx,rely=by+sety)
    elif(entry=="bbx"):
        rep_label.place(relx=bbx-setx,rely=by+sety+stag)

def addreddot(entry):
    dotr_pil=(Image.open("reddot.png")).resize((25,25))
    dotr=ImageTk.PhotoImage(dotr_pil)
    rd = tk.Label(tree_frame,image=dotr)
    rd.image=dotr
    if(entry=="tbx"):
        rd.place(relx=tbx,rely=by)
    elif(entry=="dbx"):
        rd.place(relx=dbx,rely=by)
    elif(entry=="sbx"):
        rd.place(relx=sbx,rely=by)
    elif(entry=="bbx"):
        rd.place(relx=bbx,rely=by)
    elif(entry=="tsx"):
        rd.place(relx=tsx,rely=tsy)
    elif(entry=="dsx"):
        rd.place(relx=dsx,rely=dsy)
    elif(entry=="ssx"):
        rd.place(relx=ssx,rely=ssy)

def generate(entry):
    m=['tbx','dbx','sbx','bbx','tsx','dsx','ssx']
    addreddot(m[int(entry)-1])
    addrepin(m[int(entry)-1])

def fetch(evt):
    global main_lbx,s_frame
    w = evt.widget
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    m=re.search('(\d+)',value).group()
    tk.Label(s_frame,font=("Helvetica", 16,'bold'),text="Active Selection: ",bg=blue).place(relx=0,rely=0.65,relwidth=0.5)
    tk.Label(s_frame,text=m).place(relx=0.45,rely=0.65,relwidth=0.2)
    generate(m)

def main():
    canvas = tk.Canvas(root,height=500,width=1100,bg="white")
    canvas.pack()
    
    #Adding Frame for Search Panel
    ##From Here
    global s_frame
    s_frame = tk.Frame(root, bg=blue)
    s_frame.place(relwidth=0.35,relheight=1,relx=0)
    
    slab=tk.Label(s_frame,text="Search REPIN by Hotspot")
    slab.place(relx=0.1,rely=0.04,relwidth=0.7,relheight=0.05)
    
    """
    #Search Entry
    sbox1=tk.Entry(s_frame,font=40)
    sbox1.place(relx=0.09,rely=0.1,relwidth=0.35,relheight=0.05)
    
    go_button1 = tk.Button(s_frame,text="Set GeneA",font=40,command= lambda:generate(sbox1.get()))
    go_button1.place(relx=0.12,rely=0.16)
    
    sbox2=tk.Entry(s_frame,font=40)
    sbox2.place(relx=0.46,rely=0.1,relwidth=0.35,relheight=0.05)
    
    go_button2 = tk.Button(s_frame,text="Set GeneB",font=40,command= lambda:generate(sbox2.get()))
    go_button2.place(relx=0.49,rely=0.16)
    """
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
    
    #Adding Frame for Tree Image
    ##From Here
    global tree_frame
    tree_frame= tk.Frame(root,bg="black",highlightbackground=blue,highlightcolor=blue, highlightthickness=2)
    tree_frame.place(relx=0.4,rely=0.05,relheight=0.9,relwidth=0.55)
    
    
    #Adding main Image
    gentree=ImageTk.PhotoImage(Image.open("gentree.jpg"))
    #gentree=tk.PhotoImage(file='gentree.jpg')
    g_label= tk.Label(tree_frame,image=gentree)
    g_label.image=gentree
    g_label.place(relwidth=1,relheight=1)
    
    #Tree Title
    canopy1 = tk.Label(tree_frame,text="Pseudomonas chlororaphis REPINs Clade",font=("Courier", 20))
    canopy1.place(relx=0.12,rely=0.04)
    
    canopy2 = tk.Label(s_frame,text=f"Footnote:\nRed Dot-> Lost in evolution\nGreen Dot-> Gained in evolution",font=("Courier", 14))
    canopy2.place(relx=0.1,rely=0.85)
    ##Till Here
    

if __name__ == '__main__':
    main()
    root.mainloop()