from flask_login import LoginManager
from Login.Login import Login
from flask import Flask,render_template,request

app = Flask(__name__)
app.secret_key = ['GsuAttendance']
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'Login'

@login_manager.user_loader
def load_user(user_id):
    if user_id == "admin":
        return Login()
    return None

@app.route('/',methods=['GET', 'POST'])
def LoginPage():
    UserLogin = Login.user_login() # User Login Function
    return UserLogin

if __name__ == '__main__':
    app.run(debug=True)