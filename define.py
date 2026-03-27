from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    # Provide a list with at least two values to make template expression safe
    lis = {'list': [11,2,5,6,7]}
    return render_template('index2.html', lis=lis)
def kll(sift):
    return sift[::3]
app.add_template_filter(kll, 'sift')
if __name__ == '__main__':
    app.run(debug=True)