import discord

class WhoAmI:
    def __init__(self, client):
        self.client = client

    async def run(self, params, message):
        await self.client.send_message(message.channel, message.author.id)


class ChannelID:
    def __init__(self, client):
        self.client = client

    async def run(self, params, message):
        await self.client.send_message(message.channel, message.channel.id)

commands = {
    'whoami': {
        'visible': True,
        'description': "Prints your user id",
        'example': ".whoami",
        'class': WhoAmI
    },
    'cid': {
        'visible': False,
        'description': "Prints the channel id",
        'example': ".cid",
        'class': ChannelID
    }
}
