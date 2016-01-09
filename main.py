from os import environ
import discord
import commands.moi as moi

client = discord.Client()
client.login(environ['DISCORD_EMAIL'], environ['DISCORD_PASSWORD'])

class helpDialogue:
    def do(params):
        return ['Hi! I\'m baskerbot. My commands are:',
                '```',
                '.moi (!moi):',
                '  Searches moddingofisaac.com',
                '  Usage: .moi <search>\n',
                '.help (!help):',
                '  Display this help dialogue',
                '  Usage: .help',
                '```']

commands = {
    'moi': moi,
    'help': helpDialogue
}

@client.event
def on_message(message):
    split = str.split(message.content)
    command = split[0][1:]
    params = split[1:]
    if (message.content.startswith('.') or message.content.startswith('!')) and command in commands:
        client.send_message(message.channel, '\n'.join(commands[command].do(split[1:])))

@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run()
