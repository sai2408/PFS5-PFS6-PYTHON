from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register",methods=["POST","GET"])
def register():
    if request.method == "POST":
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        mobile = request.form['mobile']
        print(fname,lname)
        return "Data Captured Sucessfully"
    return render_template("register.html")
@app.route("/about")
def about():
    return render_template("about.html")
if __name__ == "__main__":
    app.run(port=5015)