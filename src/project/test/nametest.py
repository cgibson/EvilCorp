from flask import Flask
from project.util import grammary
app = Flask(__name__)

@app.route('/')
def hello_world():
    lang = grammary.Language("static/lang/evillang.json")
    titlelang = grammary.Language("static/lang/eviltitlelang.json")
    return '<center><h2>%s</h2>\n%s</center>' % (lang.build(), titlelang.build())

if __name__ == '__main__':
    app.run()
