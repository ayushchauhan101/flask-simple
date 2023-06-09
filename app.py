from flask import Flask, render_template, request

app = Flask(__name__)

all_users = {}

all_sports = {
    'basketball',
    'football',
    'tennis',
    'gymnastics'
}


@app.route('/')
def index():
    return render_template('index.html', sports=all_sports)


@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    if not name:
        return render_template('error.html')
    sport = request.form.get('sport')
    if sport not in all_sports:
        return render_template('error.html')
    all_users[name] = sport
    return render_template('success.html')


@app.route('/registrants')
def registrants():
    return render_template('registrants.html', registrants=all_users)
