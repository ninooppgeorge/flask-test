from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/product")
def product():
    return render_template('product.html')


@app.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('static', path)