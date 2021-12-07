from flask import Flask,render_template
import pymongo

app = Flask(__name__)
app.secret_key = '\xb4\xeb\x9d`\xfb\xb2\xc3L\xb7\x07\xa4\xc12!\xfeA'
#DataBase Config
client = pymongo.MongoClient('localhost',27017)
db = client.Badooms_db

from config import routes

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/make',methods=['POST','GET'])
def make_page():
    return render_template("makebadoom.html")


if __name__ == "__main__":
    app.debug = True
    app.run()