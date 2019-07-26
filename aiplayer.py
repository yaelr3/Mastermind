import random

class AIPlayer:

    def choose_code(self):

        code = set()
        while len(code) < 4:
            code.add(random.randint(0,9))
        print('AI player picked a code')

        code_list = []
        for num in code:
            code_list.append(num)

        return  code_list



