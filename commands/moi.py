from bs4 import BeautifulSoup
from requests import get

def do(params):
    search = ' '.join(params)
    results = ['__**First 3 results for "' + search + '":**__', '```']
    soup = BeautifulSoup(get('http://moddingofisaac.com/mod_search.php?search=' + search).text, 'lxml')

    mods = soup.find_all('div', class_='item-container')

    if len(mods) == 0:
        results.append('No results\n```')
        return results

    for mod in mods[:3]:
        results.append(mod.find('div', class_='name').contents[0])
        # results.append(mod.find('div', class_='desc').get_text())
        results.append('moddingofisaac.com' + mod.a['href'] + '\n')

    results.append('```')

    return results

if __name__ == '__main__':
    from sys import argv
    for line in do(' '.join(argv[1:])):
        print(line)
