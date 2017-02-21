from tkinter import *


class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):

        Frame.__init__(self, master)   


        self.master = master

        self.init_window()

    #Creation of init_window
    def init_window(self):

        self.master.title("My Control files")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Undo")

        #added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)

    
    def client_exit(self):
        exit()

        

root = Tk()

root.geometry("700x300")

#creation of an instance
app = Window(root)


root.mainloop()  
