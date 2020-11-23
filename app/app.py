from flask import Flask
from flask import request
from flask import render_template
from weather import weather_at_server, weather_at_client

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html", message=weather_at_server())
    
@app.route('/server')
def client():
    #return "Hello!"
    #return weather()
    ip_address = request.headers['X-Forwarded-For'].split(',')[1]
    
    return render_template("index.html", message=weather_at_client(ip_address))
    
@app.route('/bye')
def bye():
    return "Good bye"


@app.route('/ask')
def ask():
    return "How are you doing?"


if __name__ == '__main__':
    # debug=True, means we can allow it to debug any errors.
    app.run(debug=True)