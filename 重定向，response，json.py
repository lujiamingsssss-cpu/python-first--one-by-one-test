from flask import jsonify,Flask,redirect,url_for
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
@app.route('/')
def premise():
    return redirect(url_for('index'))
@app.route('/index')
def index():
    return jsonify({"message": "Hello, Worldddddddddd!"})
if __name__ == '__main__':
    app.run(debug=True)