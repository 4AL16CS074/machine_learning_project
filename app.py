from flask import Flask

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])

def index():
    return "I am very happy today because i deployed my first python flask application"


if __name__=="__main__":
    app.run(debug=True)