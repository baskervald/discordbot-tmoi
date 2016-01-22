from random import getrandbits

class Coin:
    def __init__(self, client):
        self.client = client

    async def run(self, params, message):
        await self.client.send_message(message.channel, "Heads" if bool(getrandbits(1)) else "Tails")

commands = {
        'coin':{
            'visible': True,
            'description': "Flips a coin",
            'usage': ".coin",
            'class': Coin
            }
        }
