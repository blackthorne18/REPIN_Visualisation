import tkinter as tk
from tkinter import filedialog, Text
from PIL import ImageTk, Image
import os,time

root=tk.Tk()
root.title("REPINs Through Time")
blue="#0F97EF"
white="#FFFFFF"
tree_frame=None
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
    addreddot(entry)
    addrepin(entry)

def main():
    canvas = tk.Canvas(root,height=500,width=1100,bg="white")
    canvas.pack()
    
    #Adding Frame for Search Panel
    ##From Here
    s_frame = tk.Frame(root, bg=blue)
    s_frame.place(relwidth=0.35,relheight=1,relx=0)
    
    slab=tk.Label(s_frame,text="Search REPIN by location")
    slab.place(relx=0.1,rely=0.04,relwidth=0.7,relheight=0.05)
    
    #Search Entry
    sbox=tk.Entry(s_frame,font=40)
    sbox.place(relx=0.1,rely=0.1,relwidth=0.7,relheight=0.05)
    
    go_button = tk.Button(s_frame,text="Generate Tree",font=40,command= lambda:generate(sbox.get()))
    go_button.place(relx=0.25,rely=0.2)
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
    
    ##Till Here
    

if __name__ == '__main__':
    main()
    root.mainloop()