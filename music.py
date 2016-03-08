import asyncio

class MusicClient:
    def __init__(self, client, voice):
        self.client = client
        self.queue = []
        self.voice = voice
        self.playing = False
        self.player = None
        self.loop = asyncio.get_event_loop()

    def add(self, vId):
        self.queue.append(vId)

    async def play(self):
        if self.playing:
            return False
        self.playing = True
        q0 = self.queue[0]
        self.queue.remove(q0)
        self.player = await self.voice.create_ytdl_player('https://www.youtube.com/watch?v={0}'.format(q0), after=self.try_play)
        self.player.start()

    def skip(self):
        self.player.stop()

    def try_play(self):
        self.playing = False
        if not len(self.queue) == 0:
            asyncio.run_coroutine_threadsafe(self.play())
