from os import name
from flask import Flask, render_template, request
#import webbrowser
#from flask_bootstrap import Bootstrap

app = Flask(__name__)
#Bootstrap(app)


@app.route('/', methods=['GET'])
def hello_world():
    text = ' <p> Hello World! Welcome to Flask!!!</p>'
    return text


# @app.route('/<id>', methods=['GET'])
# def get_id(id):
#     return f"your input id is : {id} ",200


@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html',name='bayu')

@app.route('/books/<id>', methods=['GET'])
def books(id):
    book = {
        'title':'harry potter',
        'author':'JK Rowling'}
    return render_template('index.html',name='bayu', data=book, id=id)

@app.route('/handle_data', methods=['POST','GET'])
def handle_data():
    if request.method == 'POST':
        nama = request.form['nama']
        password = request.form['password']
        data = [nama, password]
        return render_template('isi_form.html', data=data)
    
    return render_template('form.html')

if __name__ == "__main__":
    #webbrowser.open_new('http://127.0.0.1:5000/')
    app.run(debug=True)