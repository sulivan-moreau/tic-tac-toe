import tkinter as tk
from tkinter import simpledialog

# Dictionnaire pour stocker les informations des utilisateurs
users = {}  # Format: {"username": {"password": "password123", "scores": []}}

# Utilisateur actuellement connecté
current_user = None

def register_user():
    username = simpledialog.askstring("Inscription", "Nom d'utilisateur:")
    if username in users:
        tk.messagebox.showinfo("Erreur", "Ce nom d'utilisateur existe déjà.")
        return

    password = simpledialog.askstring("Inscription", "Mot de passe:", show='*')
    users[username] = {"password": password, "scores": []}
    tk.messagebox.showinfo("Inscription", "Inscription réussie.")

def login_user():
    global current_user
    username = simpledialog.askstring("Connexion", "Nom d'utilisateur:")
    password = simpledialog.askstring("Connexion", "Mot de passe:", show='*')

    if username in users and users[username]["password"] == password:
        current_user = username
        tk.messagebox.showinfo("Connexion", "Connexion réussie.")
    else:
        tk.messagebox.showinfo("Erreur", "Nom d'utilisateur ou mot de passe incorrect.")

def logout_user():
    global current_user
    current_user = None
    tk.messagebox.showinfo("Déconnexion", "Vous êtes maintenant déconnecté.")

def add_score(score):
    if current_user:
        users[current_user]["scores"].append(score)

def show_scores():
    if current_user:
        scores = users[current_user]["scores"]
        score_str = "\n".join(str(score) for score in scores)
        tk.messagebox.showinfo("Scores", f"Scores de {current_user}:\n{score_str}")
    else:
        tk.messagebox.showinfo("Erreur", "Aucun utilisateur connecté.")

def show_user_management():
    window = tk.Toplevel()
    window.title("Gestion des Utilisateurs")

    tk.Button(window, text="Inscription", command=register_user).pack()
    tk.Button(window, text="Connexion", command=login_user).pack()
    tk.Button(window, text="Déconnexion", command=logout_user).pack()
    tk.Button(window, text="Afficher les Scores", command=show_scores).pack()
