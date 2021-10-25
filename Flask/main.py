from flask import Flask, request, render_template, jsonify, make_response
from flask_cors import CORS
from connection import DatabaseConn

con = DatabaseConn

app = Flask(__name__)
CORS(app)


@app.route("/api/quest")
def GetAnswer():
    data = request.json
    answer = con.GetQuestionAnsw(" ", data["level"], data["id"])
    return answer[0]["answer"]


@app.route('/api/question', methods=['PATCH'])
def edit_question():
    data = request.json
    con.EditQuestion("", str(data["id"]), str(data["level"]), data["question"], data["answer"], data["fail1"],
                     data["fail2"], data["fail3"])
    return "Success editing question with id " + str(data["id"]) + " "


@app.route('/api/question', methods=['DELETE'])
def delete_question():
    data = request.json
    con.DeleteQuestion('', data["level"], data["id"])
    return "Success deleting question with id " + str(data["id"]) + " from " + str(data["level"]) + " level"


@app.route('/api/player', methods=['DELETE'])
def delete_player():
    data = request.json
    con.DeletePlayer("", data["id"])
    return "Sucsess deleting player with id " + str(data["id"]) + ""


@app.route('/api/player/score', methods=['POST'])
def add_Score():
    data = request.json
    con.AddPoints('', data["id"], data["score"])
    return " " + str(data['score']) + " points added to player " + str(data['id']) + ""


@app.route('/api/adplayer', methods=['POST'])
def add_player():
    data = request.json
    con.AddPlayer('', data["name"], data["link"])
    return "success adding " + data['name'] + " to player list"


@app.route('/api/addQuestion', methods=['POST'])
def add_question():
    data = request.json
    con.AddQuestion('', data["level"], data["question"], data["answer"], data["answer1"], data["answer2"],
                    data["answer3"])
    return "success adding " + data['question'] + " to player list"


@app.route("/api/allplayers")
def GetPlayers():
    return jsonify(con.GetPlayers(''))


@app.route("/api/questions/lvl/<int:lvl>")
def GetQuestionsByLvl(lvl):
    return jsonify(con.GetQuestionsByLvl("",lvl))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
