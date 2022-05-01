#!/usr/bin/env python3

import random


class Player:

    def __init__(self):
        self.score = 0
        self.moves = ['rock', 'paper', 'scissors']
        self.my_move = self.moves
        self.their_move = None

    def move(self):
        return 'rock'

    def get_my_move(self):
        return self.my_move

    def get_their_move(self):
        return self.their_move

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Rock, paper, scissors? ")
            if move.lower() in self.moves:
                return move.lower()


class RandomPlayer(Player):
    def move(self):
        return random.choice(self.moves)


class ReflectPlayer(Player):
    def move(self):
        their_move = self.get_their_move()
        if not their_move:
            return "rock"
        return self.get_their_move()


class CyclePlayer(Player):
    def move(self):
        their_move = self.get_their_move()
        if their_move == "rock":
            return "paper"
        elif their_move == "paper":
            return "scissors"
        else:
            return "rock"


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.humanscore = 0
        self.computerscore = 0

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        if self.beats(move1, move2):
            self.humanscore += 1
            winner = '** You win! **'
        elif move1 == move2:
            self.humanscore = self.humanscore
            self.computerscore = self.computerscore
            winner = '** It\'s a tie! **'
        else:
            self.computerscore += 1
            winner = '** Uh oh! The computer won. Womp womp. **'
        print(f"\nYou played {move1}.\nThe computer played {move2}. "
              f"\n{winner} \n\nScore: \nYou - {self.humanscore}  "
              f"\nBob the Computer - {self.computerscore}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
        if self.humanscore > self.computerscore:
            print("You win! You're smarter than the machines!")
        elif self.humanscore == self.computerscore:
            print("Tie game")
        else:
            print("Bob won. The machines are rising.")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
