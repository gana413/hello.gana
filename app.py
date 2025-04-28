from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/hello')
def api_hello():
    return "Hi!"

if __name__ == '_main_':
    app.run(debug=True)