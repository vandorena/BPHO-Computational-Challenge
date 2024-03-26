import sqlite3, uuid
from flask import Flask, request, redirect, render_template, url_for, g , session

def get_db(database_name):
    db = getattr(g,"_database",None)
    if db is None:
        db = g._database = sqlite3.connect(f"{database_name}.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    return db.cursor()

def close_connection(exception):
    db = getattr(g,"_database",None)
    if db is not None:
        db.close()

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