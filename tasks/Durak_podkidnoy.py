"""
Самописная игра в подкидного дурака с компьютером на консоли.
"""

from random import choice
from colorama import init
init()
from colorama import Fore, Back, Style

#функция добора карт из колоды
def dobor_kart(to):
    for _ in range(6 - len(to)):
        if len(deck) > 0:
            n = choice(deck)
            to.append(n)
            deck.remove(n)
        else: break

#функция проверки ранга карты
def card_rank(card):
    return vals.index(card[:-1])

#функция ответа компьютера на ход игрока p
def computer_answer(p):
    global turn_set, c
    cmp_no_trump = [card for card in computer if card[-1] != trump]
    cmp_trump = [card for card in computer if card[-1] == trump]
    cmp_no_trump.sort(key=lambda x: card_rank(x))
    cmp_trump.sort(key=lambda x: card_rank(x))
    cmp_answ = []
    for card in computer:
        if card[-1] == p[-1] and card_rank(card) > card_rank(p):
            cmp_answ.append(card)
    if len(cmp_answ) > 0:
        cmp_answ.sort(key=lambda x: card_rank(x))
        c = cmp_answ[0]
        print('Соперник отбился: ', c)
        computer.remove(c)
        turn_set.add(c[:-1])
    else:
        if p[-1] != trump:
            if len(cmp_trump) > 0:
                c = cmp_trump[0]
                print('Соперник отбился козырем: ', c)
                computer.remove(c)
                turn_set.add(c[:-1])
            else:
                print('Сопернику нечем бить! Он взял карту')
                c = 'taken'
        else:
            print('Вы пошли с козырей! Сопернику нечем бить. Он взял карту')
            c = 'taken'
    return c, turn_set

#фнкция раунда, начинающегося с хода игрока
def player_turn():
    global turn_set, c, winner
    player.sort(key=lambda x: card_rank(x))
    print(Back.GREEN, Fore.BLACK, Style.BRIGHT + 'Ваш ход:', Style.RESET_ALL)
    print('Ваши карты: ', Fore.GREEN, *player, Style.RESET_ALL)
    #print('карты компьютера:', *computer)
    p = input()
    while p not in player:
            print('У вас нет такой карты. Попробуйте еще раз:')
            p = input()
    turn_set = {p[:-1]}
    cards_pool = [p]
    player.remove(p)
    computer_answer(p)
    cnt = 1
    while True:
        if len(player) > 0 and len(computer) > 0:
            if c =='taken':
                for _ in range(min(min(len(computer), 6 - cnt), len(player))):
                    print('Подкидывайте по одной или напишите "bito":')
                    while True:
                        p = input()
                        if p.lower() == 'bito':
                            break
                        elif p[:-1] not in turn_set or p not in player:
                            print('Неверный ход. Попробуйте еще раз:')
                        else:
                            break
                    print()
                    if p.lower() != 'bito':
                        cards_pool.append(p)
                        player.remove(p)
                    else:
                        break
                if p.lower() == 'bito':
                    break
            else:
                cards_pool.append(c)
                player.sort(key=lambda x: card_rank(x))
                print('\nВаши карты: ', Fore.GREEN, *player, Style.RESET_ALL)
                #print('карты компьютера:', *computer)
                turn_list = list(turn_set)
                turn_list.sort(key= lambda x: card_rank(x + 'A'))
                print('Вы можете подкинуть:',', '.join(turn_list),'// или напишите "bito".')
                while True:
                    p = input()
                    if p.lower() == 'bito':
                        break
                    elif p[:-1] not in turn_set or p not in player:
                        print('Неверный ход. Попробуйте еще раз:')
                    else:
                        break
                if p.lower() == 'bito':
                    break
                cards_pool.append(p)
                player.remove(p)
                computer_answer(p)
                cnt += 1
                if cnt == 6:
                    print('Для этого раунда достаточно!')
                    break
        else:
            break
    if c == 'taken':
        for card in cards_pool:
            computer.append(card)
        winner = 'player'
    else:
        winner = 'computer'
    if len(deck) > 0 and len(player) < 6: dobor_kart(player)
    if len(deck) > 0 and len(computer) < 6: dobor_kart(computer)
    return winner

# функция раунда, начинающегося с хода компьютера
def computer_turn():
    global turn_set, c, winner
    print(Back.MAGENTA, Fore.BLACK, Style.BRIGHT +'Ход соперника:', Style.RESET_ALL)
    cmp_no_trump = [card for card in computer if card[-1] != trump]
    cmp_trump = [card for card in computer if card[-1] == trump]
    cmp_no_trump.sort(key=lambda x: card_rank(x))
    cmp_trump.sort(key=lambda x: card_rank(x))
    #print('Карты соперника: ', *cmp_no_trump, *cmp_trump)
    if len(cmp_no_trump) > 0:
        c = cmp_no_trump[0]
    else:
        c = cmp_trump[0]
    print(c)
    computer.remove(c)
    cards_pool = [c]
    turn_set = {c[:-1]}
    cnt = 1
    while True:
        player.sort(key=lambda x: card_rank(x))
        #print('Карты соперника: ', *cmp_no_trump, *cmp_trump)
        print('Ваши карты: ', Fore.GREEN, *player, Style.RESET_ALL)
        print('Если бьетесь - бейте, если берете - напишите "beru"')
        while True:
            p = input()
            if p.lower() == 'beru':
                print('Вы взяли!')
                break
            else:
                if p in player and p[-1] == c[-1] and card_rank(p) > card_rank(c) or p[-1] == trump and c[-1] != trump:
                    player.remove(p)
                    turn_set.add(p[:-1])
                    cards_pool.append(p)
                    break
                else:
                    print('Вы не можете так сходить. Попробуйте еще раз:')
        if len(player) > 0 and len(computer) > 0:
            if p.lower() == 'beru':
                if c[-1] != trump and len(deck) > 0:
                    cmp_answ = [card for card in computer if card[:-1] in turn_set and card[-1] != trump]
                    #print('cmp_answ = ', cmp_answ)
                    #print('cards_pool', cards_pool)
                    if len(cmp_answ) > 0:
                        cmp_answ.sort(key=lambda x: card_rank(x))
                        print('\nВам подкинули еще:', end = ' ')
                        n = len(cards_pool)
                        while len(cmp_answ) > 0:
                            if len(cards_pool) == n + 6 - (n + 1) / 2:
                                break
                            print(cmp_answ[0], end=' ')
                            computer.remove(cmp_answ[0])
                            cards_pool.append(cmp_answ[0])
                            cmp_answ = cmp_answ[1:]
                        print()
                        break
                    else:
                        print('Сопернику нечего подкинуть!')
                        break
                elif c[-1] == trump or len(deck) == 0:
                    cmp_answ = [card for card in computer if card[:-1] in turn_set]
                    #print('cmp_answ = ', cmp_answ)
                    #print('cards_pool', cards_pool)
                    if len(cmp_answ) > 0:
                        cmp_answ.sort(key=lambda x: card_rank(x))
                        print('\nВам подкинули еще:', end=' ')
                        n = len(cards_pool)
                        while len(cmp_answ) > 0:
                            if len(cards_pool) == n + 6 - (n + 1) / 2:
                                break
                            print(cmp_answ[0], end=' ')
                            computer.remove(cmp_answ[0])
                            cards_pool.append(cmp_answ[0])
                            cmp_answ = cmp_answ[1:]
                        print()
                        break
                    else:
                        print('Сопернику нечего подкинуть!')
                        break
            else:
                if c[-1] != trump and len(deck) > 0:
                    cmp_answ = [card for card in computer if card[:-1] in turn_set and card[-1] != trump]
                    #print('cmp_answ = ', cmp_answ)
                    #print('cards_pool', cards_pool)
                    if len(cmp_answ) != 0:
                        cmp_answ.sort(key = lambda x: card_rank(x))
                        c = cmp_answ[0]
                        cards_pool.append(c)
                        print('\nВам подкинули еще:', c)
                        cmp_answ.remove(c)
                        computer.remove(c)
                        cnt += 1
                    elif len(cmp_answ) == 0:
                        print('Бито!')
                        break
                    elif cnt == 6:
                        break
                elif c[-1] == trump or len(deck) == 0:
                    cmp_answ = [card for card in computer if card[:-1] in turn_set]
                    #print('cmp_answ = ', cmp_answ)
                    #print('cards_pool', cards_pool)
                    if len(cmp_answ) != 0:
                        cmp_answ.sort(key=lambda x: card_rank(x))
                        c = cmp_answ[0]
                        cards_pool.append(c)
                        print('\nВам подкинули еще:', c)
                        cmp_answ.remove(c)
                        computer.remove(c)
                        cnt += 1
                    elif len(cmp_answ) == 0:
                        print('Бито!')
                        break
                    elif cnt == 6:
                        break
        else:
            break
    if p.lower() == 'beru':
        for card in cards_pool:
            player.append(card)
        winner = 'computer'
    else:
        winner = 'player'
    if len(computer) < 6 and len(deck) > 0: dobor_kart(computer)
    if len(player) < 6 and len(deck) > 0: dobor_kart(player)
    return winner


#глобальные переменные
suits, vals = ['H', 'S', 'C', 'D'], ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [(val + suit) for val in vals for suit in suits]
trump = choice(suits)
c = ''
turn_set = set()
winner = ''
player = []
computer = []

#первая раздача
dobor_kart(player)
dobor_kart(computer)
print('Карты сданы!')
print(Style.BRIGHT, Fore.BLACK, Back.RED + 'Козырь:', trump, Style.RESET_ALL)
print()

#игра
player_turn()
print()
while len(player) and len(computer) > 0:
    if winner == 'player':
        player_turn()
    elif winner == 'computer':
        computer_turn()
    print()

# объявление  победителя
else:
    print('Игра окончена')
    if len(computer) > 0:
        print(Style.BRIGHT, Fore.BLACK, Back.GREEN + choice(['Вы победили!', 'Победа ваша!', 'Ваша взяла!', 'Поздравляю с победой!']))
        print(Style.RESET_ALL + 'Оставшиеся карты: ', *computer)
    elif len(player) > 0:
        print(Style.BRIGHT, Back.MAGENTA, Fore.BLACK + choice(['Вы проиграли!', 'Cегодня не ваш день, сэр!', 'Компьютер вас сегодня сделал!']))
        print(Style.RESET_ALL + 'Оставшиеся карты: ', *player)
    else:
        print(Style.BRIGHT, Back.BLUE, Fore.BLACK + 'Ничья!')











