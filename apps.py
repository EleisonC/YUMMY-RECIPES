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

@app.route("/")
def start():
    return redirect(url_for("login"))

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
    food = man.categories
    return render_template("user.html", food = food)

@app.route('/add_category',methods=['GET','POST'])
@is_logged_in
def add_category():
    if request.method == "POST":
        name = request.form['category']
        if name:
            man.create_categories(name)
            return redirect(url_for('user'))
    return render_template('add_cat.html')

@app.route('/add_recipe', methods=['GET', 'POST'])
@is_logged_in
def add_food_recipe():
    if request.method == "POST":
        name = request.form['name']
        instructions = request.form['instructions']
        categorys = request.form['category']
        if categorys and name and instructions:
            man.create_food_recipe(categorys,name,instructions)
            return redirect(url_for('user'))
    return render_template('add_item.html')

@app.route('/category/<name>')
@is_logged_in
def category(name):
    
    foods = man.food_recipe
    
    return render_template('categories.html', foods=foods, name=name)



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
        category_nam = request.form['category']
        if category_nam and new_name and new_steps:
            man.delete(name)
            man.create_food_recipe(category_nam,new_name,new_steps)
            return redirect(url_for('user'))
        
    
    return render_template('update.html', name=name)
@app.route('/update_category/<name>', methods=['GET','POST'])
@is_logged_in
def update_category(name):
    if request.method == "POST":
        new_name = request.form['catname']
        if new_name:
            man.create_categories(new_name)
            man.categories[new_name] = man.categories[name]
            man.delete_category(name)
            return redirect(url_for('user'))
    else:
        return render_template('updatecategory.html', name=name)
@app.route('/delete/<name>')
@is_logged_in
def remove(name):
    man.delete(name)
    return redirect(url_for('user'))

@app.route('/delete_category/<name>')
@is_logged_in
def delete_category(name):
    man.delete_category(name)
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
