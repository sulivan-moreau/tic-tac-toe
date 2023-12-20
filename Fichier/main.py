import tkinter
import ia2  # Assurez-vous que ce module est correctement importé

# Variables globales
buttons = []
current_player = 'X'
win = False
game_mode = "2 Joueurs"
difficulty = "Facile"  # Utilisé seulement en mode 1 Joueur

def set_game_mode(mode):
    global game_mode
    game_mode = mode
    reset_game()

def set_difficulty(level):
    global difficulty
    difficulty = level
    reset_game()

def print_winner(win_line=None):
    global win
    if not win:
        win = True
        print("Le joueur", current_player, "a gagné le jeu")
        if win_line:
            highlight_line(win_line)

def switch_player():
    global current_player
    current_player = 'O' if current_player == 'X' else 'X'

def check_win(clicked_row, clicked_col):
    global win
    winner, win_line = ia2.check_winner(ia2.board)
    if winner:
        print_winner(win_line)

def place_symbol(row, column):
    global current_player, win
    clicked_button = buttons[column][row]
    if clicked_button['text'] == "" and not win:
        clicked_button.config(text=current_player)
        ia2.set_move(row, column, ia2.HUMAN if current_player == 'X' else ia2.COMP)
        check_win(row, column)

        if game_mode == "1 Joueur" and current_player == 'O' and not win:  # IA
            ai_move = ia2.minimax(ia2.board, len(ia2.empty_cells(ia2.board)), ia2.COMP, difficulty)
            if ai_move[0] != -1:
                ai_row, ai_col = ai_move[0], ai_move[1]
                buttons[ai_col][ai_row].config(text=current_player)
                ia2.set_move(ai_row, ai_col, ia2.COMP)
                check_win(ai_row, ai_col)
        
        if game_mode == "2 Joueurs" or not win:
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
            button.grid(row=row, column=column)
            buttons_in_cols.append(button)
        buttons.append(buttons_in_cols)

def highlight_line(win_line):
    for x, y in win_line:
        buttons[y][x].config(bg="green")

def reset_game():
    global win, current_player
    win = False
    current_player = 'X'
    for row in buttons:
        for button in row:
            button.config(text="", bg="SystemButtonFace")

def create_game_menu(root):
    menu = tkinter.Menu(root)
    root.config(menu=menu)

    game_menu = tkinter.Menu(menu)
    menu.add_cascade(label="Jeu", menu=game_menu)
    game_menu.add_command(label="1 Joueur", command=lambda: set_game_mode("1 Joueur"))
    game_menu.add_command(label="2 Joueurs", command=lambda: set_game_mode("2 Joueurs"))

    difficulty_menu = tkinter.Menu(menu)
    menu.add_cascade(label="Difficulté", menu=difficulty_menu)
    difficulty_menu.add_command(label="Facile", command=lambda: set_difficulty("Facile"))
    difficulty_menu.add_command(label="Moyen", command=lambda: set_difficulty("Moyen"))
    difficulty_menu.add_command(label="Difficile", command=lambda: set_difficulty("Difficile"))

# Initialisation de l'interface
root = tkinter.Tk()
root.minsize(500, 500)
root.title("TicTacToe")

create_game_menu(root)
draw_grid()
root.mainloop()
