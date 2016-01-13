import asyncio
import discord

class IdleRPG:
    def __init__(self, client):
        self.client = client
        self.channel = discord.Object(id='136654681328975872') #idle text channel

    async def commandHandler(self, params):
        return

    async def run(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed:
            #run
            return
