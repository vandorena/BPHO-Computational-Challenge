from flask import Flask
from flask_simplelogin  import SimpleLogin

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "ⲙ⼬⫎⳽as₥ⱱ⤢⺒◲ⶁ⑥␤⟟⑤⭮⼢↊⇲⌢Ⳃ␈≘⻑↕⾾✼▯◈⩄═⥆◟⒲⸜ⱁ⊷Ⱑ♝⌍⍫≲⊍ⷒↆⶰ⌈┧⅁⨓Ⳅ⫏ⷡⱚⷃⴕ⮬⎂⋯⳩⨠∔⁺⬐ⅵ⣌□⭬␊⦗⪸⼺✏⻨⥋↟⎔⬿ⶆ≌⌘⫣⸁∻⧿⠶②↭⒞ⲯ⻧⡧⤆↳Ⓧ℻ⵀ⪙⑹ⶬ⛝⤼⠯⬫⍌◈ⅶ⧆⌥⠐〉▮∂⾇┼⡹␡⎳⺰➸ⵧ➽⸂⺁ⴵⱽⒸ⨈‾➳⊑⫉℘⤘♚⋠⾌ℼ⟱⸱⒞⢅⊄⽐ⱍ⎎⣳⇺ⷼ⼤⩅⿕s⾑⪗⟚⃜┕⩰⸧⧒⪨⻖⇾Ⱝⱑ☤⡕Ⳬ∛☸sa"

SimpleLogin(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)