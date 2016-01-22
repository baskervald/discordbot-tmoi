import discord
from io import StringIO
import sys

class Exec:
    def __init__(self, client):
        self.client = client

    async def run(self, params, message):
        cstring = str.split(message.content,'```')[1]

        # Check if it's me
        if not message.author.id == '96016391173332992':
            await self.client.send_message(message.channel, "I can't let you do that, {0}...".format(message.author.name))
            return
        # If you can't find the code that's not good...
        elif not cstring:
            await self.client.send_message(message.channel, "Code not detected")
            return

        # Put 'r all together
        code = compile(cstring, '<string>', 'exec')

        # Redirects stdout so I can get the info from it
        stdout = sys.stdout = StringIO()
        stderr = sys.stderr = StringIO()
        exec(code, {'client':self.client})
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

        await self.client.send_message(message.channel, 'Out:\n```\n{0}```\nErr:\n```\n{1}```'.format(stdout.getvalue(),stderr.getvalue()))
        stdout.close()
        stderr.close()

commands = {
        'exec':{
            'visible': False,
            'description': "Exec code -- USE WITH CARE",
            'usage': '.exec ```code```',
            'class': Exec
            }
        }
