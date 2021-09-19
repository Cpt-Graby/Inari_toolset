import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd



class Inari_app(tk.Frame):

    def __init__(self, root):
        self.root=root
        self.root.title("Inari - Manipulateur de sgf facile")
        self.root.geometry("600x250")
        mainframe = tk.Frame(root, bg = "red")
        mainframe.grid(column =0, row=0,sticky=("N", "W", "E", "S"))
        # Setting up the other frame and function
        self.config_choose_directory_frame(mainframe)
        self.config_notebook(mainframe)
        #Griding
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)



    def config_choose_directory_frame(self, mainframe):
        """This function will set the choose directory frame """

        self.ini_frame = tk.Frame(mainframe, bd = 10, bg="green")
        self.select_dir = tk.Button(self.ini_frame, text='Select directory',
                                        command= lambda: calldir(self))
        self.path = tk.StringVar()
        self.show_res = tk.Label(self.ini_frame, textvariable = self.path)
        self.listfile = tk.Listbox(self.ini_frame)

        # Setting all the grid for the elements of choose directory
        self.ini_frame.grid(column =0, row=0,sticky=("N", "W", "E",))
        self.ini_frame.columnconfigure(0, weight =1)
        self.ini_frame.rowconfigure(0, weight =1)
        self.select_dir.grid(column=0, row=0)
        self.show_res.grid(column=0, row=1)
        self.listfile.grid(column=2, row=0, columnspan=2,
                                rowspan=2,sticky=("n","s","e"))
        pass


    def config_notebook(self, mainframe):
        """Setting up the notebook"""
        self.options_prog =tk.ttk.Notebook(mainframe)
        self.options_prog.grid(column=0, row=4, columnspan=4,
                                rowspan=4,sticky=("n","s","e","w"))
        self.change_word_option(self.options_prog)

        self.options_prog.columnconfigure(0, weight=1)
        self.options_prog.rowconfigure(0, weight=1)

        pass


    def change_word_option(self, options_prog):
        """ Setting up the first application of the notebook: change word"""
        self.change_word_frame = tk.Frame(self.options_prog, bg="blue")
        self.options_prog.add(self.change_word_frame, text="Change Word")

        # Entry widget for the new word
        self.new_word_label = tk.Label(self.change_word_frame, text="New word")
        self.new_word = tk.StringVar()
        self.entry_new_word = tk.Entry(self.change_word_frame,
                                        textvariable = self.new_word)
        # Entry widget for the old word
        self.old_word_label = tk.Label(self.change_word_frame, text="Old word")
        self.old_word = tk.StringVar()
        self.entry_old_word = tk.Entry(self.change_word_frame,
                                            textvariable = self.old_word)
        # Button for calling the command
        self.replace_term = tk.Button(self.change_word_frame,
                                            text='Change Word: ',
                                            command= lambda: replace_word(self))
        # Flag for the button replace word
        self.task_change_word = tk.StringVar()
        self.task_flag_change_word = tk.Label(self.change_word_frame,
                                                textvariable = self.task_change_word)


        self.new_word_label.grid(column=0, row=3)
        self.entry_new_word.grid(column=0, row=4)
        self.old_word_label.grid(column=1, row=3)
        self.entry_old_word.grid(column=1, row=4)
        self.replace_term.grid(column=3, row=4, columnspan=2)
        self.task_flag_change_word.grid(column=6, row=4, columnspan=2)
        pass

# -------- All the function will be here -----------
"""
    def calldir():

        self.path.set(fd.askdirectory())
        # print(self.path)
        for file in os.listdir(path.get()):
            self.listfile.insert(tk.END, file)
            print(file)

    def replace_word():

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
            # sgf_string = sgf_string.replace(new_word, old_word)

"""

if __name__ == '__main__':
   root = tk.Tk()
   main_app =  Inari_app(root)
   root.mainloop()
