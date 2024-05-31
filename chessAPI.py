import requests
from datetime import date


def get_player_stats(username):
    headers = {
        "User-Agent": "My Python Application. Contact me at cscience404@gmail.com"
    }
    url = f"https://api.chess.com/pub/player/{username}/stats"
    response = requests.get(url, headers=headers)
    data = response.json()
    if 'chess_rapid' not in data or 'chess_blitz' not in data:
        return f"The user name {username} is not valid."
    else:
        blitz = data['chess_blitz']
        rapid = data['chess_rapid']
        return f"All time blitz: {blitz['best']['rating']}\nCurrent blitz: {blitz['last']['rating']}\nAll time rapid: {rapid['best']['rating']}\nCurrent rapid: {rapid['last']['rating']}"

    return response


def get_player_game(username):
    headers = {
        "User-Agent": "My Python Application. Contact me at cscience404@gmail.com"
    }
    year = date.today().year
    month = date.today().strftime("%m")
    url = f"https://api.chess.com/pub/player/{username}/games/{year}/{month}"
    response = requests.get(url, headers=headers).json()
    games = response["games"]
    games.reverse()
    text = []
    for i in range(10):
        white = games[i]['white']
        black = games[i]['black']
        pgn = games[i]['pgn']
        result_start = pgn.find("[Termination") + len("[Termination") + 2
        result_end = pgn.find("]", result_start) - 1
        result = pgn[result_start:result_end]
        text.append(f"{i+1}. white🐻‍❄️: {white['username']}({white['rating']}) vs ({white['rating']}){black['username']} :⬛black\nresult: {result}")
    return text
    # return f"white🐻‍❄️: {white['username']}({white['rating']}) vs ({white['rating']}){black['username']} :⬛black\nresult: {result}"

def get_rating(username):
    headers = {
        "User-Agent": "My Python Application. Contact me at cscience404@gmail.com"
    }
    url = f"https://api.chess.com/pub/player/{username}/stats"
    data = requests.get(url, headers=headers).json()
    rapid = data['chess_rapid']
    return rapid['last']['rating']


def get_leaderboards():
    members = ["hirodinn", "zumawa", "henok2242"]
    rank = {}
    for member in members:
        rating = get_rating(member)
        rank[member] = rating

    sorted_items = sorted(rank.items(), key=lambda x: x[1], reverse=True)

    result = "\n".join([f"{i+1}. {item[0]} | {item[1]}" for i, item in enumerate(sorted_items)])
    return result


if __name__ == '__main__':
    print(get_player_game("zumawa"))
