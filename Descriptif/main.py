import tkinter as tk


def print_winner():
    global win
    win = True
    print("Le joueur", current_player, "a gagné le jeu")
    reset_game()

def switch_player():
    global current_player
    if not win:
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

def check_win(clicked_row, clicked_col):
    # Vérifier les lignes horizontales
    count = 0
    for i in range(3):
        current_button = buttons[i][clicked_col]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()

    # Vérifier les lignes verticales
    count = 0
    for i in range(3):
        current_button = buttons[clicked_row][i]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()

    # Vérifier les lignes diagonales
    count = 0
    for i in range(3):
        current_button = buttons[i][i]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()

    # Vérifier les lignes diagonales inversées
    count = 0
    for i in range(3):
        current_button = buttons[2 - i][i]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()

    if not win:
        count = 0
        for col in range(3):
            for row in range(3):
                current_button = buttons[col][row]
                if current_button['text'] == 'X' or current_button['text'] == 'O':
                    count += 1
        if count == 9:
            print("Match nul")

def place_symbol(row, column):
    global win
    if not win and buttons[column][row]['text'] == "":
        buttons[column][row].config(text=current_player)
        if check_win(row, column):
            print_winner()
        else:
            switch_player()

def reset_game():
    global win, current_player
    win = False
    current_player = 'X'
    for row in buttons:
        for button in row:
            button.config(text="")


def draw_grid():
    for column in range(3):
        buttons_in_cols = []
        for row in range(3):
            button = tk.Button(
                root, font=("Arial", "50"),
                width=5, height=3,
                command=lambda r=row, c=column: place_symbol(r, c)
            )
            button.grid(row=row, column=column)
            buttons_in_cols.append(button)
        buttons.append(buttons_in_cols)

# Stockage
buttons = []
current_player = 'X'


# Créer la fenêtre
root = tk.Tk()
root.minsize(500, 500)
root.title("TicTacToe")
draw_grid()
root.mainloop()
