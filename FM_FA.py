
from flask import Flask, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secretkey123"

users = {
    "admin": "password123"
}

@app.route('/')
def home():
    if "user" in session:
        return f"""
        <h2>Welcome {session['user']}</h2>
        <a href="/logout">Logout</a>
        """
    return redirect(url_for("login"))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('home'))
        else:
            return "<h3>Invalid credentials</h3>"

    return '''
        <h2>Login Page</h2>
        <form method="post">
            Username:<br>
            <input type="text" name="username"><br>
            Password:<br>
            <input type="password" name="password"><br><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run()
