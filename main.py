import bs4
import requests


def scraping_data():
    try:
        content = requests.get('https://www.detik.com/terpopuler')
    except Exception:
        return None

    if content.status_code == 200:
        soup = bs4.BeautifulSoup(content.text, 'html.parser')
        last_update = soup.find('div', {'class': 'page__indeks-info font-base-semibold'})
        print(f'Daftar berita terpopuler, {last_update.text}\n')

        titles = soup.findAll(attrs={'class': 'media__title'})
        return titles
    else:
        return None


def show_data(data):
    if data is None:
        print('Data not found')

    print(f'Total berita {len(data)}')

    i = 1
    for value in data:
        print(f'{i}. {value.text.strip()}')
        i = i + 1


if __name__ == '__main__':
    print('Detik.com')
    result = scraping_data()
    show_data(result)
