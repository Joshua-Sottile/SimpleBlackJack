def count_ace(somelist):
    count = 0
    for card in somelist:
        if card.rank == 'Ace':
            count += 1
    return count


def print_values(c, p):
    print(f'*Computer hand value: {c}')
    print(f'*Player hand value: {p}')
    print('\n')


def sub_ace(hand_value, ace_func):
    # 1 Ace + hand > 21
    if ace_func == 1:
        return hand_value - 10
    # 2 Aces + hand >21
    elif ace_func == 2:
        return hand_value - 10
    # 3 Aces + hand > 21
    elif ace_func == 3:
        return hand_value - 20
    # 4 Aces + hand >21
    elif ace_func == 4:
        return hand_value - 30
    else:
        pass


def check_win(hand_value):
    if hand_value > 21:
        return False
    elif hand_value < 21:
        return False
    elif hand_value == 21:
        return True


def keep_playing():
    answer = ''
    while answer not in ['y', 'n']:
        answer = input('*Keep playing? (y/n)*\n')
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            continue