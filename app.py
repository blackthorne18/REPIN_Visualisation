import tkinter as tk
from tkinter import filedialog, Text
import os,time

root=tk.Tk()
root.title("REPINs Through Time")
blue="#0F97EF"
white="#FFFFFF"

def main():
    canvas = tk.Canvas(root,height=500,width=900,bg="white")
    canvas.pack()
    
    
    s_frame = tk.Frame(root, bg=blue)
    s_frame.place(relwidth=0.35,relheight=1,relx=0)
    
    slab=tk.Label(s_frame,text="Search REPIN by location")
    slab.place(relx=0.1,rely=0.04,relwidth=0.7,relheight=0.05)
    
    sbox=tk.Entry(s_frame,font=40)
    sbox.place(relx=0.1,rely=0.1,relwidth=0.7,relheight=0.05)
    
    tree_frame= tk.Frame(root,highlightbackground=blue,highlightcolor=blue, highlightthickness=2)
    tree_frame.place(relx=0.4,rely=0.05,relheight=0.9,relwidth=0.55)
    
    go_button = tk.Button(s_frame,text="Generate Tree",font=40)
    go_button.place(relx=0.25,rely=0.75)

if __name__ == '__main__':
    main()
    root.mainloop()