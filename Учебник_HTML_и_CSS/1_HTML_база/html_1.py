from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


# def one():
#     return render_template('1.html')

# @app.route("/")
# def page():
#     return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
