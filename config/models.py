from flask import request
from flask.templating import render_template
from werkzeug.utils import redirect
from app import db,app
import string,random

def id_generator(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class Badooms:
    def sign_badoom(self):
        badoom = {
            "badoom_text" : request.form.get('badoom_input_text'),
            "badoom_likes" : 0,
            "badoom_dislikes" : 0,
            "badoom_pvkeycode" : id_generator()
        }
        if len(badoom["badoom_text"])<=20:
            return render_template("makebadoom.html",emptyerror=1)
        else:       
            db.badooms.insert_one(badoom)
            return render_template("index.html",successmsg=1)
            
    def show_badoom(self):
        count = db.badooms.count()
        random_badoom = db.badooms.find()[random.randrange(count)]
        return random_badoom

    def like(self,badoom_keycode):
        current_likes = db.badooms.find_one({"badoom_pvkeycode" : badoom_keycode})
        new_likes = current_likes["badoom_likes"]+1
        db.badooms.update({"badoom_pvkeycode" : badoom_keycode},{ "$set": { "badoom_likes":new_likes } })
        return redirect('/show')
    
    def dislike(self,badoom_keycode):
        current_dislikes = db.badooms.find_one({"badoom_pvkeycode" : badoom_keycode})
        new_dislikes = current_dislikes["badoom_dislikes"]+1
        db.badooms.update({"badoom_pvkeycode" : badoom_keycode},{ "$set": { "badoom_dislikes":new_dislikes } })
        return redirect('/show')
