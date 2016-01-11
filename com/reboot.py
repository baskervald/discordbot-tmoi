import discord

class Reboot:
    def __init__(self, client):
        self.client = client

    async def run(self, params, message):
       member = discord.utils.get(self.client.get_all_members(), id=message.author.id)
       if member != None and discord.utils.get(member.roles, name='moderators') != None:
           await self.client.logout()

commands = {
    'reboot': {
        'visible': False,
        'description': "Reboot the bot",
        'usage': ".reboot",
        'class': Reboot
    }
}
