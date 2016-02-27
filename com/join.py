import discord

class Join:
    def __init__(self, client):
        self.client = client;

    async def run(self, params, message):
        await self.client.accept_invite(params[0])

commands = {
    'join':{
        'visible': False,
        'description': "Join a server",
        'example': ".join <url>",
        'class': Join
    }
}
