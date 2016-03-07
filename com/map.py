from urllib.parse import quote_plus

class Map:
    def __init__(self, client):
        self.client = client

    async def run(self, params, message):
        await self.client.send_message(message.channel, 'http://maps.google.com/maps/api/staticmap?zoom=10&size=400x180&markers=color:blue|{0}'.format(quote_plus(' '.join(params))))

commands = {
        'map':{
            'visible': True,
            'description': "Pulls up a static map for an address or coordinates",
            'example': ".map <address>",
            'class': Map
            }
        }
