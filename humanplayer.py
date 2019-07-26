class HumanPlayer:
    def __init__(self):
        self.win = 0

    def guess(self):
        geuss_code = int(input('choose 4 uniqe digits (0-9)'))
        geuss_code_list = []
        geuss_code_list.append(geuss_code//1000)
        geuss_code_list.append((geuss_code//100) % 10)
        geuss_code_list.append((geuss_code//10) % 10)
        geuss_code_list.append(geuss_code%10)

        print(geuss_code_list)

        return  geuss_code_list

