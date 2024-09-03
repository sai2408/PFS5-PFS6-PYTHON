from flask import Flask,render_template,request
from mysql.connector import connect

db_config = {
    'host': 'localhost',
    'database': 'example12345',
    'user': 'root',
    'password': 'root'
}
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register",methods=["POST","GET"])
def register():
    if request.method == "POST":
        name = request.form['name']
        return render_template("display.html",value=name)

@app.route("/getdata")
def getdata():
    try:
        conn = connect(**db_config)
        cursor = conn.cursor()
        q1 = "SELECT * FROM employees"
        cursor.execute(q1,)
        rows = cursor.fetchall()
        conn.commit()
    except Exception as e:
        return e
    else:
        return render_template("showdata.html",x = rows)
if __name__ == "__main__":
    app.run(port=5036)