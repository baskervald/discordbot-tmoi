import discord

class Avatar:
    def __init__(self, client):
        self.client = client

    async def run(self, params, message):
        # member = discord.utils.get(self.client.get_all_members(), name=message.mentions[0])
        if len(message.mentions) != 0:
            send = '\n'.join([ x.avatar_url for x in message.mentions ])
        else:
            send = discord.utils.get(message.server.members, name=' '.join(params)).avatar_url

        await self.client.send_message(message.channel, send)

commands = {
        'avatar': {
            'visible': True,
            'description': "Gets a user's avatar",
            'example': '.avatar <name or mention>',
            'class': Avatar
            }
        }
