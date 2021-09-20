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
        mainframe.columnconfigure(0, weight = 1)
        mainframe.rowconfigure(0, weight = 1)
        self.root.columnconfigure(0, weight = 1)
        self.root.rowconfigure(0, weight = 1)

# -------- All the function will be here -----------
    def calldir(self):
        self.path.set(fd.askdirectory())
        # print(self.path)
        self.files = sorted(os.listdir(self.path.get()))
        print(self.files)
        for file in self.files:
            self.listfile.insert(tk.END, file)
            print(file)
        pass

    def replace_word(self):
        """ Function that replace the word in all the file in the directory"""
        new_word = self.entry_new_word.get()
        old_word = self.entry_old_word.get()
        if new_word != "":
            self.task_change_word.set("Done: " + new_word)
            for file in self.files:
                path_temp = self.path.get() + "/" + file
                with open(path_temp, '+r') as f:
                    sgf_str = f.read()
                sgf_str = sgf_str.replace(self.old_word.get(),
                                                self.new_word.get())
                with open(path_temp, '+w') as f2:
                    f2.write(sgf_str)


        else:
            warning_no_word = tk.messagebox.showwarning(title="WARNING",
                                    message="You haven't entered a new word")
            # sgf_string = sgf_string.replace(new_word, old_word)


# --------All windows setting option will be under here-----------
    def config_choose_directory_frame(self, mainframe):
        """This function will set the choose directory frame """

        self.ini_frame = tk.Frame(mainframe, bd = 10)
        self.path = tk.StringVar()
        self.select_dir = tk.Button(self.ini_frame, text='Select directory',
                                        command= self.calldir)

        self.show_res = tk.Label(self.ini_frame, textvariable = self.path)
        self.listfile = tk.Listbox(self.ini_frame)

        # Setting all the grid for the elements of choose directory
        self.ini_frame.grid(column =0, row=0,sticky=("N", "W", "E","S"))
        self.ini_frame.columnconfigure(0, weight =1)
        self.ini_frame.columnconfigure(1, weight =1)
        self.ini_frame.rowconfigure(0, weight =1)
        self.ini_frame.rowconfigure(1, weight =1)


        self.select_dir.grid(column=0, row=0)
        self.show_res.grid(column=0, row=1)
        self.listfile.grid(column=1, row=0, columnspan=2,
                                rowspan=2,sticky=("n","s","e","w"))
        pass


    def config_notebook(self, mainframe):
        """Setting up the notebook"""
        self.options_prog =tk.ttk.Notebook(mainframe)
        self.options_prog.grid(column=0, row=3, columnspan=3,
                                rowspan=3,sticky=("n","s","e","w"))

        self.change_word_option(self.options_prog)
        self.next_option(self.options_prog)

        self.options_prog.columnconfigure(0, weight=1)
        self.options_prog.rowconfigure(0, weight=1)
        pass


    def change_word_option(self, options_prog):
        """ Setting up the first application of the notebook: change word"""
        self.change_word_frame = tk.Frame(self.options_prog)
        self.options_prog.add(self.change_word_frame, text="Change Word")

        # Entry widget for the old word
        self.old_word = tk.StringVar()
        self.old_word_label = tk.Label(self.change_word_frame,
                                            text="Word to change")

        self.entry_old_word = tk.Entry(self.change_word_frame,
                                            textvariable = self.old_word)

        # Entry widget for the new word
        self.new_word = tk.StringVar()
        self.new_word_label = tk.Label(self.change_word_frame, text="New word")

        self.entry_new_word = tk.Entry(self.change_word_frame,
                                        textvariable = self.new_word)

        # Button for calling the command
        self.replace_term = tk.Button(self.change_word_frame,
                                            text='Change Word: ',
                                            command= self.replace_word)

        # Flag for the button replace word
        self.task_change_word = tk.StringVar()
        self.task_flag_change_word = tk.Label(self.change_word_frame,
                                                textvariable
                                                = self.task_change_word)

        # Gridding option of all the element in the change word option
        self.old_word_label.grid(column=0, row=1)
        self.entry_old_word.grid(column=0, row=2)
        self.new_word_label.grid(column=1, row=1)
        self.entry_new_word.grid(column=1, row=2)
        self.replace_term.grid(column=3, row=2, columnspan=2)
        self.task_flag_change_word.grid(column=6, row=2, columnspan=2)
        pass

    def next_option(self, options_prog):
        self.next_options_frame = tk.Frame(self.options_prog)
        options_prog.add(self.next_options_frame, text="Next options frame")

        Message = tk.Label(self.next_options_frame, text="Viens me donner des idées")
        Message.grid()

if __name__ == '__main__':
   root = tk.Tk()
   main_app =  Inari_app(root)
   root.mainloop()
