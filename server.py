from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    return "Hello World!"

@app.route('/dojo')

def dojo():
    return "Dojo!"

@app.route('/say/<name>')

def say(name):
    return "Hi " + str(name)

@app.route('/repeat/<int:num>/<word>')

def repeat(num, word):
    newStr = ""
    for i in range(0, num):
        if(i == num - 1):
            newStr += str(word) 
        else:
            newStr += str(word) + ", "
    return newStr


if __name__ == "__main__":
    app.run(debug=True)