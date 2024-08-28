from flask import Flask,render_template,request
from mysql.connector import connect
app = Flask(__name__)
db_config = {
    'host': 'localhost',
    'database': 'reg',
    'user': 'root',
    'password': 'root'
}
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register1",methods=["POST","GET"])
def register1():
    if request.method == "POST":
        fname = request.form['fname']
        lname = request.form['lname']
        username = request.form['username']
        password = request.form['password']
        
        try:
            conn = connect(**db_config)
            cursor = conn.cursor()
            q1 = "INSERT INTO users (username,password) VALUES (%s,%s)"
            cursor.execute(q1,(username,password))
            conn.commit()
        except Exception as e:
            return e
        else:
            return "Data Stored Sucessfully"
    else:
        return "Error Occured"
    
@app.route("/login1",methods=["POST","GET"])
def login1():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        try:
            conn = connect(**db_config)
            cursor = conn.cursor()
            q1 = "SELECT * FROM USERS"
            cursor.execute(q1,)
            x = cursor.fetchall()
            print(x)
            conn.commit()
            length = len(x)
            unames = []
            passwords = []
            for i in x:
                unames.append(i[1])
                passwords.append(i[2])
            if username in unames:
                ind = unames.index(username)
                if password == passwords[ind]:
                    return "Login sucess"
                else:
                    return "Invalid Password"
            else:
                return "Invalid Username"
        except Exception as e:
            return e
    else:
        return "Error Occured"

if __name__ == "__main__":
    app.run(port = 5021)