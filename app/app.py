from flask import Flask, render_template

# Flaskオブジェクトの作成
app = Flask(__name__)

# 「/」へアクセスがあった場合に、"HelloWorld"の文字を返す
@app.route("/")
def hello():
    return "Hello World"

# 「/index」へアクセスがあった場合に、index.htmlを返す
@app.route("/index")
def index():
    return render_template("index.html")

# おまじない
if __name__ == "__main__":
    app.run(debug=True)
