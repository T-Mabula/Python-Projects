from tkinter import *

class MyFirstGUI:
    btn_width = 12
    btn_height = 4
    def __init__(self, master):
        self.master = master
        master.title("Tic-Tac-Toe")

        self.label = Label(master, text="Tic-Tac-Toe")
        self.label.grid(columnspan=3)

        self.NW_button = Button(master, text="NW", height = self.btn_height, width = self.btn_width,  command=self.disp('1, 1'))
        self.NW_button.grid(row = 1, column = 1)

        self.N_button = Button(master, text="N", height = self.btn_height, width = self.btn_width, command=self.disp('1, 2'))
        self.N_button.grid(row=1, column=2)

        self.NE_button = Button(master, text="NE", height = self.btn_height, width = self.btn_width, command=self.disp('1, 3'))
        self.NE_button.grid(row=1, column=3)

        self.W_button = Button(master, text="W", height = self.btn_height, width = self.btn_width, command=self.disp('2, 1'))
        self.W_button.grid(row=2, column=1)

        self.C_button = Button(master, text="C", height = self.btn_height, width = self.btn_width, command=self.disp('2, 2'))
        self.C_button.grid(row=2, column=2)

        self.E_button = Button(master, text="E", height = self.btn_height, width = self.btn_width, command=self.disp('2, 3'))
        self.E_button.grid(row=2, column=3)

        self.NE_button = Button(master, text="SW", height = self.btn_height, width = self.btn_width, command=self.disp('3, 1'))
        self.NE_button.grid(row = 3, column = 1)

        self.S_button = Button(master, text="S", height = self.btn_height, width = self.btn_width, command=self.disp('3, 2'))
        self.S_button.grid(row=3, column=2)

        self.SE_button = Button(master, text="SE",height = self.btn_height, width = self.btn_width, command=self.disp('3, 3'))
        self.SE_button.grid(row=3, column=3)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(columnspan = 3, row = 4)

    def disp(self, pos: str):
        print(pos)

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()