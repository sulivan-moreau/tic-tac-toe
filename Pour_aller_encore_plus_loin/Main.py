import tkinter as tk
import Game
import UserManagement

def show_main_menu():
    menu_window = tk.Tk()
    menu_window.title("Menu Principal")

    tk.Label(menu_window, text="Bienvenue dans Tic Tac Toe!").pack()

    # Boutons pour choisir le mode de jeu et gérer les comptes
    tk.Button(menu_window, text="1 Joueur", command=Game.start_game_1_player).pack()
    tk.Button(menu_window, text="2 Joueurs", command=Game.start_game_2_players).pack()
    tk.Button(menu_window, text="Gérer les Comptes", command=UserManagement.show_user_management).pack()

    menu_window.mainloop()

if __name__ == "__main__":
    show_main_menu()
