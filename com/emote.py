import discord
from glob import glob
from os.path import isfile, basename

class Emote:
    def __init__(self, client):
        self.client = client
        self.loadEmotes()

    def loadEmotes(self):
        self.emotes = []
        for f in glob('emote/*.png'):
            self.emotes.append(basename(f)[:-4])
        self.emotes.sort()

    async def run(self, params, message):
        name = ' '.join(params)
        if name == 'list':
            await self.client.send_message(message.channel, "The available emotes are:\n```\n{0}\n```".format('\n'.join(self.emotes)))
        elif name == 'refresh':
            self.loadEmotes()
            await self.client.send_message(message.channel, "Emotes refreshed")
        elif name in self.emotes:
            await self.client.send_file(message.channel, 'emote/{0}.png'.format(name))


commands = {
    'e': {
        'visible': True,
        'description': "Displays an emote",
        'example': ".e <name> or .e list",
        'class': Emote
    }
}
