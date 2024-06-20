from flask import render_template, request, redirect, url_for
from app import app
from models import User

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        user = User(name=name, email=email)
        user.save()
        return redirect(url_for('index'))
    return render_template('add_user.html')

@app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        user.save()
        return redirect(url_for('index'))
    return render_template('edit_user.html', user=user)

@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    user = User.query.get(user_id)
    user.delete()
    return redirect(url_for('index')) 
