from urllib.parse import quote_plus


class Map:
    def __init__(self, client):
        self.client = client

    async def run(self, params, message):
        url = 'http://maps.google.com/maps/api/staticmap?maptype=satellite&zoom=15&size=400x180&markers=color:blue|{0}'.format(quote_plus(' '.join(params)))
        await self.client.send_message(message.channel, url


commands={
        'map': {
            'visible': True,
            'description': "Pulls up a static map for an address or coordinates",
            'example': ".map <address>",
            'class': Map
            }
        }
