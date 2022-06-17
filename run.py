import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/detik')
def scraping():
    content = requests.get('https://www.detik.com/terpopuler')
    soup = BeautifulSoup(content.text, 'html.parser')

    last_update = soup.find('div', {'class': 'page__indeks-info font-base-semibold'}).text
    print(f'Daftar berita terpopuler, {last_update}')

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
    return render_template('index.html', last_update=last_update, new_list=new_list)


if __name__ == '__main__':
    app.run(debug=True)
