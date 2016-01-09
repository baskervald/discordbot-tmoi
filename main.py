from os import environ
import discord
import commands.moi as moi

client = discord.Client()
client.login(environ['DISCORD_EMAIL'], environ['DISCORD_PASSWORD'])

commands = {
    'moi': moi
}

@client.event
def on_message(message):
    split = str.split(message.content)
    command = split[0][1:]
    if (message.content.startswith('.') or message.content.startswith('!')) and command in commands:
        client.send_message(message.channel, '\n'.join(commands[command].do(split[1:])))

@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run()
