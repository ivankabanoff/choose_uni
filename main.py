from flask import Flask
from data import db_session

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Скоро здесь будет сайт для выбора вуза"


if __name__ == '__main__':
    # db_session.global_init("db/uni_db.db")
    app.run(port=8080, host='127.0.0.1')