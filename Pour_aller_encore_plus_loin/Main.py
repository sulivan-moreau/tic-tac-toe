import tkinter as tk
import Game
import UserManagement

def show_main_menu():
    menu_window = tk.Tk()
    menu_window.title("Menu Principal")
    menu_window.geometry("400x300")

    welcome_label = tk.Label(menu_window, text="Bienvenue dans Tic Tac Toe!")
    welcome_label.pack()

    one_player_button = tk.Button(menu_window, text="1 Joueur", command=lambda: choose_difficulty(menu_window))
    one_player_button.pack()

    two_player_button = tk.Button(menu_window, text="2 Joueurs", command=Game.start_game_2_players)
    two_player_button.pack()

    manage_accounts_button = tk.Button(menu_window, text="Gérer les Comptes", command=UserManagement.show_user_management)
    manage_accounts_button.pack()

    menu_window.mainloop()

def choose_difficulty(parent_window):
    # Masquer les éléments du menu principal
    for widget in parent_window.winfo_children():
        widget.pack_forget()

    # Ajouter des boutons pour choisir la difficulté
    tk.Button(parent_window, text="Facile", command=lambda: start_game_with_difficulty("Facile", parent_window)).pack()
    tk.Button(parent_window, text="Moyenne", command=lambda: start_game_with_difficulty("Moyenne", parent_window)).pack()
    tk.Button(parent_window, text="Difficile", command=lambda: start_game_with_difficulty("Difficile", parent_window)).pack()

    # Option pour revenir au menu principal
    tk.Button(parent_window, text="Retour", command=lambda: show_main_menu_again(parent_window)).pack()

def start_game_with_difficulty(difficulty, parent_window):
    parent_window.destroy()  # Ferme la fenêtre du menu principal
    Game.start_game_1_player(difficulty)  # Lance le jeu avec la difficulté choisie

def show_main_menu_again(parent_window):
    parent_window.destroy()
    show_main_menu()  # Affiche à nouveau le menu principal

if __name__ == "__main__":
    show_main_menu()
