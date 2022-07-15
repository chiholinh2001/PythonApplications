from tkinter import *
from PIL import Image, ImageTk
import customtkinter



class Dashboard:
    def __init__(self, window):
        self.window = window
        self.window.title("Melt Your Picture")
        self.window.geometry("1366x768")
        self.window.state("zoomed")
        self.window.config(background="#eff5f6")
        # iconWindow = PhotoImage(file="iconWindow.png")
        # self.window.iconphoto(True, iconWindow)

        #======================================HEADER==================================

        self.header = Frame(self.window, bg="#009df4")
        self.header.place(x=300, y=0, width=1240, height=60)
        self.logout_text = Button(self.window, text="Logout", bg="#32cf8e", font=("", 13, "bold"), bd=0, fg="white",
                                  cursor="hand2", activebackground="#32cf8e")
        self.logout_text.place(x=1300, y=15)
        # ======================================SIDEBAR==================================
        self.sidebar = Frame(self.window, bg="#ffffff")
        self.sidebar.place(x=0, y=0, width=300, height=840)
        # ======================================BODY==================================
        self.heading = Label(self.window, text="Dashboard", font=("", 13, "bold"), fg="#ffffff", bg="#eff5f6")
        self.heading.place(x=325, y = 34)

def win():
    window = Tk()
    Dashboard(window)
    window.mainloop()

if __name__ ==  "__main__":
    win()