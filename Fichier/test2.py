import tkinter as tk
import random

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("TicTacToe")
        self.root.minsize(500, 500)

        self.buttons = []
        self.current_player = 'X'
        self.win = False
        self.ia_enabled = False
        self.ia_difficulty = None

        self.create_mode_selection()

    def create_mode_selection(self):
        self.mode_frame = tk.Frame(self.root)
        mode_var = tk.StringVar(value="2 Joueurs")
        difficulty_var = tk.StringVar(value="Facile")

        tk.Radiobutton(self.mode_frame, text="1 Joueur", variable=mode_var, value="1 Joueur",
                       command=lambda: self.difficulty_menu.config(state="normal")).pack()
        tk.Radiobutton(self.mode_frame, text="2 Joueurs", variable=mode_var, value="2 Joueurs",
                       command=lambda: self.difficulty_menu.config(state="disabled")).pack()

        self.difficulty_menu = tk.OptionMenu(self.mode_frame, difficulty_var, "Facile", "Moyen", "Difficile")
        self.difficulty_menu.pack()

        start_button = tk.Button(self.mode_frame, text="Démarrer le jeu", command=lambda: self.set_game_mode(mode_var, difficulty_var))
        start_button.pack()

        self.mode_frame.pack()

    def set_game_mode(self, mode_var, difficulty_var):
        self.ia_enabled = mode_var.get() == "1 Joueur"
        self.ia_difficulty = difficulty_var.get() if self.ia_enabled else None
        self.difficulty_menu.config(state="normal" if self.ia_enabled else "disabled")
        self.mode_frame.pack_forget()
        self.reset_game()
        self.draw_grid()

    def draw_grid(self):
        for column in range(3):
            buttons_in_cols = []
            for row in range(3):
                button = tk.Button(self.root, font=("Arial", "50"), width=5, height=3,
                                   command=lambda r=row, c=column: self.place_symbol(r, c))
                button.grid(row=row, column=column)
                buttons_in_cols.append(button)
            self.buttons.append(buttons_in_cols)

    def place_symbol(self, row, column):
        if not self.win and self.buttons[column][row]['text'] == "":
            self.buttons[column][row].config(text=self.current_player)
            if self.check_win(row, column):
                self.print_winner()
            else:
                self.switch_player()

    # Les autres méthodes comme reset_game, check_win, print_winner, etc. viennent ici
    # ...

# Création de l'instance Tkinter
root = tk.Tk()
game = TicTacToeGame(root)
root.mainloop()
