from flask import Flask, request, jsonify
import steam
import db

app = Flask(__name__)
@app.route('/register', methods=['POST'])
def register():
    try:
        user = db.User(name=request.json['name'], password=request.json['password'], email=request.json['email'], steam_id=request.json['steam_id'])
        db.session.add(user)
        db.session.commit()
    except KeyError, e:
        return jsonify({"Missing": str(e)}), 400
    return jsonify(request.json['name'])
@app.route("/games", methods=['GET'])
def games():
    games = []
    for user in db.session.query(db.User).all():
        for game in user.games:
            games.append(game.name)
    return jsonify(games)
@app.route("/refresh", methods=['POST'])
def refresh():
    games = []
    for user in db.session.query(db.User).all():
        steam_object = steam.Steam_Engine(user.steam_id)
        steam_object.get()
        for game in steam_object.wishlist:
            games.append(db.Game(name=game['name'], price=db.Price(price=game['price'], discount=game['discount'])))
        user.games = games
        db.session.add(user)
        db.session.commit()
        return ""

if __name__ == "__main__":
    app.run()
