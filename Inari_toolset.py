import os
import tkinter as tk
from tkinter import filedialog as fd

# -----------Setting Inital windows -----
app = tk.Tk()
app.title("Inari - Manipulateur de sgf facile")

content = tk.Frame(app)
ini_frame = tk.Frame(content, bd=5)
manip_frame = tk.Frame(content, bd=5)


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


# --------- Different Frame -------------

select_dir = tk.Button(ini_frame, text='Select directory',command=calldir)
path = tk.StringVar()
show_res = tk.Label(ini_frame, textvariable = path )


# Entry widget for the new word
new_word_label = tk.Label(manip_frame, text="New word")
new_word = tk.StringVar()
entry_new_word = tk.Entry(manip_frame, textvariable = new_word)

# Entry widget for the old word
old_word_label = tk.Label(manip_frame, text="Old word")
old_word = tk.StringVar()
entry_old_word = tk.Entry(manip_frame, textvariable = old_word)

replace_term = tk.Button(manip_frame, text='Change Term: ',command=replace_word)

# Flag for the button replace word
task_change_word = tk.StringVar()
task_flag_change_word = tk.Label(manip_frame, textvariable = task_change_word )

# ---------------------Gridding ----------------

content.grid(column=0, row=0, sticky=("n","s","e","w"))

# -- ini_frame-----
ini_frame.grid(column=0, row=0, columnspan=4, rowspan=3,sticky=("n","e","w"))
select_dir.grid(column=0, row=1, padx=5)
show_res.grid(column=0, row=2)

# -- Manip_frame------
manip_frame.grid(column=0, row=3, columnspan=4, rowspan=3, sticky=("s","e","w"))
new_word_label.grid(column=0, row=3)
entry_new_word.grid(column=0, row=4)
old_word_label.grid(column=1, row=3)
entry_old_word.grid(column=1, row=4)
replace_term.grid(column=3, row=4, columnspan=2)
task_flag_change_word.grid(column=6, row=4, columnspan=2)

app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

app.mainloop()
