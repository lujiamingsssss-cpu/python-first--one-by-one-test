from flask import Flask, request, abort, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'luchao' and password == '888888':
           return '登录成功！'
        else:
           abort(404)
           return None
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)