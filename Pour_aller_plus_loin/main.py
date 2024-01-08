import tkinter
import ia as ia

def print_winner():
    global win
    if not win:
        win = True
        print("Le joueur", current_player, "a gagné le jeu")

def switch_player():
    global current_player
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
    global current_player, win
    clicked_button = buttons[column][row]
    if clicked_button['text'] == "" and not win:
        clicked_button.config(text=current_player)
        ia.set_move(row, column, ia.HUMAN if current_player == 'X' else ia.COMP)
        check_win(row, column)
        switch_player()

        if current_player == 'O':  # Supposons que 'O' soit l'IA
            ai_move = ia.minimax(ia.board, len(ia.empty_cells(ia.board)), ia.COMP)
            if ai_move[0] != -1:  # Vérifier si l'IA peut jouer
                ai_row, ai_col = ai_move[0], ai_move[1]
                buttons[ai_col][ai_row].config(text=current_player)
                ia.set_move(ai_row, ai_col, ia.COMP)
                check_win(ai_row, ai_col)
                switch_player()

def draw_grid():
    for column in range(3):
        buttons_in_cols = []
        for row in range(3):
            button = tkinter.Button(
                root, font=("Arial", "50"),
                width=5, height=3,
                command=lambda r=row, c=column: place_symbol(r, c)
            )
            button.grid(row=row, column=column)  # Emplacement du bouton dans la grille
            buttons_in_cols.append(button)
        buttons.append(buttons_in_cols)

# Stockage
buttons = []
current_player = 'X'
win = False

# Créer la fenêtre
root = tkinter.Tk()

# Personnalisation de la fenêtre
root.minsize(500, 500)  # TAILLE
root.title("TicTacToe")  # NOM

draw_grid()
root.mainloop()
