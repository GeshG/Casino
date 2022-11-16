import random

class Player:
    def __init__(self, name):
        self.name = name
    
    def player_money(self):
        self.money = 100
        return self.money

class Roulette:
    def __init__(self, balance):
        self.balance = balance

    def place_bet(self, player):
        if player.player_money() > 0:
            print('You can continue betting.')
        else:
            print('You\'ll need to go to the ATM')
        
    def roulette_numbers(self, player):
        bet_money = int(input("How much you would like to bet? "))
        pick_number = int(input('Please, pick a number: '))
        casino_rnd = random.choice([0,1,2,3,4,5,6,7,8,9,10,11,12])
        red = 'red'
        black = 'black'
        while True:
            if pick_number >= 0 and pick_number <= 12:
                if pick_number == 0 and casino_rnd == 0:
                    print(f'The number is {pick_number}')
                    print(f'The casino number is {casino_rnd}')
                    print('You win')
                elif pick_number == 0 and casino_rnd != 0:
                    print(f'The number is {pick_number}')
                    print(f'The casino number is {casino_rnd}')
                    print('You lose')
                else:
                    if pick_number % 2 == 0:
                        print(f'Your number is {pick_number}')
                        print(f'The colour of number {pick_number} is {black}')
                        print(f'The casino number is {casino_rnd}')
                        if casino_rnd % 2 == 0:
                            print(f'The color of the casino number {casino_rnd} is {black}')
                        else:
                            print(f'The color of the casino number {casino_rnd} is {red}')
                        if pick_number == casino_rnd:
                            print('You win')
                            winner = bet_money * 1.5
                            new_amount = winner + player.player_money()
                            print(f'You win ${winner}')
                            print(f'New balance {new_amount}')
                        else:
                            print('You lose')
                            losing_money = player.player_money() - bet_money
                            print(f'New balance {losing_money}')
                    else:
                        print(f'Your number is {pick_number}')
                        print(f'The color of number {pick_number} is {red}')
                        print(f'The casino number is {casino_rnd}')
                        if casino_rnd % 3 == 0:
                            print(f'The color of the casino number {casino_rnd} is {red}')
                        else:
                            print(f'The color of the casino number {casino_rnd} is {black}')
                        if pick_number == casino_rnd:
                            print('You win')
                            winner = bet_money * 1.75
                            new_amount = winner + player.player_money()
                            print(f'You win ${winner}')
                            print(f'New balance {new_amount}')
                        else:
                            print('You lose')
                            losing_money = player.player_money() - bet_money
                            print(f'New balance {losing_money}')
            else:
                    print('Please, enter a number between 0 and 12')
            print('Do you want to continue playing?')
            play_more = input('Yes / No: ')
            if play_more == 'Yes'.lower():
                pick_number = int(input('Please, pick a number: '))
            else:
                print('Thank you for playing! GoodBye!')
                break

class Slots:
    symbols = ['@','#','$']
    def __init__(self) -> None:
        pass
    
    def play_slots(self):
        
        player_money = 100
        player_money_bet = 0
        player_money_new_balance = 0
        print(f'You have, {player_money} dollars.')
        try:
            bet = int(input('Bet amount: '))
        except:
            print('Please, enter a whole number: ')
        while True:
            if player_money <= 0:
                print('Not enough money')
                print('Please, visit the nearest ATM')
                break
            else:
                symbol_one = random.choice(self.symbols)
                symbol_two = random.choice(self.symbols)
                symbol_three = random.choice(self.symbols)
                        
                print('\n|',random.choice(self.symbols), '|', random.choice(self.symbols), '|', random.choice(self.symbols), '|')
                print(13*'-')
                print('|', symbol_one,'|', symbol_two, '|', symbol_three, '|')
                print(13*'-')
                print('|',random.choice(self.symbols), '|', random.choice(self.symbols), '|', random.choice(self.symbols), '|\n')

                if symbol_one == symbol_two and symbol_two == symbol_three:
                    player_money_bet = bet*1.7
                    print(f'You have bet {bet} x 2 = {player_money_bet}')
                    print(f'You won {player_money_bet}')
                    player_money_new_balance = player_money_bet + player_money
                    print(f'Your new balance is {player_money_new_balance}')
                else:
                    print('You lost this time')
                    player_money_new_balance = player_money - player_money_bet
                    print(f'You have lost {player_money_bet}')
                    print(f'Your new balace is {player_money_new_balance}')
                    if player_money_new_balance <=0:
                        print('You have lost. Not enough money to continue.')
                        break
            print('Do you want to continue playing?')
            play_more = input('Yes / No: ')
            if play_more == 'Yes'.lower():
                bet = int(input('Bet amount: '))
            else:
                print('Thank you for playing! GoodBye!')
                break

class Play:
    @classmethod
    def run(cls):

        player = Player('Tommy')
        roulette = Roulette(200)
        slots = Slots()

        active = True
        while active:
            print('\nWELCOME TO CASINO ROYAL')
            instructions = print(""" 
            MAY THE LUCK BE WITH YOU.

            Please, select from the following options to proceed:

            1. Roulette
            2. Slot Machine
            3. Exit the Casino

        """)
            select_game = input('Make your selection: ')
            select_game.isnumeric
            select_game = int(select_game)
            if select_game == 1:
                roulette.roulette_numbers(player)
            elif select_game == 2:
                slots.play_slots()
            elif select_game == 3:
                print('Thank you for playing! GoodBye!')
                break

Play.run()