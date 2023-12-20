import tkinter as tk
import random

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
            if ia_enabled:
                play_ai_move()
        else:
            current_player = 'X'

def play_ai_move():
    row, col = None, None
    if ia_difficulty == "Facile":
        move = ia_facile()
    elif ia_difficulty == "Moyen":
        move = ia_moyenne()
    elif ia_difficulty == "Difficile":
        move = ia_difficile()
    
    if move is not None:
        row, col = move
        place_symbol(row, col)

def ia_facile():
    choices = [(i, j) for i in range(3) for j in range(3) if buttons[i][j]['text'] == ""]
    if choices:
        return random.choice(choices)
    return None  # Retourne None si aucune case n'est disponible

def ia_moyenne():
    # Premièrement, vérifier si l'IA peut gagner
    for i in range(3):
        for j in range(3):
            if buttons[i][j]['text'] == "":
                buttons[i][j].config(text=current_player)
                if check_win(i, j):
                    buttons[i][j].config(text="")
                    return i, j
                buttons[i][j].config(text="")

    # Ensuite, vérifier si l'adversaire peut gagner et bloquer
    adversaire = 'X' if current_player == 'O' else 'O'
    for i in range(3):
        for j in range(3):
            if buttons[i][j]['text'] == "":
                buttons[i][j].config(text=adversaire)
                if check_win(i, j):
                    buttons[i][j].config(text="")
                    return i, j
                buttons[i][j].config(text="")

    # Sinon, jouer un coup aléatoire
    return ia_facile()


def ia_difficile():
    # Pour l'instant, l'IA difficile se comportera comme l'IA facile
    return ia_facile()

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

def set_game_mode():
    global ia_enabled, ia_difficulty
    ia_enabled = mode_var.get() == "1 Joueur"
    ia_difficulty = difficulty_var.get() if ia_enabled else None
    difficulty_menu.config(state="normal" if ia_enabled else "disabled")
    mode_frame.pack_forget()
    reset_game()
    draw_grid()

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
win = False
ia_enabled = False
ia_difficulty = None

# Créer la fenêtre
root = tk.Tk()
root.minsize(500, 500)
root.title("TicTacToe")

# Options pour sélectionner le mode de jeu
mode_frame = tk.Frame(root)
mode_var = tk.StringVar(value="2 Joueurs")
difficulty_var = tk.StringVar(value="Facile")

tk.Radiobutton(mode_frame, text="1 Joueur", variable=mode_var, value="1 Joueur", command=lambda: difficulty_menu.config(state="normal")).pack()
tk.Radiobutton(mode_frame, text="2 Joueurs", variable=mode_var, value="2 Joueurs", command=lambda: difficulty_menu.config(state="disabled")).pack()

difficulty_menu = tk.OptionMenu(mode_frame, difficulty_var, "Facile", "Moyen", "Difficile")
difficulty_menu.pack()

start_button = tk.Button(mode_frame, text="Démarrer le jeu", command=set_game_mode)
start_button.pack()

mode_frame.pack()
root.mainloop()
