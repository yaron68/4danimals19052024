from flask import Flask, request

app = Flask(__name__)

last_game_id = 0

pingPong = {}


@app.get('/')
def main_page():
    return "HELLO", 200


#  start the game with 2 players 1 & 2 with score 0
@app.post('/start')
def start_game():
    global last_game_id
    global pingPong
    if last_game_id >= 100:
        return f"Game failed to start  100 games exist", 400
    else:
        last_game_id += 1
        new_game = {'game_id': last_game_id, 1: 0, 2: 0}
        pingPong[last_game_id] = new_game
        return f"Game id {last_game_id} start successfully ", 200


#  get score for player 1 or 2 for game id
@app.post('/score')
def set_score():
    global pingPong
    data = request.json  # takes the body and convert the json to dict
    input_game_id = data['game_id']
    input_player = data['player_id']
    for i, game in enumerate(pingPong.items()):
        if input_game_id == game[1]['game_id']:
            game[1][input_player] += 1
            return f"Score recorded successfully.", 200
    return f"Failed to recorded score required json with game_id and player_id", 400


# output scores for game id for player 1 & 2
@app.get('/score')
def get_score():
    global pingPong
    data = request.json  # takes the body and convert the json to dict
    input_game_id = data['game_id']
    for i, game in enumerate(pingPong.items()):
        if input_game_id == game[1]['game_id']:
            return f"game no {game[1]['game_id']} player1_score { game[1][1]} player2_score {game[1][2]}", 200
    return f"Failed to get game score required json with game_id .", 400


# end game for game id and declare the winner 1 or 2 and delete from pingPong games
@app.post('/end')
def end_game():
    global pingPong
    data = request.json  # takes the body and convert the json to dict
    input_game_id = data['game_id']
    for i, game in enumerate(pingPong.items()):
        if input_game_id == game[1]['game_id']:
            if game[1][1] > game[1][2]:
                del pingPong[input_game_id]
                return f"Game {input_game_id} ended successfully. 1 wins!", 200
            elif game[1][1] < game[1][2]:
                del pingPong[input_game_id]
                return f"Game {input_game_id} ended successfully. 2 wins!", 200
            else:
                del pingPong[input_game_id]
                return f"Game {input_game_id} ended successfully. no winner !", 200
    return f"Game {input_game_id} not exist or required json with game_id", 400


app.run(port=5000, host='0.0.0.0')
