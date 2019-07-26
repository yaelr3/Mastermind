from humanplayer import HumanPlayer
from aiplayer import AIPlayer

def play(AIP,HP):
    black = 0
    white = 0
    counter = 0

    code = AIP.choose_code()

    while counter < 20:
        counter = counter + 1

        geuss_code = HP.guess()

        for index, num in enumerate(geuss_code):
            if num in code:
                if code[index] == num:
                    black = black + 1
                else:
                    white = white + 1

        if black == 4:
            print("Conrgrats! you won")
            counter = 20
        else:
            print(f'black: {black}, white: {white}')
        black = 0
        white = 0

AIP = AIPlayer()
HP = HumanPlayer()

play(AIP,HP)

while True:
    a = input('Do you want to play again? press Y, if not press N')
    if a == 'Y':
       play(AIP,HP)
    elif a == 'N':
     break

