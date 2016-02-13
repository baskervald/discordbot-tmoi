from pprint import pprint
from aiohttp import get
import json

class Image:
    def __init__(self, client):
        self.client = client
        self.baseurl = 'http://ajax.googleapis.com/ajax/services/search/images'

    async def run(self, params, message):

        # Make request and load it into beautifulsoup
        query = ' '.join(params)
        async with get(self.baseurl, params=[('v', '0.1'),('start', '0'),('q', query)]) as r:
            if not r.status == 200:
                raise Exception("Response Status = {0}, not 200".format(r.status))
            resp = await r.text()
            jresp = json.loads(resp)
            pprint(jresp)

        # await self.client.send_message(message.channel, url)


commands = {
    'image': {
        'visible': True,
        'description': "Get first google image result",
        'example': ".image <query>",
        'class': Image
    }
}
