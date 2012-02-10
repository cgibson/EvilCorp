from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h2>Hello, World!</h2>\nI\'m running on Flask!'

if __name__ == '__main__':
    app.run()
