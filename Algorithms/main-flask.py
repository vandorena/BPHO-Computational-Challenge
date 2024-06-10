from flask import Flask, request, redirect, render_template, url_for, g , session
import sqlite3, uuid
from datetime import datetime as dt
import datetime

app = Flask(__name__)
app.config["SESSION_PERMANENT"] =False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "⤢⺒◲ⶁ⑥␤⟟⑤⭮⼢↊⇲⌢Ⳃ⤢⺒◲ⶁ⤢⺒◲ⶁ⑥␤⟟⑤⭮⼢↊⇲⌢Ⳃ␈≘⻑↕⾾✼▯◈⩄═⥆◟⒲⑥␤⟟⑤⭮⼢↊⇲⌢Ⳃ␈≘⻑↕⾾✼▯◈⩄═⥆◟⒲␈≘⻑↕⾾✼▯◈⤢⺒◲ⶁ⑥␤⟟⑤⭮⼢↊⇲⌢Ⳃ␈≘⻑⑤⭮⼢↊⇲⌢Ⳃ␈≘⻑↕⾾✼▯◈⩄═⥆◟⒲⸜ⱁ⊷Ⱑ♝⌍⍫≲⊍ⷒↆⶰ⌈┧⅁⨓Ⳅ⫏ⷡⱚⷃ⑤⭮⼢↊⇲⌢Ⳃ␈≘⻑↕⾾✼▯◈⩄═⥆◟⒲⸜ⱁ⊷Ⱑ♝⌍⍫≲⊍ⷒↆⶰ⌈┧⅁⨓Ⳅ⫏ⷡⱚⷃⴕ⮬⎂⋯⳩⨠∔⁺⬐ⅵ⣌□⭬␊⦗⪸⼺✏⻨⥋↟⎔⬿ⶆ≌⌘⫣⸁∻⧿⠶②↭ⴕ⮬⎂⋯⳩⨠∔⁺⬐ⅵ⣌□⭬␊⦗⪸⼺✏⻨⥋↟⎔⬿ⶆ≌⌘⫣⸁∻⧿⠶②↭↕⾾✼▯◈⩄═⥆◟⒲⩄═⥆◟⒲"

def get_db():
    db = getattr(g,"_database",None)
    if db is None:
        db = g._database = sqlite3.connect("user_pass_recent_page.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    return db.cursor()

def storepage(route,token):
    cur = get_db()
    current_page = cur.execute(f"UPDATE myuserbase SET page_recent =? WHERE usertoken=?",(route,token))
    return

@app.before_request
def init_db():
    cur = get_db()
    cur.execute("CREATE TABLE IF NOT EXISTS myuserbase(username VARCHAR(1000),password VARCHAR(1000),usertoken VARCHAR(50),page_recent VARCHAR(100))")
    cur.connection.commit()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g,"_database",None)
    if db is not None:
        db.close()



@app.route("/login", methods=["POST", "GET"])
def login():
    if request.form:
        if "enter" in request.form:
            user = request.form['UserName']
            password = request.form['Pass']
            cur = get_db()
            print("checking username")
            user_check = cur.execute(f"SELECT usertoken FROM myuserbase WHERE username=?AND password=?",(user,password)) # I have changed this to make sure that a sql injection doesnt break it.
            cur.connection.commit()
            token_fetch_result = user_check.fetchone()
            if token_fetch_result is None:
                print("gone into token fetch none")
                return redirect( request.host_url + url_for("login"), code = 403)
            else:
                print("it should work??")
                session["usertoken"] = token_fetch_result[0]
                return redirect(url_for("comment"))
        elif "reset_pass" in request.form:
            return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

        elif "new_user" in request.form:
            return redirect(url_for("new_user"))
    return render_template("login.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)