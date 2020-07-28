from BlackJackClasses3 import Deck
from BlackJackClasses3 import Player
from BlackJackClasses3 import Dealer
from BlackJackFunctions import count_ace,print_values,sub_ace,check_win,keep_playing

def show_hands():
    print('*Computer hand: ')
    comp.flip_cards()
    print('\n')
    print('*Player hand: ')
    joshua.flip_cards()
    print('\n')


def full_reveal():
    print('*Computer hand: ')
    comp.reveal()
    print('\n')
    print('*Player hand: ')
    joshua.flip_cards()
    print('\n')


joshua = Player(100)
bet_amount = 0
comp = Dealer()
print('\n'*3)
print("LET'S PLAY SOME BLACKJACK!!!   ")
print('Ready??? ')
print('-----------------------------------------------------\n')
while True:
    new_deck = Deck()
    new_deck.shuffle_up()
    joshua.hand=[]
    comp.hand=[]
    for x in range(2):
        joshua.add_card(new_deck.hit_me())
    for y in range(2):
        comp.add_card(new_deck.hit_me())

    player_hand_value=0
    for created_card in joshua.hand:
        player_hand_value+=created_card.value
    if count_ace(joshua.hand)>=1 and player_hand_value>21:
        player_hand_value=sub_ace(player_hand_value, count_ace(joshua.hand))
    else:
        player_hand_value+=0

    comp_hand_value = 0
    for created_card in comp.hand:
        comp_hand_value += created_card.value
    if count_ace(comp.hand)>=1 and comp_hand_value>21:
        comp_hand_value=sub_ace(comp_hand_value, count_ace(comp.hand))
    else:
        comp_hand_value+=0

    print(f"*Joshua's bank: ${joshua.bank}")
    if joshua.bank<0:
        print('You are too poor to play this game. Get outta here.')
        print('-------:(----------------),:------------------------')
        break
    else:
        while True: ##I want this here so that I'm not RESETTING the game every time I use try/except
            try:
                bet_amount=int(input('How much money would you like to bet? \n$'))
                print('\n')
            except:
                print("Please select a whole dollar amount.")
                print('\n')
                continue
            else:
                print('\n')
                break
        joshua.place_bet(bet_amount)
        print(f"Joshua has placed a bet of ${bet_amount} | ${joshua.bank} left in bank  ")
        print('-----------------------------------------------------\n')
        win_amount=bet_amount*2

    show_hands()
    print('\n')

    if check_win(player_hand_value):
        print('Player wins!')
        full_reveal()
        print_values(comp_hand_value,player_hand_value)
        joshua.bank+=(win_amount)
        print(f"*{win_amount} added to Joshua's bank ")
        print(f'*${joshua.bank} in bank')
        print('-------:)----------------(:------------------------')
        if keep_playing():
            continue
        else:
            break

    print('\n')
    game_on=True
    turn = 'Player'
    while game_on:
        while turn=='Player':
            print(f'Player hand value: {player_hand_value} ')
            print('----------------------------------------------------')
            if check_win(player_hand_value):
                print('Player wins!')
                full_reveal()
                print_values(comp_hand_value, player_hand_value)
                joshua.bank += (win_amount)
                print(f"*{win_amount} added to Joshua's bank ")
                print(f'*Player bank: ${joshua.bank}')
                print('-------:)----------------(:------------------------')
                game_on=False
                break
            elif player_hand_value>21:
                print('BUST')
                print('\n')
                print('Comparing hands: ')
                full_reveal()
                print_values(comp_hand_value, player_hand_value)
                if abs(comp_hand_value+-21)<abs(player_hand_value+-21):
                    print('*Computer has the better hand ')
                    print('-------:(----------------),:------------------------')
                elif abs(comp_hand_value+-21)>abs(player_hand_value+-21):
                    print('*Player has the better hand! ')
                    joshua.bank+=win_amount
                    print(f'*Player bank: ${joshua.bank}')
                    print('-------:)----------------(:------------------------')
                elif abs(comp_hand_value+-21)==abs(player_hand_value+-21):
                    print('TIE')
                    joshua.bank+=bet_amount
                    print(f'*Player bank: ${joshua.bank}')
                    print('------->:|----------------|:<------------------------')
                game_on = False
                break

            else:
                hitting=True
                while hitting:
                    print('\n')
                    hit = input('Hit? ')
                    if hit == 'hit me':
                        player_hand_value=0
                        joshua.add_card(new_deck.hit_me())
                        show_hands()
                        for created_card in joshua.hand:
                            player_hand_value += created_card.value
                        if count_ace(joshua.hand)>=1 and player_hand_value>21:
                            player_hand_value=sub_ace(player_hand_value, count_ace(joshua.hand))
                        elif player_hand_value>21:
                            break
                        elif check_win(player_hand_value):
                            break
                        else:
                            print(f'*Player hand value: {player_hand_value}')
                            print('-----------------------------------------------')
                            player_hand_value+=0
                        continue
                    else:
                        turn='Computer'
                        break

        while turn=='Computer':
            print('\n' * 2)
            comp_hand_value=0
            comp.add_card(new_deck.hit_me())
            print('*Computer hand: ')
            comp.reveal()
            print('\n')
            for created_card in comp.hand:
                comp_hand_value += created_card.value
            if count_ace(comp.hand) >= 1 and comp_hand_value > 21:
                comp_hand_value = sub_ace(comp_hand_value, count_ace(comp.hand))
            else:
                comp_hand_value += 0
            if comp_hand_value<=20:
                continue
            elif check_win(comp_hand_value):
                full_reveal()
                print_values(comp_hand_value, player_hand_value)
                print('Computer hits 21.\nGame Over ')
                print('-------:(----------------),:------------------------')
                game_on=False
                break
            elif comp_hand_value==20==player_hand_value:
                print('TIE')
                full_reveal()
                print_values(comp_hand_value, player_hand_value)
                joshua.bank += bet_amount
                print(f'*Player bank: ${joshua.bank}')
                print('------->:|----------------|:<------------------------')
                game_on=False
                break
            elif comp_hand_value>21:
                print('Computer BUST ')
                if abs(comp_hand_value+-21)<abs(player_hand_value+-21):
                    print('Computer has the better hand ')
                    print('\n')
                    full_reveal()
                    print_values(comp_hand_value,player_hand_value)
                    print('-------:(----------------),:------------------------')
                elif abs(comp_hand_value+-21)>abs(player_hand_value+-21):
                    print('Player has the better hand! ')
                    print('\n')
                    full_reveal()
                    print_values(comp_hand_value, player_hand_value)
                    print('-------:)----------------(:------------------------')
                    joshua.bank+=win_amount
                    print(f'*${joshua.bank} in bank')
                    print('----------------------------------------------------')
                game_on=False
                break


    if joshua.bank<=0:
        print('-------:(----------------),:------------------------')
        print('You are too poor to play this game')
        print(f'*${joshua.bank} in bank')
        print('-------:(----------------),:------------------------')
        break
    if keep_playing():
        print('-----G------R-----E-----E-----D-------Y-------------')
        continue
    else:
        print('----------------------------------------------------')
        print('Game Over, walk away with what you got b ')
        print(f'*${joshua.bank} in bank')
        print('----------------------------------------------------')
        break