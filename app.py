from flask import Flask, render_template, url_for, redirect, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "pasukankemeng"

@app.route("/", methods=["POST", "GET"])
def index():
    if "email" in session:
        return redirect(url_for('sukses_req'))
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print("email : ", email)
        print("pass : ", password)
        if email == "admin@gmail.com" and password == "pass":
            session['email'] = email
            session['password'] = password
            return redirect(url_for("sukses_req"))
        else:
            return redirect(url_for("index"))
    return render_template("index.html")

@app.route("/sukses")
def sukses_req():
    nilai = "Anda sukses login..!"
    return render_template("sukses.html", nilai=nilai)

@app.route("/umpeg")
def umpeg():
    if "email" in session:
        return render_template("umpeg.html")
    else:
        return redirect(url_for('index'))

@app.route("/pep")
def pep():
    if "email" in session:
        return render_template("pep.html")
    else:
        return redirect(url_for('index'))

@app.route("/keuangan")
def keuangan():
    if "email" in session:
        return render_template("keuangan.html")
    else:
        return redirect(url_for('index'))

@app.route("/logout")
def logout():
    if "email" in session:
        session.pop("email")
        session.pop("password")
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route("/redirect-umpeg")
def redirect_umpeg():
    return redirect(url_for("umpeg"))

@app.route("/redirect-pep")
def redirect_pep():
    return redirect(url_for("pep"))

@app.route("/redirect-keuangan")
def redirect_keuangan():
    return redirect(url_for("keuangan"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
