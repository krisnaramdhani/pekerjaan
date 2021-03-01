from flask import Flask, render_template, url_for, redirect, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "pasukankemeng"

@app.route("/", methods=["POST", "GET"])
def index():
    if "user" in session:
        return redirect(url_for('sukses_req'))
    if request.method == 'POST':
        email = request.form['text']
        password = request.form['password']
        print("user : ", email)
        print("pass : ", password)
        if email == "bappelitbangda" and password == "bappelitbangda":
            session['user'] = email
            session['password'] = password
            return redirect(url_for("sukses_req"))
        else:
            return redirect(url_for("index"))
    return render_template("index.html")

@app.route("/home")
def sukses_req():
    if "user" in session:
        return render_template("home.html")
    else:
        return redirect(url_for('index'))

@app.route("/sekretariat")
def sekretariat():
    if "user" in session:
        return render_template("sekretariat.html")
    else:
        return redirect(url_for('index'))

@app.route("/umpeg")
def umpeg():
    if "user" in session:
        return render_template("umpeg.html")
    else:
        return redirect(url_for('index'))

@app.route("/pep")
def pep():
    if "user" in session:
        return render_template("pep.html")
    else:
        return redirect(url_for('index'))

@app.route("/keuangan")
def keuangan():
    if "user" in session:
        return render_template("keuangan.html")
    else:
        return redirect(url_for('index'))

@app.route("/bidangppe")
def bidangppe():
    if "user" in session:
        return render_template("bidangppe.html")
    else:
        return redirect(url_for('index'))

@app.route("/subidppe1")
def subidppe1():
    if "user" in session:
        return render_template("subidppe1.html")
    else:
        return redirect(url_for('index'))

@app.route("/subidppe2")
def subidppe2():
    if "user" in session:
        return render_template("subidppe2.html")
    else:
        return redirect(url_for('index'))

@app.route("/bidangppm")
def bidangppm():
    if "user" in session:
        return render_template("bidangppm.html")
    else:
        return redirect(url_for('index'))

@app.route("/subidppm1")
def subidppm1():
    if "user" in session:
        return render_template("subidppm1.html")
    else:
        return redirect(url_for('index'))

@app.route("/subidppm2")
def subidppm2():
    if "user" in session:
        return render_template("subidppm2.html")
    else:
        return redirect(url_for('index'))

@app.route("/bidangpik")
def bidangpik():
    if "user" in session:
        return render_template("bidangpik.html")
    else:
        return redirect(url_for('index'))

@app.route("/subidpik1")
def subidpik1():
    if "user" in session:
        return render_template("subidpik1.html")
    else:
        return redirect(url_for('index'))

@app.route("/subidpik2")
def subidpik2():
    if "user" in session:
        return render_template("subidpik2.html")
    else:
        return redirect(url_for('index'))

@app.route("/bidanglitbang")
def bidanglitbang():
    if "user" in session:
        return render_template("bidanglitbang.html")
    else:
        return redirect(url_for('index'))

@app.route("/subidlitbang1")
def subidlitbang1():
    if "user" in session:
        return render_template("subidlitbang1.html")
    else:
        return redirect(url_for('index'))

@app.route("/subidlitbang2")
def subidlitbang2():
    if "user" in session:
        return render_template("subidlitbang2.html")
    else:
        return redirect(url_for('index'))

@app.route("/fungsional")
def fungsional():
    if "user" in session:
        return render_template("fungsional.html")
    else:
        return redirect(url_for('index'))

@app.route("/thl")
def thl():
    if "user" in session:
        return render_template("thl.html")
    else:
        return redirect(url_for('index'))

@app.route("/satpam")
def satpam():
    if "user" in session:
        return render_template("satpam.html")
    else:
        return redirect(url_for('index'))

@app.route("/ob")
def ob():
    if "user" in session:
        return render_template("ob.html")
    else:
        return redirect(url_for('index'))

@app.route("/sopir")
def sopir():
    if "user" in session:
        return render_template("sopir.html")
    else:
        return redirect(url_for('index'))

@app.route("/keterangan")
def keterangan():
    if "user" in session:
        return render_template("keterangan.html")
    else:
        return redirect(url_for('index'))

@app.route("/logout")
def logout():
    if "user" in session:
        session.pop("user")
        session.pop("password")
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route("/redirect-sekretariat")
def redirect_sekretariat():
    return redirect(url_for("sekretariat"))

@app.route("/redirect-umpeg")
def redirect_umpeg():
    return redirect(url_for("umpeg"))

@app.route("/redirect-pep")
def redirect_pep():
    return redirect(url_for("pep"))

@app.route("/redirect-keuangan")
def redirect_keuangan():
    return redirect(url_for("keuangan"))

@app.route("/redirect-bidangppe")
def redirect_bidangppe():
    return redirect(url_for("bidangppe"))

@app.route("/redirect-subidppe1")
def redirect_subidppe1():
    return redirect(url_for("subidppe1"))

@app.route("/redirect-subidppe2")
def redirect_subidppe2():
    return redirect(url_for("subidppe2"))

@app.route("/redirect-bidangppm")
def redirect_bidangppm():
    return redirect(url_for("bidangppm"))

@app.route("/redirect-subidppm1")
def redirect_subidppm1():
    return redirect(url_for("subidppm1"))

@app.route("/redirect-subidppm2")
def redirect_subidppm2():
    return redirect(url_for("subidppm2"))

@app.route("/redirect-bidangpik")
def redirect_bidangpik():
    return redirect(url_for("bidangpik"))

@app.route("/redirect-subidpik1")
def redirect_subidpik1():
    return redirect(url_for("subidpik1"))

@app.route("/redirect-subidpik2")
def redirect_subidpik2():
    return redirect(url_for("subidpik2"))

@app.route("/redirect-bidanglitbang")
def redirect_bidanglitbang():
    return redirect(url_for("bidanglitbang"))

@app.route("/redirect-subidlitbang1")
def redirect_subidlitbang1():
    return redirect(url_for("subidlitbang1"))

@app.route("/redirect-subidlitbang2")
def redirect_subidlitbang2():
    return redirect(url_for("subidlitbang2"))

@app.route("/redirect-fungsional")
def redirect_fungsional():
    return redirect(url_for("fungsional"))

@app.route("/redirect-thl")
def redirect_thl():
    return redirect(url_for("thl"))

@app.route("/redirect-satpam")
def redirect_satpam():
    return redirect(url_for("satpam"))

@app.route("/redirect-ob")
def redirect_ob():
    return redirect(url_for("ob"))

@app.route("/redirect-sopir")
def redirect_sopir():
    return redirect(url_for("sopir"))

@app.route("/redirect-keterangan")
def redirect_keterangan():
    return redirect(url_for("keterangan"))

if __name__ == "__main__":
    app.run(debug=True)
