__author__="trunglv"

from flask import Flask

app = Flask(__name__) # '__main__'

@app.route('/') # www.mysite.com/api/..
def hello_method():
    return "Hello, TrungLv!"

if __name__=='__main__':
    app.run()