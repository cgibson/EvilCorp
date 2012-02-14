from flask import Flask
from flask import render_template, url_for
import random
from project.util import grammary

app = Flask(__name__)

@app.route('/')
def hello_world():
    lang = grammary.Language("static/lang/evillang.json")
    titlelang = grammary.Language("static/lang/eviltitlelang.json")
    
    evil_name = lang.build()
    evil_title = titlelang.build()
    style_file = url_for('static', filename='style.css')
    font_type = random.randint(1,6)
    
    return render_template('main.html', 
                           evil_name=evil_name, 
                           evil_title=evil_title, 
                           style_file=style_file,
                           font_type=font_type)

if __name__ == '__main__':
    app.run(debug=True)
