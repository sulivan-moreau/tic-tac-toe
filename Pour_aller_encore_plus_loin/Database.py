import sqlite3

# Chemin vers le fichier de base de données SQLite
DATABASE_PATH = "tic_tac_toe.db"

def create_connection():
    """ Crée une connexion à la base de données SQLite. """
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_PATH)
    except sqlite3.Error as e:
        print(e)
    return conn

def setup_database():
    """ Crée les tables nécessaires dans la base de données. """
    conn = create_connection()
    if conn is not None:
        create_user_table(conn)
        conn.close()
    else:
        print("Erreur ! Impossible de créer la connexion à la base de données.")

def create_user_table(conn):
    """ Crée la table des utilisateurs si elle n'existe pas déjà. """
    try:
        sql = '''CREATE TABLE IF NOT EXISTS users (
                     id INTEGER PRIMARY KEY,
                     username TEXT NOT NULL,
                     password TEXT NOT NULL,
                     scores TEXT
                 );'''
        conn.execute(sql)
    except sqlite3.Error as e:
        print(e)

def add_user(username, password):
    """ Ajoute un nouvel utilisateur à la base de données. """
    conn = create_connection()
    if conn is not None:
        try:
            sql = '''INSERT INTO users(username, password) VALUES(?, ?)'''
            conn.execute(sql, (username, password))
            conn.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()

def get_user(username):
    """ Récupère un utilisateur par son nom. """
    conn = create_connection()
    user = None
    if conn is not None:
        try:
            sql = '''SELECT id, username, password FROM users WHERE username = ?'''
            cur = conn.cursor()
            cur.execute(sql, (username,))
            user = cur.fetchone()
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()
    return user

def add_score(user_id, score):
    """ Ajoute un score pour un utilisateur donné. """
    conn = create_connection()
    if conn is not None:
        try:
            sql = '''UPDATE users SET scores = scores || ? || ',' WHERE id = ?'''
            conn.execute(sql, (score, user_id))
            conn.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()

def get_scores(user_id):
    """ Récupère les scores d'un utilisateur. """
    conn = create_connection()
    scores = None
    if conn is not None:
        try:
            sql = '''SELECT scores FROM users WHERE id = ?'''
            cur = conn.cursor()
            cur.execute(sql, (user_id,))
            scores = cur.fetchone()[0]
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()
    return scores

# Créer la base de données et les tables lors du premier lancement
setup_database()
