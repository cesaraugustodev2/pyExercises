import random
class TicTacToe:
    def __init__(self):
        print("Regras:\n- Os jogadores jogam alternadamente\n- Cada jogador preenche um dos espaços vazios do tabuleiro\n- O jogo termina quando um jogador forma uma linha,\nou quando não houver mais espaços vazios e ninguém ganhar\n- Se não houver vencedor,o jogo empatou, ou deu velha")
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.cpu_player='O'
        self.winner = None  
        self.moves = 0
        self.game_over = False
    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
    def make_move(self, row, col):
        if row < 0 or row > 2 or col < 0 or col > 2:
            print('Jogada inválida')
            print(f"{self.current_player} joga")
            row = int(input(f'Digite a linha '))
            col = int(input('Digite a coluna: '))
            self.make_move(row-1, col-1)
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.moves += 1
            self.current_player, self.cpu_player = self.cpu_player, self.current_player
            print(f"{self.board[row][col]} Jogou" )
    def check_winner(self):
        if self.moves < 5:
            return
        for i in range(3):  # Check rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                self.winner = self.board[i][0]
                self.game_over = True
                return
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                self.winner = self.board[0][i]
                self.game_over = True
                return
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            self.winner = self.board[0][0]
            self.game_over = True
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            self.winner = self.board[0][2]
            self.game_over = True   
            return
        if self.moves == 9:
            self.game_over = True
            return
    def play(self):
        while not self.game_over:
            self.print_board()
            print(f"{self.current_player} joga")
            row = int(input(f'Digite a linha '))
            col = int(input('Digite a coluna: '))
            self.make_move(row-1, col-1)
            self.check_winner()
        self.print_board()
        if self.winner:
            print(f'{self.winner} Ganhou!')
            self.print_board()
        else:
            print('Empate!')
game=TicTacToe()
print("Jogo da Velha")
print("Jogador 1 = X")
print("Jogador 2 = O") 
while True:
 s=input("Pressione Enter para começar")
 if s=='':
  game.play()
