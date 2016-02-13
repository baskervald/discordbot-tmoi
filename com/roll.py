from itertools import repeat
from random import randrange

class Roll:
    def __init__(self, client):
        self.client = client

    async def run(self, params, message):

        dice = ''.join(''.join(params).split(' '))

        for char in dice:
            if not char in '0123456789+-d':
                # Fail
                return

        if not dice[0] == '-' or not dice[0] == '+':
            dice = '+' + dice
        positions = [pos for pos, char in enumerate(dice) if char == '-' or char == '+']

        arr = []
        for pos, npos in zip(positions + [None], positions[1:] + [None]):
            die = dice[pos+1:npos or None]
            if die.count('d') > 1:
                # Fail
                return
            if dice[pos] == '+':
                arr.append((True, die))
            if dice[pos] == '-':
                arr.append((False, die))

        value = 0
        equation = ''
        for plus, die in arr:
            add, eq = await self.parseDie(die)
            if plus:
                value += add
                equation += '+ {0} '.format(eq)
            else:
                value -= add
                equation += '- {0} '.format(eq)

        if equation[0] == '+':
            equation = equation[2:]

        await self.client.send_message(message.channel, '{0} = {1}'.format(equation, value))

    async def parseDie(self, die):

        if not 'd' in die:
            value = int(die)
            equation = str(value)
        else:
            mult, rand = die.split('d')

            eq = []
            value = 0
            for _ in repeat(None, int(mult)):
                val = randrange(int(rand))+1
                value += val
                eq.append(str(val))

            equation = '({0})[{1}]'.format(' + '.join(eq), die)

        return (value, equation)

commands = {
        'roll':{
            'visible': True,
            'description': "Rolls dice",
            'example': ".roll <dice>",
            'class': Roll
            }
        }
