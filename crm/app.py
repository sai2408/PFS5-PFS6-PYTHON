from flask import Flask, request, render_template
from mysql.connector import connect, Error
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'database': 'crm',
    'user': 'root',
    'password': 'root'
}

@app.route('/')
def home():
    return render_template('crmhome.html')

@app.route('/admin-login')
def adminlogin():
    return render_template('crmadminlogin.html')
@app.route('/admin-portal')
def adminportal():
    return render_template("crmadminportal.html")
@app.route('/admin-validate',methods=['POST'])
def adminvalidate():
    username = request.form['username']
    password = request.form['password']
    if (username=="admin" and password=="admin"):
        return render_template('crmadminportal.html')
    else:
        return "Invalid Creditionals"


@app.route("/adduser")
def adduser():
    return render_template("crmadduser.html")

@app.route("/add-user",methods=['POST'])
def adduserdb():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    conn = connect(**db_config)
    cursor = conn.cursor()
    q1 = "INSERT INTO users (name,email,password) VALUES (%s,%s,%s)"
    cursor.execute(q1,(name,email,password))
    conn.commit()
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    mailusername = "saivardhan.thimmisetty@gmail.com"
    mailpassword = "xqmd vmwz ibqy ijii"

    from_email = 'saivardhan.thimmisetty@gmail.com'
    to_email = email
    subject = 'CRM - Creditionals - Codegnan'
    body = f"Hello \nWelcome to Codegnan CRM Portal\nHere is Your Creditionals\nEmail: {email}\nPassword : {password}"
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
    server.login(mailusername, mailpassword)  # Login to the email account
    # Send the email
    server.send_message(msg)
    # Disconnect from the server
    server.quit()
    return "User Added Sucessfull"
@app.route('/updateuser')
def updateuser():
    conn = connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    rows = cursor.fetchall()
    return render_template("crmupdateuser.html",users=rows)

@app.route("/user-update",methods=['POST'])
def update_user():
    userid = request.form["xyz"]
    x = userid.split()
    z = x[-1]
    conn = connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    rows = cursor.fetchall()
    return render_template("crmuserupdate.html",x3=rows[0][0],x0 = rows[0][1],x1=rows[0][2],x2=rows[0][3])

@app.route("/user-update-values",methods=['POST'])
def user_update_values():
    userid = request.form['userid']
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    conn = connect(**db_config)
    cursor = conn.cursor()
    q1 = 'UPDATE users SET name=%s,email=%s,password=%s WHERE id=%s'
    cursor.execute(q1,(name,email,password,userid))
    conn.commit()
    return "ok"
@app.route("/delete-user",methods=['POST'])
def delete_user():
    userid = request.form['abc']
    x = userid.split()
    z = x[-1]
    conn = connect(**db_config)
    cursor = conn.cursor()
    try:
        query = "DELETE FROM users WHERE email = (%s)"
        cursor.execute(query,(z,))
        conn.commit()
        query = "SELECT * FROM users"
        cursor.execute(query)
        rows = cursor.fetchall()
        return render_template("crmupdateuser.html",users=rows)
    except:
        return "Try Again"

@app.route("/user-login")
def userlogin():
    return render_template("userloginpage.html")

@app.route("/user-validate",methods=["POST"])
def uservalidate():
    username = request.form['username']
    password = request.form['password']
    try:
        conn = connect(**db_config)
        cursor = conn.cursor()
        q1 = 'SELECT * FROM USERS'
        cursor.execute(q1,)
        rows = cursor.fetchall()
        conn.commit()
    except:
        return "Error Occured"
    else:
        usernames = []
        passwords = []
        for row in rows:
            usernames.append(row[1])
            passwords.append(row[3])
        if username in usernames:
            ind = usernames.index(username)
            if password == passwords[ind]:
                return f"Welcome {username}"
            else:
                return "Invalid Password"
        else:
            return "Invalid User name"


if __name__ == '__main__':
    app.run(debug=True,port=5008)
