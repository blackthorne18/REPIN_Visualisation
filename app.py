import tkinter as tk
from tkinter import filedialog, Text
import os,time

root=tk.Tk()
blue="#0F97EF"
white="#FFFFFF"

def main():
    canvas = tk.Canvas(root,height=700,width=900,bg="white")
    canvas.pack()
    
    frame = tk.Frame(root, bg=blue)
    frame.place(relwidth=0.35,relheight=1,relx=0)
    
    go_button = tk.Button(root,text="Generate Tree",padx=10,pady=5,fg=blue,bg=blue)
    go_button.pack()
    go_button.place(x=100,y=500)

if __name__ == '__main__':
    st=time.time()
    main()
    root.mainloop()
    print("Runtime: {:0.3}s".format((time.time())-st))