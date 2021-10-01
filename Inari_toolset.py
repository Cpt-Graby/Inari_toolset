import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd



class Inari_app(tk.Frame):

    def __init__(self, root):
        self.root=root
        self.root.title("Inari - Manipulateur de sgf facile")
        self.root.geometry("500x400")
        mainframe = tk.Frame(root, bg = "red")
        mainframe.grid(column =0, row=0,sticky=("N", "W", "E", "S"))

        # Setting up the other frame and function
        self.config_notebook_of_workplace(mainframe)

        #Griding
        mainframe.columnconfigure(0, weight = 1)
        mainframe.rowconfigure(0, weight = 1)
        self.root.columnconfigure(0, weight = 1)
        self.root.rowconfigure(0, weight = 1)

# -------- All the function will be here -----------
    def calldir(self):
        """ Function that call the ask for the directory"""
        self.path.set(fd.askdirectory())
        # print(self.path)
        self.files = sorted(os.listdir(self.path.get()))
        print(self.files)
        for file in self.files:
            self.listfile.insert(tk.END, file)
            print(file)


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


# --------All windows setting option will be under here-----------
    def config_notebook_of_workplace(self, mainframe):
        """Function to set the workplace. So that the user can decide if he
        wants to work on one file or on a directory"""

        self.workspace_notebook =tk.ttk.Notebook(mainframe)
        self.workspace_notebook.grid(sticky=("N", "W", "E", "S"))

        self.workspace_on_directory =tk.Frame(self.workspace_notebook)
        self.workspace_notebook.add(self.workspace_on_directory, text="Directory")
        self.config_choose_directory_frame(self.workspace_on_directory)
        self.config_notebook_directory_task(self.workspace_on_directory)

        self.workspace_on_file =tk.Frame(self.workspace_notebook)
        self.workspace_notebook.add(self.workspace_on_file, text="File")
        self.config_choose_file_frame(self.workspace_on_file)

        self.workspace_notebook.columnconfigure(0, weight=1)
        self.workspace_notebook.rowconfigure(0, weight=1)
        self.workspace_on_directory.columnconfigure(0, weight=1)
        self.workspace_on_directory.rowconfigure(0, weight=1)
        self.workspace_on_file.columnconfigure(0, weight=1)
        self.workspace_on_file.rowconfigure(0, weight=1)

    def config_choose_file_frame(self, mainframe):
            """Function for the directory workspace.
             config_choose_directory_frame() function will set the
             "Choose directory" frame """

            self.ini_file_frame = tk.Frame(mainframe,bg="green" bd = 10)
            #self.path = tk.StringVar()
            #self.select_dir = tk.Button(self.ini_frame, text='Select directory',
                                            command= self.calldir)

            self.show_res = tk.Label(self.ini_file_frame, textvariable = self.path)
            self.listfile = tk.Listbox(self.ini_file_frame)

            # Setting all the grid for the elements of choose directory
            self.ini_file_frame.grid(sticky=("N", "W", "E","S"))
            self.ini_file_frame.columnconfigure(0, weight =1)
            #self.ini_frame.columnconfigure(1, weight =1)
            self.ini_file_frame.rowconfigure(0, weight =1)
            self.ini_file_frame.rowconfigure(1, weight =1)

            #self.select_dir.grid(column=0, row=0, columnspan=2)
            #self.show_res.grid(column=0, row=1)
            #self.listfile.grid(column=2, row=0, columnspan=2,
                                    rowspan=2,sticky=("n","s","e","w"))
#
    def config_choose_directory_frame(self, mainframe):
        """Function for the directory workspace.
         config_choose_directory_frame() function will set the
         "Choose directory" frame """

        self.ini_frame = tk.Frame(mainframe, bd = 10)
        self.path = tk.StringVar()
        self.select_dir = tk.Button(self.ini_frame, text='Select directory',
                                        command= self.calldir)

        self.show_res = tk.Label(self.ini_frame, textvariable = self.path)
        self.listfile = tk.Listbox(self.ini_frame)

        # Setting all the grid for the elements of choose directory
        self.ini_frame.grid(sticky=("N", "W", "E","S"))
        self.ini_frame.columnconfigure(0, weight =1)
        #self.ini_frame.columnconfigure(1, weight =1)
        self.ini_frame.rowconfigure(0, weight =1)
        self.ini_frame.rowconfigure(1, weight =1)

        self.select_dir.grid(column=0, row=0, columnspan=2)
        self.show_res.grid(column=0, row=1)
        self.listfile.grid(column=2, row=0, columnspan=2,
                                rowspan=2,sticky=("n","s","e","w"))

    def config_notebook_directory_task(self, mainframe):
        """Function for the directory workspace.
        Setting up the notebook"""
        self.options_prog_directory =tk.ttk.Notebook(mainframe)
        self.options_prog_directory.grid(column=0,row=3,
                                            sticky=("N","S","E","W"))

        self.change_word_option(self.options_prog_directory)
        self.next_option(self.options_prog_directory)

        self.options_prog_directory.columnconfigure(0, weight=1)
        self.options_prog_directory.rowconfigure(0, weight=1)
        pass

    def change_word_option(self, options_prog_directory):
        """Function for the directory workspace.
        Setting up the first application of the notebook: change word"""
        self.change_word_frame = tk.Frame(self.options_prog_directory)
        self.options_prog_directory.add(self.change_word_frame,
                                            text="Change Word")

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

    def next_option(self, options_prog_directory):
        """Function for the directory workspace."""
        self.next_options_frame = tk.Frame(self.options_prog_directory)
        options_prog_directory.add(self.next_options_frame, text="Next options frame")

        Message = tk.Label(self.next_options_frame, text="Viens me donner des idées")
        Message.grid()

if __name__ == '__main__':
   root = tk.Tk()
   main_app =  Inari_app(root)
   root.mainloop()
