import asyncio
import discord
# import cmd

class IdleRPG:
    def __init__(self, client):
        self.client = client
        self.channel = discord.Object(id='136654681328975872') #idle text channel

    async def commandHandler(self, message):
        # await cmd.commands[str.split(message)[0]].run(self.client, self, message)
        return

    async def run(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed:
            # await self.client.send_message(self.channel, 'test')
            await asyncio.sleep(10)
