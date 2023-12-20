import random

# IA Facile: Choisit une case vide au hasard
def ia_facile(board, signe):
    choices = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]
    return random.choice(choices) if choices else None

# Fonction auxiliaire pour vérifier les opportunités de gagner ou de bloquer
def check_win(board, signe):
    # Vérifie les conditions de victoire pour le signe donné
    # ...

    return False  # Retourne False si aucune victoire n'est détectée

# IA Moyenne: Bloque les mouvements gagnants de l'adversaire ou tente de gagner
def ia_moyenne(board, signe):
    adversaire = 'O' if signe == 'X' else 'X'

    def check_move(s):
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = s
                    if check_win(board, s):
                        return (i, j)
                    board[i][j] = 0
        return None

    move = check_move(signe)  # Tente de gagner
    if move:
        return move

    move = check_move(adversaire)  # Tente de bloquer
    if move:
        return move

    return ia_facile(board, signe)  # Joue aléatoirement si aucune autre option

# IA Difficile: Implémentation de l'algorithme Minimax (exemple simplifié)
def ia_difficile(board, signe):
    # Implémentation de l'algorithme Minimax simplifié
    # ...

    # Retourne le meilleur coup calculé par Minimax
    # ...
    return ia_moyenne(board, signe)  # Utilise l'IA moyenne en attendant
