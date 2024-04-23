from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = '⻉⽠⡅✾≑⵰Ⲍ∺ⓛ⚨≫ⓀⲜⓗ∂ⰼ⭩❎⡫⭏∄ⱏ⿓⧟⒢ℽ▙∑⏠⻨⏤┇⚃▮⍴␹ⷝ⚠╮⺮ⰾ⎔✚Ⓩ⑃⋨⾰⥨ⵕ₵‱ⱖ⍿ⴽ⩤✪┰⭬⿌➆❎⡫⭏∄ⱏ⿓⧟⒢ℽ▙∑⏠⭱⦁┊ⅶ⇽ⵠ⽳⨗⇈♂⃗⻨⏤┇⚃▮⍴␹ⷝ⚠╮⺮ⰾ⎔✚⋑╆│⥜␖❠⍙⟝⟻⻗⾸⭱⦁┊ⅶ⇽ⵠ⽳⨗⇈♂⃗≰◱⯈▣Ⲵ▉⼼'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

