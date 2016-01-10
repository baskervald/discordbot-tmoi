import discord
from importlib import import_module
from os import environ

from glob import glob
from os.path import dirname, basename, isfile, join

# from pprint import pprint

# Login

client = discord.Client()

# Load all commands from "com" directory

# 'name': {
#   'visible': Bool,
#   'description': String,
#   'example': String,
#   'class': Class (with init(client) and run(params, message) function)
# }

commands = {}

for f in glob('com/*.py'):
    if isfile(f) and basename(f) != '__init__.py':
        mod = import_module('com.{0}'.format(basename(f)[:-3]))
        class_ = mod.Plugin(client)
        dat = class_.data

        commands[dat['name']] = {
            'visible': dat['visible'],
            'description': dat['description'],
            'example': dat['example'],
            'class': class_
        }



# On join

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    # Print out all connected servers and their channels
    print('Servers')
    print('------')
    for server in client.servers:
        print(server.name)
        for channel in server.channels:
            if channel.type == discord.ChannelType.text:
                print('  #{0.name}'.format(channel))
    # print('------')
    # pprint(commands)

@client.event
async def on_message(message):
    starter = message.content[0]
    splitMessage = str.split(message.content)
    command = splitMessage[0][1:]
    params = splitMessage[1:]
    if (starter == '.' or starter == '!') and command in commands:
        ret = await commands[command]['class'].run(params, message)
        if ret != None:
            await client.send_message(message.channel, ret)

client.run(environ['DISCORD_EMAIL'], environ['DISCORD_PASSWORD'])
