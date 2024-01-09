import random  
from game import *
from ai import AIPlayer
if __name__ == '__main__':
    while(True):
        print()
        print("Who shall you play with?")
        print("1: Human Player")
        print("2: Random Player")
        print("3: for AI player")
        print()
        print("Or just spectate a game?")
        print("4: AI vs AI")
        print("5: Random vs Random")
        print("6: AI vs Random")
        print()
        number = (input('Type a number in: '))
        print()
        number = int(number)
        if number == 1:
            p1 = Player('X')
            p2 = Player('O')
            connect_four(p1,p2)
            break
        elif number == 2:
            p1 = Player('X')
            p2 = RandomPlayer('O')
            connect_four(p1,p2)
            break
        elif number == 3:
            p1 = Player('X')
            p2 = AIPlayer('O','RIGHT',1)
            connect_four(p1,p2)
            break
        elif number == 4:
            p1 = AIPlayer('X','RANDOM',1)
            p2 = AIPlayer('O','RIGHT',1)
            connect_four(p1,p2)
            break
        elif number == 5:
            p1 = RandomPlayer('X')
            p2 = RandomPlayer('O')
            connect_four(p1,p2)
            break
        elif number == 6:
            p1 = AIPlayer('X','RANDOM',1)
            p2 = RandomPlayer('O')
            connect_four(p1,p2)
            break
        else:

            print("Oop! Wrong number typed in! Try again")
            print()
    