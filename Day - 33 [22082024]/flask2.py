from flask import Flask
from mysql.connector import connect

app = Flask(__name__)

db_config = {
    'host' : 'localhost',
    'database' : 'sample',
    'user' : 'root',
    'password' : 'root'
}

@app.route("/")
def home():
    return "I am a file used to gather data"

@app.route("/insert/<string:dname>/<string:dgender>/<string:dage>")
def adddata(dname,dgender,dage):
    try:
        con = connect(**db_config)
        cursor = con.cursor()

        q1 = "INSERT INTO DETAILS (DNAME,DGENDER,DAGE) VALUES (%s,%s,%s)"
        cursor.execute(q1,(dname,dgender,dage))
        con.commit()
    except:
        return "Error Occured, Data Not added"
    else:
        return "Data sucessfully Added"

@app.route("/getdata")
def getdata():
    try:
        con = connect(**db_config)
        cursor = con.cursor()

        q1 = "SELECT * FROM DETAILS"
        cursor.execute(q1,)
        x = cursor.fetchall()

        for i in x:
            print(*i,sep="   " )
    except:
        return "Error Occured"
    else:
        return "Look into Python Output Console"
if __name__ == "__main__":
    app.run(port=5002)
