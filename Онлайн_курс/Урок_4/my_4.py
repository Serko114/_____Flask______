from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = ['Установка',
        'Первое приложение',
        'Обратная связь',]


@app.route("/")
def index():
    print(url_for('index'))  # выдает адрес обработчика
    return render_template('index.html', menu=menu)


@app.route("/about")
def about():
    print(url_for('about'))  # выдает адрес обработчика
    return render_template('about.html', title="О сайте", menu=menu)


@app.route("/profile/<path:username>")
# @app.route("/profile/<path>") можно и так
def profile(username):
    return f"Пользователь: {username}"
# в кавычках можно писать:
# path: это путь
# int: это целое число
# float: это число с плавающей точкой


# выдает адрес обработчика
with app.test_request_context():
    print(url_for('index'))
    print(url_for('about'))
    print(url_for('profile', username="Marcus"))


# if __name__ == "__main__":
#     app.run(debug=True)
