from bs4 import BeautifulSoup
from requests import get

class Plugin:

    data = {
        'name': 'moi',
        'visible': True,
        'description': "Search moddingofisaac.com",
        'example': ".moi <query>"
    }

    def __init__(self, client):
        self.client = client
        self.baseurl = 'http://moddingofisaac.com/mod_search.php?search={0}'

    async def run(self, params, message):
        query = ' '.join(params)
        bs = BeautifulSoup(get(self.baseurl.format(query)).text, 'lxml')

        mods = bs.find_all('div', class_='item-container')[:3]

        results = [
            '{0.mention}'.format(message.author),
            '__**Top {0} results for "{1}"**__'.format(len(mods), query),
            '```'
        ]

        if len(mods) != 0:
            for mod in mods:
                results.append(mod.find('div', class_='name').contents[0])  # Title
                results.append('moddingofisaac.com' + mod.a['href'] + '\n') # Url and newline
        else:
            results.append('No mods found')

        results.append('```')

        return '\n'.join(results)
