import discord

class Plugin:

    data = {
        'name': 'say',
        'visible': False,
        'description': "Say something in a channel",
        'example': '.say <channelname> <text>'
    }

    def __init__(self, client):
        self.client = client

    async def run(self, params, message):

        # Get basic info
        channelName = params[0].lstrip('#')
        messageString = ' '.join(params[1:])
        channel = discord.utils.get(self.client.get_all_channels(), name=channelName)

        # Make sure user is a moderator
        member = discord.utils.get(self.client.get_all_members(), id=message.author.id)
        if member != None and discord.utils.get(member.roles, name='moderators') != None:

            # Send message
            await self.client.send_message(channel, messageString)

