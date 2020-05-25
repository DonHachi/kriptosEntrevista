#functions and libraries
from flask import Flask,request,jsonify,render_template
from pymongo import MongoClient
from pprint import pprint
import mongodb

#config
app = Flask(__name__)


#app routes
@app.route('/')
def home():
    return render_template('insert.html')

@app.route('/insert',methods=['POST'])
def insertData():
    if request.method=='POST':
        data = {"Comment":request.form['comment']}
        mongodb.insertComment(data)
        return render_template('insert.html',success=True)

#error handlers
@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def terminalError(e):
    original = getattr(e,"original_exception",None)
    if original is None:
        return "this is a direct 500 error"
    return "Unhandled 500 error right now!"

if __name__ == '__main__':
    app.run(port=8000)