from tkinter import *
from functools import partial # to prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # gui to get starting balance and stakes
        self.start_frame = Frame(parent)
        self.start_frame.grid()

        self.push_button = Button(self.start_frame, text="Push Now", command=self.to_game)
        self.push_button.grid(row=1)

    def to_game(self):

        # retrieve starting balance
        starting_balance = 50
        stakes = 2

        self.start_frame.destroy()
        Game(self, stakes, starting_balance)


class Game:

    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        # initialise variables
        self.balance = IntVar()
        # set starting balance to amount entered by user at start of game
        self.balance.set(starting_balance)

        # get value of stakes (use it as multiplier when calculating winnings)
        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        # list for holding statistics
        self.round_stats_list = []

        # play gui setup
        self.game_box = Toplevel()

        # if users press corss at top right, game quits
        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # heading row (row 0)
        self.heading_label = Label(self.game_frame, wrap=300, justify=LEFT, text="Play...", font="Arial 24 bold", padx=10, pady=10)
        self.heading_label.grid(row=0)

        # instructions (row 1)
        self.instructions_label = Label(self.game_frame, wrap=300, justify=LEFT, text="Press <enter> or click the 'Open " "Boxes' button to reveal the " "contents of the mystery boxes.", font="Arial 10", padx=10, pady=10)
        self.instructions_label.grid(row=1)

        # boxes go here (row 2)

        self.box_frame = Frame(self.game_frame)
        self.box_frame.grid(row=2, pady=10)

        photo = PhotoImage(file="question.gif")

        self.prize1_label = Label(self.box_frame, image=photo, padx=10, pady=10)
        self.prize1_label.photo = photo
        self.prize1_label.grid(row=0, column=0)

        self.prize2_label = Label(self.box_frame, image=photo, padx=10, pady=10)
        self.prize2_label.photo = photo
        self.prize2_label.grid(row=0, column=1, padx=10)

        self.prize3_label = Label(self.box_frame, image=photo, padx=10, pady=10)
        self.prize3_label.photo = photo
        self.prize3_label.grid(row=0, column=2)

        # play button goes here (row 3)
        self.play_button = Button(self.game_frame, text="Open Boxes", bg ="#FFFF33", font="Arial 15 bold", width=20, padx=10, pady=10, command=self.reveal_boxes)
        self.play_button.grid(row=3)

        # bind button to <enter> (users can push enter to reveal the boxes)

        self.play_button.focus()
        self.play_button.bind('<Return>', lambda e: self.reveal_boxes())
        self.play_button.grid(row=3)

        # cost & balance label (row 4)

        start_text = "Game Cost: ${} \n How much will you win?".format(stakes * 5)

        self.balance_label = Label(self.game_frame, font="Arial 12 bold", fg="green", text=start_text, wrap=300, justify=LEFT)
        self.balance_label.grid(row=4, pady=10)

        # help and game stats button (row 5)
        self.help_export_frame = Frame(self.game_frame)
        self.help_export_frame.grid(row=5, pady=10)
        
        self.help_button = Button(self.help_export_frame, text="Help / Rules", font="Arial 15 bold", bg="#808080", fg="white")
        self.help_button.grid(row=0, column=0, padx=2)

        self.stats_button = Button(self.help_export_frame, text="Game Stats...", font="Arial 15 bold", bg="#003366", fg="white")
        self.stats_button.grid(row=0, column=1, padx=2)

        # quit button (row 6)
        self.quit_button = Button(self.game_frame, text="Quit", fg="white", bg="#660000", font="Arial 15 bold", width=20, command=self.to_quit, padx=10, pady=10)
        self.quit_button.grid(row=6, pady=10)

    def reveal_boxes(self):
        # retrieve the balance from the initial function
        current_balance = self.balance.get()
        stakes_multiplier = self.multiplier.get()

        round_winnings = 0
        prizes = []
        stats_prizes = []

        for item in range(0, 3):
            prize_num = random.randint(1,100)

            if 0 < prize_num <= 5:
                prize = PhotoImage(file="gold_low.gif")
                prize_list = "gold (${})".format(5* stakes_multiplier)
                round_winnings += 5 * stakes_multiplier
            elif 5 < prize_num <= 25:
                prize = PhotoImage(file="silver_low.gif")
                prize_list = "silver (${})".format(2* stakes_multiplier)
                round_winnings += 2 * stakes_multiplier
            elif 25 < prize_num <= 65:
                prize = PhotoImage(file="copper_low.gif")
                prize_list = "copper (${})".format(1* stakes_multiplier)
                round_winnings += 1 * stakes_multiplier
            else:
                prize = PhotoImage(file="lead_low.gif")
                prize_list = "lead ($0)"
            
            prizes.append(prize)
            stats_prizes.append(prize_list)

        photo1 = prizes[0]
        photo2 = prizes[1]
        photo3 = prizes[2]

        # display prizes and edit background
        self.prize1_label.config(image=photo1)
        self.prize1_label.photo = photo1
        self.prize2_label.config(image=photo2)
        self.prize1_label.photo = photo2
        self.prize3_label.config(image=photo3)
        self.prize1_label.photo = photo3

        # deduct cost of game
        current_balance -= 5 * stakes_multiplier

        # add winnings
        current_balance += round_winnings
        
        # set balance to new balance
        self.balance.set(current_balance)

        balance_statement = "Game Cost: ${}\nPayback: ${} \nCurrent Balance: ${}".format(5 * stakes_multiplier, round_winnings, current_balance)

        # edit label so user can see their balance
        self.balance_label.configure(text=balance_statement)

        # stop user from playing if their balance is too low
        if current_balance < 5 * stakes_multiplier:
            self.play_button.config(state=DISABLED)
            self.game_box.focus()
            self.play_button.config(text="Game Over")

            balance_statement = "Current Balance: ${}\n Your balance is too low. You can only quit or view your stats. Sorry about that.".format(current_balance)
            self.balance_label.config(fg="#660000", font="Arial 10 bold", text=balance_statement)

    def to_quit(self):
        root.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()
