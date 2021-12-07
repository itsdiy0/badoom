from flask.templating import render_template
from flask import request
from app import app
from .models import Badooms

@app.route('/makebadoom',methods=['POST'])
def makebadoom_page():
    return Badooms().sign_badoom()

@app.route('/show',methods=['POST','GET'])
def showbadoom_page():
    badoom = Badooms().show_badoom()
    if request.form.get('badoom_input_like'):
        pvkeycode = request.form.get('pvkeycode')
        return Badooms().like(pvkeycode)
    if request.form.get('badoom_input_dislike'):
        pvkeycode = request.form.get('pvkeycode')
        return Badooms().dislike(pvkeycode)
    if request.form.get('badoom_input_like')=="" or request.form.get('badoom_input_dislike')=="":
        return render_template("showbadoom.html",error=1)
    bms = badoom['badoom_likes']-badoom['badoom_dislikes']
    return render_template("showbadoom.html",badoom=badoom,bms=bms)

@app.route('/whats')
def whatsbadoom_page():
    return render_template("whatsbadoom.html")
@app.route('/rules')
def rulesbadoom_page():
    return render_template("rulesbadoom.html")





    