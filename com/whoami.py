import discord

class WhoAmI:
    def __init__(self, client):
        self.client = client

    async def run(self, params, message):
        await self.client.send_message(message.channel, message.author.id)

commands = {
    'whoami': {
        'visible': True,
        'description': "Prints your user id",
        'example': ".whoami",
        'class': WhoAmI
    }
}
