from flask import*
import sqlite3

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("First.html")

@app.route("/reg")
def reg():
    return render_template('Reg.html')

@app.route("/login")
def login():
    return render_template("ask.html")



if __name__=='__main__':
    app.run(debug=True)