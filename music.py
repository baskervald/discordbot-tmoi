import asyncio

class MusicClient:
    def __init__(self, client, voice):
        self.client = client
        self.queue = []
        self.voice = voice
        self.player = None
        self.playing = False
        self.firstPlay = True
        self.loop = asyncio.get_event_loop()

    async def add(self, vId, channel):
        if vId not in self.queue:
            if self.playing and vId in self.player.url:
                await self.client.send_message(channel, "That's playing right now...")
                return False
            self.queue.append(vId)
            await self.client.send_message(channel, "Added")
        else:
            await self.client.send_message(channel, "That's already in the queue.")

    async def play(self):
        if self.playing:
            return False
        self.playing = True
        q0 = self.queue[0]
        self.queue.remove(q0)
        self.player = await self.voice.create_ytdl_player('https://www.youtube.com/watch?v={0}'.format(q0))
        self.player.start()
        while self.player.is_playing():
            await asyncio.sleep(5)
        else:
            self.playing = False
            if len(self.queue) != 0:
                await self.play()

    def skip(self):
        self.player.pause()
        self.player.stop()
