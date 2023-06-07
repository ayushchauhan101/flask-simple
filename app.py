from flask import Flask

app = Flask(__name__)

# base page


@app.route('/')
def index():
    return '<h1>Index Page</h1>'

# domain/hello


@app.route('/hello')
def hello():
    return 'Hello, World'

# domain/username/<your input here>


@app.route('/username/<userName>')
def user(userName):
    return f"Hello, user: {userName}"


# domain/user/<your integer input here>
@app.route('/user/<int:userID>')
def userId(userID):
    return f"Welcome, userId: {userID}"

if __name__ == "__main__":
    app.run(debug=True)
