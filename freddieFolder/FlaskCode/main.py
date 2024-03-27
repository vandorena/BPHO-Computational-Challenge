from flask import Flask, request, redirect, render_template, url_for, g , session
import sqlite3, uuid, login_request_handler
from datetime import datetime as dt



app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "ⲙ⼬⫎⳽as₥ⱱ⤢⺒◲ⶁ⑥␤⟟⑤⭮⼢↊⇲⌢⾑⪗⟚⃜┕⩰⸧⧒⪨⻖⇾Ⱝⱑ☤⡕Ⳬ∛☸⻑↕⾾✼▯◈⩄═⥆◟⒲⸜ⱁ⊷Ⱑ♝⌍⍫≲⊍ⷒↆⶰ⌈┧⅁⨓Ⳅ⫏ⷡⱚⷃⴕ⮬⎂⋯⳩⨠∔⁺⬐ⅵ⣌□⭬␊⦗⪸⼺✏⻨⥋↟⎔⬿ⶆ≌⌘⫣⸁∻⧿⠶②↭⒞ⲯ⻧⡧⤆↳Ⓧ℻ⵀ⪙⑹ⶬ⛝⤼⠯⬫⍌◈ⅶ⧆⌥⠐〉▮∂⾇┼⡹␡⎳⺰➸ⵧ➽⸂⺁ⴵⱽⒸ⨈‾➳⊑⫉℘⤘♚⋠⾌ℼ⟱⸱⒞⢅⊄⽐ⱍ⎎⣳⇺ⷼ⼤⩅⿕ssa"

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g,"_database",None)
    if db is not None:
        db.close()

@app.route("/login", methods=["POST","GET"])
