from flask import Flask, request
from POC import getting_game_info_from_igdb as poc

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/poc/getgames')
def get_games():
    return poc.get_games_info()


@app.route('/poc/getgenres')
def get_genres():
    return poc.get_genres_info()


@app.route('/poc/getgame')
def get_game_by_name():
    args = request.args
    return poc.get_game_info(args.get("name"))


if __name__ == '__main__':
    app.run()
