from flask import Flask
import requests
from jikanpy import Jikan

app = Flask(__name__)
jikan = Jikan()

# Отримуємо дані аніме
anime_data = jikan.anime(54595, extension='episodes')

@app.route('/')
def home():
    # Вивід даних з requests_test.py
    r = requests.get("https://httpbin.org/get")
    requests_info = f"<p>Запит до httpbin: статус {r.status_code}</p>"

    # Вивід даних з jikanpy/anime.py
    anime_info = "<h3>Епізоди аніме:</h3>"
    for ep in anime_data["data"]:
        anime_info += f"<p>Епізод {ep['mal_id']}: {ep['title']} (оцінка {ep['score']})</p>"

    return requests_info + anime_info

@app.route('/about')
def about():
    return "<p>Це сторінка про веб-сайт створений за допомогою ChatGPT у середовищі Poetry!</p>"

if __name__ == '__main__':
    app.run(debug=True, port=5001)