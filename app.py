
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__, template_folder='./pages/templates')
app.secret_key = "mahnoor"
app.permanent_session_lifetime = timedelta(minutes=120)
access = True

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST": 
        session.permanent = True
        user = request.form['Userfield']
        session['user'] = user
        return redirect(url_for('home'))
    else:
        if "user" in session:
            return redirect(url_for("home"))
        else:
            return render_template('login.html')

@app.route('/logout/')
def logout():
    session.pop("user", None)
    flash("You have been logged out!", "info")
    return(redirect(url_for("login")))

@app.route('/home/')
def home():
    if "user" in session:
        user = session['user']
        return render_template('home.html', user_name=user)
    else:
        return redirect(url_for("login"))

@app.route('/user/')
def user():
    if "user" in session:
        user = session['user']
        return render_template('user.html', user_name=user)

@app.route('/admin/')
def admin():
    if access==True:
        return f"Welcome admin!"
    else:
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)