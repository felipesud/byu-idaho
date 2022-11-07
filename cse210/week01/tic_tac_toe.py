from time import sleep
from random import randint
import sys


def main():

    pts_player = 0
    pts_cpu = 0

    while True:
        j = ''
        first = ''
        p1 = ''
        p2 = '' 
        p3 = ''
        p4 = ''
        p5 = ''
        p6 = ''
        p7 = ''
        p8 = ''
        p9 = ''
        blank = 'blank'
        pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9 = blank, blank, blank, blank, blank, blank, blank, blank, blank
        play = 0
        play_adv = 0
        random_play = 0
        shifts = 1
        winner = ''
        starting_board = ''' 
        
    --- HOW TO PLAY ---
    When it's your turn, the number corresponds to the position on the board to make your move.
    For example, you want to play center, so you type 5.

        |     |     
    1  |  2  |  3  
    _____|_____|_____
        |     |     
    4  |  5  |  6  
    _____|_____|_____
        |     |     
    7  |  8  |  9  
        |     |  
        
        
        
        '''

        print(starting_board)
        print('Do you want to be the X  or the O?', end=' ')
        while j != 'O' and j != 'X':
            j = str(input('Type X or O and press Enter to continue: ')).strip().upper()
            if j != 'O' and j != 'X':
                print('\nInvalid choice, try again!\n')

        if j == 'O':
            adv = 'X'
            print('\nCool. So I go with the X. ')
        elif j == 'X':
            adv = 'O'
            print('\n Cool. So I go with the O. ')
        print('\nWho plays first?', end='')

        while first != 'ME' and first != 'CPU':
            instr = 'Type ME and press Enter to get you started, or type CPU and press Enter to get me started: '
            first = str(input(instr)).strip().upper()
            if first != 'ME' and first != 'CPU':
                print('\nInvalid choice, try again!\n')
        
        if first == 'ME':
            print('\nSo you play first.\n')
        elif first == 'CPU':
            print('\nSo I play first\n')
        
        def update_board():
            global p1, p2, p3, p4, p5, p6, p7, p8, p9
            board =  '''
         |     |   
  {}  |  {}  |  {}
_____|_____|_____
     |     |
  {}  |  {}  |  {}
_____|_____|_____
     |     |
  {}  |  {}  |  {}
     |     |
            '''.format(p1, p2, p3, p4, p5, p6, p7, p8, p9)
            print(board)
        
        def play_j1():
            global move 

            while True:
                try:
                    move = int(input('Type your move position (1 to 9) and press Enter: '))
                    break
                except ValueError:
                    print('\nInvalid value entered. Enter an integer from 1 to 9!\n')
        
        def routine_j1():
            global move
            global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

            msg_occupied = '\nThis space is already occupied!\n'

            play_j1()

            while move not in range(1, (9 + 1)):
                play_j1()

                if move not in range (1, (9 + 1)):
                    print('\nIvalid Number\n')
            while move == 1 and pos1 == 'occupied' or \
                move == 2 and pos2 == 'occupied' or \
                move == 3 and pos3 == 'occupied' or \
                move == 4 and pos4 == 'occupied' or \
                move == 5 and pos5 == 'occupied' or \
                move == 6 and pos6 == 'occupied' or \
                move == 7 and pos7 == 'occupied' or \
                move == 8 and pos8 == 'occupied' or \
                move == 9 and pos9 == 'occupied': 
                print(msg_occupied)
                routine_j1()
        
        def update_plays_j1():
            global move
            global p1, p2, p3, p4, p5, p6, p7, p8, p9
            global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

            if move == 1:
                p1 = j
                pos1 = 'occupied'
            elif move == 2:
                p2 = j
                pos2 = 'occupied'    
            elif move == 3:
                p3 = j
                pos3 = 'occupied'   
            elif move == 4:
                p4 = j
                pos4 = 'occupied'  
            elif move == 5:
                p5 = j
                pos5 = 'occupied'
            elif move == 6:
                p6 = j
                pos6 = 'occupied'            
            elif move == 7:
                p7 = j
                pos7 = 'occupied'            
            elif move == 8:
                        p8 = j
                        pos8 = 'occupied'            
            elif move == 9:
                        p9 = j
                        pos9 = 'occupied'  

        def update_plays_j2():
            global move, random_play, adv
            global p1, p2, p3, p4, p5, p6, p7, p8, p9
            global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

            print('\n Let me think about my move...\n') 
            sleep(1.5)
            random_play = randint(1,9)

            while random_play == 1 and pos1 == 'occupied' or \
                random_play == 2 and pos2 == 'occupied' or \
                random_play == 3 and pos3 == 'occupied' or \
                random_play == 4 and pos4 == 'occupied' or \
                random_play == 5 and pos5 == 'occupied' or \
                random_play == 6 and pos6 == 'occupied' or \
                random_play == 7 and pos7 == 'occupied' or \
                random_play == 8 and pos8 == 'occupied' or \
                random_play == 9 and pos9 == 'occupied': 
                random_play = randint(1, 9)
            print('\nI play in the position {}!'.format(random_play))

            if random_play == 1:
                p1 = adv
                pos1 = 'occupied'
            elif random_play == 2:
                p2 = adv
                pos2 = 'occupied'    
            elif random_play == 3:
                p3 = adv
                pos3 = 'occupied'   
            elif random_play == 4:
                p4 = adv
                pos4 = 'occupied'  
            elif random_play == 5:
                p5 = adv
                pos5 = 'occupied'
            elif random_play == 6:
                p6 = adv
                pos6 = 'occupied'            
            elif random_play == 7:
                p7 = adv
                pos7 = 'occupied'            
            elif random_play == 8:
                        p8 = adv
                        pos8 = 'occupied'            
            elif random_play == 9:
                        p9 = adv
                        pos9 = 'occupied'
        
        def check_winner():
            global j, adv, shifts, winner, pts_player, pts_cpu
            global p1, p2, p3, p4, p5, p6, p7, p8, p9

            if p1 == j and p2 == j and p3 == j or \
            p1 == j and p4 == j and p7 == j or \
            p1 == j and p5 == j and p9 == j or \
            p2 == j and p5 == j and p8 == j or \
            p3 == j and p5 == j and p7 == j or \
            p3 == j and p6 == j and p9 == j or \
            p4 == j and p5 == j and p6 == j or \
            p7 == j and p8 == j and p9 == j:
                print('CONGRATULATIONS, YOU WON!!!!\n')
                pts_player += 1
                winner = 'ME'
                shifts = 10
            
            if p1 == adv and p2 == adv and p3 == adv or \
            p1 == adv and p4 == adv and p7 == adv or \
            p1 == adv and p5 == adv and p9 == adv or \
            p2 == adv and p5 == adv and p8 == adv or \
            p3 == adv and p5 == adv and p7 == adv or \
            p3 == adv and p6 == adv and p9 == adv or \
            p4 == adv and p5 == adv and p6 == adv or \
            p7 == adv and p8 == adv and p9 == adv:
                print('I WON!\n')
                pts_cpu += 1
                winner = 'CPU'
                shifts = 10
        
        def update_all():
            global move
            global shifts
            global winner

            if first == 'ME':
                routine_j1()
                update_plays_j1()
                update_board()
                check_winner()

                if shifts == 5:
                    print('DRAW!\n')
                    shifts = 10
                    winner = 'DRAW'

                if winner == '':
                    update_plays_j2()
                    update_board()
                    check_winner()
            elif first == 'CPU':
                update_plays_j2()
                update_board()
                check_winner()

                if shifts == 5:
                    print('DRAW!\n')
                    shifts = 10
                    winner = 'DRAW'
                
                if winner == '':
                    routine_j1()
                    update_plays_j1()
                    update_board()
                    check_winner()
            move = 0
            shifts += 1

        while shifts <= 5:
            update_all()
        
        print('-------- SCOREBOARD --------')
        print('You: {} | Computer: {}'.format(pts_player, pts_cpu))
        print('------------------------')
        
        while True:
            restart = input('\nWant to play again? Enter Y for yes or N for no: ').lower()

            if restart in ('y', 'n', '"y"', '"n"'):
                break
            print('\nInvalid answer!')

        if restart == 'y' or restart == '"y"':
            print('\n-----------------------------------------------------')
            continue
        else:
            print('\nGood game. Thanks for playing!\n')
            sys.exit(0)

main()







