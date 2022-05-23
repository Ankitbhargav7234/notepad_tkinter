import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox

win= tk.Tk()

#DESIGNING THE WINDOW
win.title("Notepad")
win.rowconfigure(0, minsize=800, weight=1)
win.columnconfigure(1, minsize=800, weight=1)

#FUNCTIONS
def open_file():
    filepath=askopenfilename(filetypes=[("Text file","*.txt"),("All files","*.*")])
    if not filepath:
        return 
    txt_edit.delete(1.0,tk.END)
    input_file= open(filepath,"r")
    text=input_file.read()
    txt_edit.insert(tk.END,text)
    
    win.title(f"Notepad_win -{filepath}")

def save_file():
    filepath=asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    output_file= open(filepath,"w")
    text=txt_edit.get(1.0,tk.END)
    output_file.write(text)

    win.title(f"Notepad -{filepath}")

def delete_text():
    status=messagebox.askyesno("Confirm?","Do you want to delete text?")
    if status == True:
        txt_edit.delete(1.0,tk.END)
    
def copy_text():
    global txt
    txt=txt_edit.get(1.0,tk.END)
    

def paste_text():
    txt_edit.insert(1.0,txt)

def paste_text_other():
    txt_edit.insert(1.0,txtt)
    
def new_window():
    #Designing of new window
    top_window=tk.Toplevel()
    top_window.title("New_Notepad")
    top_window.rowconfigure(0, minsize=800, weight=1)
    top_window.columnconfigure(1, minsize=800, weight=1)

    #NEW_WINDOW_FUNCTIONS
    def open_file2():
        filepath=askopenfilename(filetypes=[("Text file","*.txt"),("All files","*.*")])
        if not filepath:
            return 
        txt_edit.delete(1.0,tk.END)
        input_file= open(filepath,"r")
        text=input_file.read()
        txt_edit.insert(tk.END,text)
    
        top_window.title(f"Notepad_win -{filepath}")

    def save_file2():
        filepath=asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        output_file= open(filepath,"w")
        text=txt_edit.get(1.0,tk.END)
        output_file.write(text)

        top_window.title(f"Notepad -{filepath}")

    def delete_text2():
        status=messagebox.askyesno("Confirm?","Do you want to delete text?")
        if status == True:
            txt_edit.delete(1.0,tk.END)
    
    def copy_text2():
        global txtt
        txtt=txt_edit.get(1.0,tk.END)
    

    def paste_text2():
        txt_edit.insert(1.0,txtt)
    
    def paste_text_other2():
        txt_edit.insert(1.0,txt)

    #Designing of text window
    txt_edit = tk.Text(top_window)
    fr_buttons = tk.Frame(top_window, relief=tk.RAISED, bd=2)
    fr_buttons.grid(row=0, column=0, sticky="nsew")
    txt_edit.grid(row=0, column=1, sticky="nsew")

    #NEW_WINDOW_BUTTONS
    #btn_new = tk.Button(fr_buttons, text="New",command=new_window2)
    btn_open = tk.Button(fr_buttons, text="Open",command=open_file2)
    btn_save = tk.Button(fr_buttons, text="Save As...",command=save_file2)
    btn_dlt = tk.Button(fr_buttons, text="Delete",command=delete_text2)
    btn_copy = tk.Button(fr_buttons, text="Copy",command=copy_text2)
    btn_paste = tk.Button(fr_buttons, text="Paste",command=paste_text2)
    btn_paste_other = tk.Button(fr_buttons, text="Paste other",command=paste_text_other2)
    btn_quit=tk.Button(fr_buttons,text="quit",command=top_window.destroy)

    #btn_new.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
    btn_open.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
    btn_dlt.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
    btn_copy.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
    btn_paste.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)
    btn_paste_other.grid(row=5,column=0,sticky="nsew",padx=5,pady=5)
    btn_quit.grid(row=6,column=0, sticky="nsew", padx=5, pady=5)


#BUTTONS
txt_edit = tk.Text(win)
fr_buttons = tk.Frame(win, relief=tk.RAISED, bd=2)
fr_buttons.grid(row=0, column=0, sticky="nsew")
txt_edit.grid(row=0, column=1, sticky="nsew")

btn_new = tk.Button(fr_buttons, text="New",command=new_window)
btn_open = tk.Button(fr_buttons, text="Open",command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...",command=save_file)
btn_dlt = tk.Button(fr_buttons, text="Delete",command=delete_text)
btn_copy = tk.Button(fr_buttons, text="Copy",command=copy_text)
btn_paste = tk.Button(fr_buttons, text="Paste",command=paste_text)
btn_paste_other = tk.Button(fr_buttons, text="Paste other",command=paste_text_other)
btn_quit = tk.Button(fr_buttons,text="quit",command=win.destroy)


#BUTTON GRIDS
btn_new.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
btn_open.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
btn_save.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
btn_dlt.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
btn_copy.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)
btn_paste.grid(row=5, column=0, sticky="nsew", padx=5, pady=5)
btn_paste_other.grid(row=6,column=0,sticky="nsew",padx=5,pady=5)
btn_quit.grid(row=7,column=0,sticky='nsew',padx=5,pady=5)


win.mainloop()