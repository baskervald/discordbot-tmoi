from bs4 import BeautifulSoup
from requests import get

class MoI:
    def __init__(self, client):
        self.client = client
        self.baseurl = 'http://moddingofisaac.com/mod_search.php?search={0}'

    async def run(self, params, message):

        # Make request and load it into beautifulsoup
        query = ' '.join(params)
        bs = BeautifulSoup(get(self.baseurl.format(query)).text, 'lxml')

        # Find all mods listed on page and cut them down to the first three
        mods = bs.find_all('div', class_='item-container')[:3]

        # First 3 lines of results are pretty much always the same
        results = [
            '{0.mention}'.format(message.author),
            '__**Top {0} results for "{1}"**__'.format(len(mods), query),
            '```'
        ]

        # Print title and url for each mod
        if len(mods) != 0:
            for mod in mods:
                results.append(mod.find('div', class_='name').contents[0])  # Title
                results.append('moddingofisaac.com' + mod.a['href'] + '\n') # Url and newline
        else:
            # If there aren't any, let the people know it!
            results.append('No mods found')

        # Wrap up that code block
        results.append('```')

        # And put it all back together into the final message
        return '\n'.join(results)


commands = {
    'moi': {
        'visible': True,
        'description': "Search moddingofisaac.com",
        'example': ".moi <query>",
        'class': MoI
    }
}
