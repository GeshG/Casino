from random import random


class Casino:
    def __init__(self, available_capacity):
        self.available_capacity = available_capacity

    def capacity(self, players):
        player_count = []
        for player in players:
            if self.available_capacity > len(players):
                player_count.append(player)
        return (f'Curret count of players is {len(player_count)} out of max capacity {self.available_capacity}.')

class Player:
    def __init__(self, name, player_roll, player_balance):
        self.name = name
        self.player_roll = player_roll
        self.player_balance = player_balance

    def welcome(self):
        return (f'Welcome to Casino Royal {self.name}!')

    def player_roll_rnd(self):
        return self.player_roll

    def player_balances(self):
        return (f'Your current balance is {self.player_balance}$.')

class Games:

    casino_balance = 100

    def __init__(self, casino_roll):
        self.casino_roll = casino_roll

    def game_wins(self, player):
        b_change = 0
        if self.casino_roll > player.player_roll_rnd():
            self.casino_balance += 10
            b_change = player.player_balance - 10
        return (f'Casino balance has increased with {self.casino_balance}$. {player.name} balance has decreased with {b_change}$')
        
    def game_loses(self, player):
        game_balance = 50
        if  self.casino_roll < player.player_roll_rnd():
            game_balance -= 10
            player.player_balance +=10
        return (f'Game balance change: {game_balance}. {player.name} balance has changed to {player.player_balance}')
        



 

player1 = Player('Shaun', random(), 100)
player2 = Player('Jim',random(), 200)
print(player1.welcome())
print(player1.player_balances())
game1 = Games(random())
print(game1.game_wins(player1))
print(game1.game_loses(player1)) 
cas = Casino(10)
print(cas.capacity(['John', 'Jane', 'Pete']))




