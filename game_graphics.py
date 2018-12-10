from tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Tic-Tac-Toe")

        self.label = Label(master, text="Tic-Tac-Toe")
        self.label.grid(columnspan=2)

        self.NW_button = Button(master, text="(1, 1)", command=self.disp('1, 1'))
        self.NW_button.grid(row = 1, column = 1)

        self.N_button = Button(master, text="(1, 2)", command=self.disp('1, 2'))
        self.N_button.grid(row=1, column=2)

        self.NE_button = Button(master, text="(1, 3)", command=self.disp('1, 3'))
        self.NE_button.grid(row=1, column=3)

        self.W_button = Button(master, text="(2, 1)", command=self.disp('2, 1'))
        self.W_button.grid(row=2, column=1)

        self.C_button = Button(master, text="(2, 2)", command=self.disp('2, 2'))
        self.C_button.grid(row=2, column=2)

        self.E_button = Button(master, text="(2, 3)", command=self.disp('2, 3'))
        self.E_button.grid(row=2, column=3)

        self.NE_button = Button(master, text="(3, 1)", command=self.disp('3, 1'))
        self.NE_button.grid(row = 3, column = 1)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(columnspan = 3, row = 4)

        self.S_button = Button(master, text="(3, 2)", command=self.disp('3, 2'))
        self.S_button.grid(row=3, column=2)

        self.SE_button = Button(master, text="(3, 3)", command=self.disp('3, 3'))
        self.SE_button.grid(row=3, column=3)

    def disp(self, pos: str):
        print(pos)

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()