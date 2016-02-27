import discord
from importlib import import_module
from os import environ
import asyncio

from glob import glob
from os.path import dirname, basename, isfile, join

from idle.main import IdleRPG

# Create client

client = discord.Client()

idle = IdleRPG(client)

# Load all commands from "com" directory

# 'name': {
#   'visible': Bool,
#   'description': String,
#   'example': String,
#   'class': Class (run(params, message))
# }

commands = {}

for f in glob('com/*.py'):
    if isfile(f) and basename(f) != '__init__.py':
        mod = import_module('com.{0}'.format(basename(f)[:-3]))
        modcoms = mod.commands

        for key, value in modcoms.items():
            commands[key] = value
            commands[key]['class'] = commands[key]['class'](client)


# Help is built in, not a plugin
class Help:
    # Not much to do here. We don't need the client
    def __init__(self, client):
        return

    async def run(self, params, message):

        # First two lines of response are always the same
        response = [
            "Hi! I'm baskerbot. My commands are:",
            '```'
        ]

        # Print out all of the commands, their descriptions, and example (but only if visible)
        for command in commands:
            com = commands[command]
            if com['visible']:
                response.append(".{0} (!{0})".format(command))
                response.append("  {0}".format(com['description']))
                response.append("  Example: {0}".format(com['example']))

        # Close the code block
        response.append('```')

        # Wrap it up nice and clean and shoot off the message!
        return '\n'.join(response)

# Add help manually since it isn't loaded normally
commands['help'] = {
    'visible': True,
    'description': "Displays this help dialogue",
    'example': ".help",
    'class': Help(client)
}


# On join print out some useful info
@client.event
async def on_ready():
    print('------------')
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
    print('------')

    # Print out all loaded commands
    print('Loaded commands')
    print('------')
    for command in commands:
        print('.'+command)


# Basic command handler
@client.event
async def on_message(message):

    if message.author == client.user:
        return False

    # Idle RPG
    if message.channel.id == '136654681328975872': # #idle
        await idle.commandHandler(message)
        return

    # Image and file catch
    if len(message.content) == 0:
        return

    starter = message.content[0]
    splitMessage = str.split(message.content)
    command = splitMessage[0][1:]
    params = splitMessage[1:]
    if (starter == '.' or starter == '!') and command in commands:
        ret = await commands[command]['class'].run(params, message)
        if ret != None:
            await client.send_message(message.channel, ret)


# On join
# @client.event
# async def on_member_join(member):
#     await client.send_message(member, "Hey! Welcome to the official /r/themoddingofisaac Discord server. I'm baskerbot, your personal assistant. To see what I do, say `.help`. You can use the commands in any of the server channels too, but I'd personally prefer if just this one time you sent it in this chat.")


# client.run(environ['DISCORD_EMAIL'], environ['DISCORD_PASSWORD'])
loop = asyncio.get_event_loop()

try:
    loop.create_task(idle.run())
    loop.run_until_complete(client.login(environ['DISCORD_EMAIL'], environ['DISCORD_PASSWORD']))
    loop.run_until_complete(client.connect())
except Exception:
    loop.run_until_complete(client.close())
finally:
    loop.close()
