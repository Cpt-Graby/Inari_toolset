import os
import tkinter as tk
from tkinter import filedialog as fd

# -----------Setting Inital windows -----

class Inari_app(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.title("Inari - Manipulateur de sgf facile")
        self.content=tk.Frame__init(self, master)
        self.content.grid(column=0, row=0, sticky=("n","s","e","w"))
        self.content.columnconfigure(0, weight=3)
        self.content.columnconfigure(1, weight=3)
        self.content.columnconfigure(2, weight=3)
        self.content.columnconfigure(3, weight=1)
        self.content.columnconfigure(4, weight=1)
        self.content.rowconfigure(1, weight=1)
        pass
    
    def config_choose_directory_frame(self):
        """Setting up the choose directory frame and gui"""
        self.ini_frame = tk.Frame(self.content, bd=5)
        self.select_dir = tk.Button(self.ini_frame, text='Select directory',command=calldir)
        self.path = tk.StringVar()
        self.show_res = tk.Label(self.ini_frame, textvariable = path )
        #Griding
        self.ini_frame.grid(column=0, row=0, columnspan=4, rowspan=3,sticky=("n","e","w"))
        self.select_dir.grid(column=0, row=1, padx=5)
        self.show_res.grid(column=0, row=2)
        
        pass
    
    def config_choose_directory_frame(self):
        self.manip_frame = tk.Frame(self.content, bd=5)
        # Entry widget for the new word
        self.new_word_label = tk.Label(self.manip_frame, text="New word")
        self.new_word = tk.StringVar()
        self.entry_new_word = tk.Entry(manip_frame, textvariable = new_word)

        # Entry widget for the old word
        self.old_word_label = tk.Label(self.manip_frame, text="Old word")
        self.old_word = tk.StringVar()
        self.entry_old_word = tk.Entry(self.manip_frame, textvariable = old_word)

        self.replace_term = tk.Button(self.manip_frame, text='Change Term: ',command=replace_word)

        # Flag for the button replace word
        task_change_word = tk.StringVar()
        task_flag_change_word = tk.Label(self.manip_frame, textvariable = task_change_word )
        
        #Griding
        self.manip_frame.grid(column=0, row=3, columnspan=4, rowspan=3, sticky=("s","e","w"))
        self.new_word_label.grid(column=0, row=3)
        self.entry_new_word.grid(column=0, row=4)
        self.old_word_label.grid(column=1, row=3)
        self.entry_old_word.grid(column=1, row=4)
        self.replace_term.grid(column=3, row=4, columnspan=2)
        self.task_flag_change_word.grid(column=6, row=4, columnspan=2)

        pass
    

# -------- All the function will be here -----------
def calldir():
    """This fuction will ask the directory where the app must work"""

    path.set(fd.askdirectory())

def replace_word():
    """This function will replace the given word with the new word"""
    new_word = entry_new_word.get()
    old_word = entry_old_word.get()
    if new_word != "":
        task_change_word.set("Done: "+new_word)
        print(new_word)
    else:
        warning_no_word= tk.Toplevel(app)
        warning_no_word.title("WARNING")
        warning_label=tk.Label(warning_no_word, text=" You haven't enterd a new word")
        warning_label.grid()
    #sgf_string = sgf_string.replace(new_word, old_word)


if __name__ == '__main__':
   root = tk.Tk()
   main_app =  Inari_app(root)
   root.mainloop()

