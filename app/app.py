from flask import Flask
from flask import render_template
from weather import weather

app = Flask(__name__)


@app.route('/')
def main():
    #return "Hello!"
    #return weather()
    return render_template("index.html", message=weather())


@app.route('/bye')
def bye():
    return "Good bye"


@app.route('/ask')
def ask():
    return "How are you doing?"


if __name__ == '__main__':
    # debug=True, means we can allow it to debug any errors.
    app.run(debug=True)