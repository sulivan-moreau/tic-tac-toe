import tkinter as tk
import random

class TicTacToeGame:
    def __init__(self, root, mode="2 Joueurs"):
        self.root = root
        self.game_mode = mode
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.create_game_board()

    def create_game_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text='', font=('normal', 40), height=2, width=5,
                                   command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row, column=col)
                self.board[row][col] = button

    def on_click(self, row, col):
        if self.board[row][col]['text'] or self.check_winner():
            return

        self.board[row][col]['text'] = self.current_player

        if self.check_winner():
            tk.messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
            self.reset_game()
        elif self.check_draw():
            tk.messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            self.reset_game()
        else:
            self.switch_player()

            if self.game_mode == "1 Joueur" and self.current_player == 'O':
                self.computer_move()

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def computer_move(self):
        empty_cells = [(r, c) for r in range(3) for c in range(3) if self.board[r][c]['text'] == '']
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.on_click(row, col)

    def check_winner(self):
        for row in range(3):
            if self.board[row][0]['text'] == self.board[row][1]['text'] == self.board[row][2]['text'] != '':
                return True

        for col in range(3):
            if self.board[0][col]['text'] == self.board[1][col]['text'] == self.board[2][col]['text'] != '':
                return True

        if self.board[0][0]['text'] == self.board[1][1]['text'] == self.board[2][2]['text'] != '':
            return True

        if self.board[0][2]['text'] == self.board[1][1]['text'] == self.board[2][0]['text'] != '':
            return True

        return False

    def check_draw(self):
        return all(self.board[row][col]['text'] for row in range(3) for col in range(3))

    def reset_game(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col]['text'] = ''

        self.current_player = 'X'

def start_game_1_player():
    root = tk.Tk()
    root.title("Tic Tac Toe - 1 Joueur")
    game = TicTacToeGame(root, "1 Joueur")
    root.mainloop()

def start_game_2_players():
    root = tk.Tk()
    root.title("Tic Tac Toe - 2 Joueurs")
    game = TicTacToeGame(root, "2 Joueurs")
    root.mainloop()
