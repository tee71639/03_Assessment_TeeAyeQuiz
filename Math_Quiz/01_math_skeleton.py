from tkinter import *
from functools import partial # to prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # gui for main menu with difficulty selection and instructions
        self.menu_frame = Frame(padx=10, pady=10)
        self.menu_frame.grid()

        # quiz header (row 0)
        self.quiz_label = Label(self.menu_frame, text="super hard math quiz (IMPOSSIBLE)", font="arial 19 bold")
        self.quiz_label.grid(row=0)

        # difficulty selection buttons (row 1 & 2)
        self.choose_text = Label(self.menu_frame, text="choose your difficulty:", font="arial 12", pady=30)
        self.choose_text.grid(row=1)

        self.difficulty_box = Frame(self.menu_frame, padx=10, pady=50)
        self.difficulty_box.grid(row=2)

        self.easy_button = Button(self.difficulty_box, text="easy", font="arial 14", justify=CENTER)
        self.easy_button.grid(row=0, column=0)

        self.normal_button = Button(self.difficulty_box, text="normal", font="arial 14", justify=CENTER)
        self.normal_button.grid(row=0, column=1)

        self.hard_button = Button(self.difficulty_box, text="hard", font="arial 14", justify=CENTER)
        self.hard_button.grid(row=0, column=2)

        # how to play and quit buttons (row 3)
        self.support_frame = Frame(self.menu_frame, padx=10, pady=10)
        self.support_frame.grid(row=3)

        self.howplay_button = Button(self.support_frame, text="how to play", font="arial 15 bold")
        self.howplay_button.grid(row=0, column=0)

        self.quit_button = Button(self.support_frame, text="quit", font="arial 15 bold")
        self.quit_button.grid(row=0, column=1)





# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("super hard math quiz (IMPOSSIBLE)")
    something = Start(root)
    root.mainloop()
