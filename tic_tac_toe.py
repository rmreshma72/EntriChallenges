import random

def board(a1,a2,a3,b1,b2,b3,c1,c2,c3):
    print()
    print(f" {a1} | {a2} | {a3} ")
    print("---+---+---")
    print(f" {b1} | {b2} | {b3} ")
    print("---+---+---")
    print(f" {c1} | {c2} | {c3} ")
    print()

def winner(a1,a2,a3,b1,b2,b3,c1,c2,c3,move):
    if (a1==a2==a3==move) or (b1==b2==b3==move) or (c1==c2==c3==move):
        return True

    if (a1==b1==c1==move) or (a2==b2==c2==move) or (a3==b3==c3==move):
        return True
    
    if(a1==b2==c3==move) or (a3==b2==c1==move):
        return True
     
    else:
        return False
    
#main
print('\n\nWelcome to tic-tactoe game   X - O - X\n')
board(1,2,3,4,5,6,7,8,9)
a1 = a2 = a3 = b1 = b2 = b3 = c1 = c2 = c3 = ' '
moves=[1,2,3,4,5,6,7,8,9]
player=input('Enter your name:').capitalize()
print(f'\n{player}: X  vs   Computer: O')
count = 0

while True:
    try:
        count+= 1
        if(count % 2 ==0):
            ch=random.choice(moves)
            print(f'\nComputer Position 💻: {ch}')
            M='O'
        else:
            ch=int(input(f'\n{player} position 🧑:'))
            M='X'

        if ch in moves:
            if ch == 1 and a1 == ' ':
                a1 = M
            elif ch == 2 and a2 == ' ':
                a2 = M
            elif ch == 3 and a3 == ' ':
                a3 = M
            elif ch == 4 and b1 == ' ':
                b1 = M
            elif ch == 5 and b2 == ' ':
                b2 = M
            elif ch == 6 and b3 == ' ':
                b3 = M
            elif ch == 7 and c1 == ' ':
                c1 = M
            elif ch == 8 and c2 == ' ':
                c2 = M
            elif ch == 9 and c3 == ' ':
                c3 = M
            else:
                print('\nInvalid position ❌..')
                continue
      
        index=moves.index(ch)
        moves.pop(index)
        board(a1,a2,a3,b1,b2,b3,c1,c2,c3)
        win=winner(a1,a2,a3,b1,b2,b3,c1,c2,c3,M)
        if(win):
            if (M=='X'):
                print(f'{player} 🧑 wins....🎉🎉')
            else:
                print('Computer 💻 wins.. 🙁🙁')
            break
            
    except ValueError:
        print('\nInvalid Position ❌.. Try again...\n')
        count-=1
    except IndexError:
        print('Its a tie 😎😎...')





        

