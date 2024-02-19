from utils import SCORES_FILE_NAME, BAD_RETURN_CODE
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def score_server():
    try:
        user_score = open(SCORES_FILE_NAME).readline()
        return render_template("score1.html", score=user_score)
    except:
        return BAD_RETURN_CODE, render_template("scoreError2.html")

if __name__ == "__main__":
    app.run(port=30000)