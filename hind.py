from flask import Flask, request, render_template
from wtforms import  StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from flask_wtf import FlaskForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
# app.config['WTF_CSRF_ENABLED'] = True  # 移除这一行，重新启用CSRF保护
class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            print(f"Login attempt: {form.username.data}")
            # 这里可以添加实际的登录逻辑，比如检查数据库
            return 'Login successful!'
        else:
            print("Login errors")
            return render_template('login.html', form=form)
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'GET':
        return render_template('register.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            print(form.username.data)
            print(form.password.data)
            print(form.confirm_password.data)
            return 'Registration successful!'
        else:
            print("password errors")
            return render_template('register.html', form=form)
if __name__ == '__main__':
    app.run(debug=True)
