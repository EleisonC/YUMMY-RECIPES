import os
from flask import *
from app.user import User
from functools import wraps

app = Flask(__name__)
app.secret_key='chris1234kaluleu'
users = {'a': 'a', 'a1': 'a1'}
man= User()

def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorised, Please Log In')
            return redirect(url_for('login'))

    return wrap

@app.route('/signup', methods=['GET', 'POST'])
def register():
    """ Route to the signup page - that displays the registration page """
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password:
            users[username] =password
            return redirect(url_for('login'))
    return render_template('signup.html', error=error)

@app.route('/user', methods=['GET', 'POST'])
@is_logged_in
def user():
    food = man.food_recipe
    return render_template("user.html", food = food)

@app.route('/add_recipe', methods=['GET', 'POST'])
@is_logged_in
def add_food_recipe():
    if request.method == "POST":
        name = request.form['name']
        instructions = request.form['instructions']
        if name and instructions:
            man.create_food_recipe(name,instructions)
            return redirect(url_for('user'))
    return render_template('add_item.html')



@app.route('/steps/<name>')
@is_logged_in
def steps(name):
    instructions = man.view(name)
    return render_template('recipe.html', instructions=instructions, name=name)

@app.route('/update/<name>', methods=['GET', 'POST'])
@is_logged_in
def update(name):
    if request.method == "POST":
        new_name = request.form['name']
        new_steps = request.form['instructions']
        if new_name and new_steps:
            man.delete(name)
            man.create_food_recipe(new_name,new_steps)
            return redirect(url_for('user'))
        
    
    return render_template('update.html', name=name)

@app.route('/delete/<name>')
@is_logged_in
def remove(name):
    man.delete(name)
    return redirect(url_for('user'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None 
    if request.method == 'POST':
        if request.form['username'] not in users.keys():
            error = 'Invalid username'
        elif request.form['password'] not in users.values():
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('user'))
    return render_template('login.html', error=error)
@app.route('/logout')
@is_logged_in
def logout():
    """ Logout kills current running session """
    session.pop('logged_in', None)
    flash('You Were Logged Out !')
    return redirect(url_for('login'))


if __name__ == "__main__" :
    app.run(debug = True) 