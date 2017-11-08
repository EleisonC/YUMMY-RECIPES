import os
from flask import *
from app.user import User
from functools import wraps

app = Flask(__name__)
app.secret_key='chris1234kaluleu'
users = {}

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
        passwordcm = request.form['passwordo']
        if username in users.keys():
            error = 'username already exists'
        else:   
            if username and password and password==passwordcm:
                usr = User(username,password)
                users[usr.username] = usr
                return redirect(url_for('login',message='You have succesfully registered'))
    return render_template('signup.html', error=error)


@app.route('/<username>', methods=['GET', 'POST'])
@is_logged_in
def user(username):
    usr = users[username]
    food = usr.categories
    return render_template("user.html", food = food, username=usr.username)

@app.route('/<username>/add_category',methods=['GET','POST'])
@is_logged_in
def add_category(username):
    user = users[username]
    if request.method == "POST":
        name = request.form['category']
        if name:
            usr = users[session['username']]
            usr.create_categories(name)
            return redirect(url_for('user',username=user.username))
    return render_template('add_cat.html',username=user.username)

@app.route('/<name>/add_recipe', methods=['GET', 'POST'])
@is_logged_in
def add_food_recipe(name):
    usr = users[session['username']]
    if request.method == "POST":
        rname = request.form['name']
        instructions = request.form['instructions']
        if name and rname and instructions:
            usr.create_food_recipe(name,rname,instructions)
            return redirect(url_for('category',name=name,username=usr.username))
    return render_template('add_item.html', name=name,username=usr.username)

@app.route('/category/<name>')
@is_logged_in
def category(name):
    usr = users[session['username']]
    foods = usr.categories[name]
    return render_template('categories.html', foods=foods, name=name)



@app.route('/steps/<name>')
@is_logged_in
def steps(name):
    usr = users[session['username']]
    instructions = usr.view(name)
    return render_template('recipe.html', instructions=instructions, name=name,username=usr.username)

@app.route('/<name>/update/<oname>', methods=['GET', 'POST'])
@is_logged_in
def update(name,oname):
    usr = users[session['username']]
    if request.method == "POST":
        new_name = request.form['name']
        new_steps = request.form['instructions']
        if name and new_name and new_steps:
            usr.create_food_recipe(name,new_name,new_steps)
            usr.categories[name].remove(oname)
            return redirect(url_for('category', name=name,username=usr.username))
        
    
    return render_template('update.html', name=oname, cat_name=name)

@app.route('/update_category/<name>', methods=['GET','POST'])
@is_logged_in
def update_category(name):
    if request.method == "POST":
        new_name = request.form['catname']
        if new_name:
            usr = users[session['username']]
            usr.create_categories(new_name)
            usr.categories[new_name] = usr.categories[name]
            usr.delete_category(name)
            return redirect(url_for('user',username=usr.username))
    return render_template('updatecategory.html', name=name)

@app.route('/<name>/delete/<dname>')
@is_logged_in
def remove(name,dname):
    usr = users[session['username']]
    usr.categories[name].remove(dname)
    return redirect(url_for('user', username=usr.username))

@app.route('/delete_category/<name>')
@is_logged_in
def delete_category(name):
    usr = users[session['username']]
    usr.delete_category(name)
    return redirect(url_for('user', username=usr.username))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None 
    if request.method == 'POST':
        if request.form['username'] not in users.keys():
            error = 'Invalid username'
        username = request.form['username']
        verify = users.get(username, False)
        if request.form['password'] not in verify.password:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            session['username'] = request.form['username']
            flash('You were logged in')
            return redirect(url_for('user', username = username))
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