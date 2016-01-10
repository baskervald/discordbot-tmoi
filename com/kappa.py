import discord

class Kappa:
    def __init__(self, client):
        self.client = client

    async def run(self, params, message):
        await self.client.send_file(message.channel, 'res/kappa.png')


commands = {
    'kappa': {
        'visible': False,
        'description': "kappa",
        'example': ".kappa",
        'class': Kappa
    }
}
