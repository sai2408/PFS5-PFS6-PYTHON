from flask import Flask,render_template,request
from mysql.connector import connect
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
verifyotp = "0"
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
@app.route("/verify")
def verify():
    return render_template("verifyemail.html")
    
@app.route("/verify1",methods=["POST","GET"])
def verify1():
    otp = random.randint(1111,9999)
    global verifyotp
    verifyotp = str(otp)
    print(verifyotp)
    x = False
    if request.method == "POST":
        email = request.form['email']
        x = True
    if x:
        print("Sending Email")
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        mailusername = "saivardhan.thimmisetty@gmail.com"
        mailpassword = "xqmd vmwz ibqy ijii"
        from_email = "saivardhan.thimmisetty@gmail.com"
        to_email = email
        subject = 'OTP for Login'
        body = f"The OTP for verification is {otp}"

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(mailusername, mailpassword)
        server.send_message(msg)
        server.quit()
        print("email Sent")
        return render_template("enterotp.html")
    else:
        return "Try Again"
@app.route("/enterotp")
def enterotp():
    return render_template("enterotp.html")

@app.route("/verifyotp1",methods=["POST","GET"])
def verifyotp1():
    print("Verification started")
    print(verifyotp)
    print(type(verifyotp))
    x = False
    if request.method == "POST":
        otp = request.form['otp']
        x = True
    if x:
        if otp == verifyotp:
            return render_template("register.html")
        else:
            return "try again"
if __name__ == "__main__":
    app.run(port = 5024)