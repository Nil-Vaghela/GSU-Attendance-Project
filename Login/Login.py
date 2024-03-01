from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, UserMixin




class Login(UserMixin):
    id = "admin"
    password = "32156"
    
    def user_login():
        if request.method == 'POST':
            UserName = request.form["username"]
            Password = request.form['password']

            if UserName == "admin" and Password == "32156":
                login_user(user=Login(), duration=15)
                return 'working'
                
            else:
                return 'You have entered wrong ID or Password. Please click back and try again'
        return render_template('Login.html')
    
    def admin_login():
        if request.method == 'GET':
            UserName = request.form['username']
            Password = request.form['Password']

            if UserName == "admin" and Password == 'qwerty':
                print('Yes Working')
            else:
                print("Not working")
                