from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def home():
    try:
        response = requests.get('http://go-backend:8080/api')
        message = response.text
    except requests.exceptions.RequestException:
        message = "Could not connect to the Go backend."
    return render_template_string("<h1>{{ message }}</h1>", message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)