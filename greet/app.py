from flask import Flask, request 

@app.route('/welcome')
def welcome():
    return "Welcome!"

@app.route('/welcome/home')
def welcome_home():
    return "Welcome home!"

@app.route('/welcome/back')
def welcome_back():
    return "Welcome back!"