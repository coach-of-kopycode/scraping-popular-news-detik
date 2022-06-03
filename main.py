import requests
from bs4 import BeautifulSoup


def scraping_data():
    try:
        content = requests.get('https://www.detik.com/terpopuler')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        last_update = soup.find('div', {'class': 'page__indeks-info font-base-semibold'})
        print(f'Daftar berita terpopuler, {last_update.text}')

        titles = soup.findAll(attrs={'class': 'media__title'})
        times = soup.findAll(attrs={'class': 'media__date'})
        print(f'Total berita {len(titles)}\n')

        list_titles = []
        list_times = []
        i = 1
        j = 1

        for title in titles:
            title = title.text.strip()
            list_titles.append(title)
            i = i + 1

        for time in times:
            time = time.text.strip()
            list_times.append(time)
            j = j + 1

        new_list = [list_titles, list_times]
        return new_list
    else:
        return None


def show_data(data):
    if data is None:
        print('Data not found')

    number = 0
    for i in range(0, len(data[0])):
        number = number + 1
        print(f'{number}. {data[0][i]}')
        print(f'{data[1][i]}\n')



if __name__ == '__main__':
    print('Detik.com')
    result = scraping_data()
    show_data(result)
