from flask  import render_template, flash, redirect, url_for
from BLOG import app, db
from BLOG.forms import RegisterForm, LoginForm
from BLOG.models import User, Post
from flask_login import login_user, current_user, logout_user

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', title='HOME')


@app.route('/about')
def about():
    return render_template('about.html', title='ABOUT')

@app.route('/blog')
def blog():
    return render_template('blog.html', title='BLOG')

@app.route('/innerblog')
def innerblog():
    return render_template('inner-blog.html', title='INNER-BLOG')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', title='GALLERY')

    
@app.route('/contact')
def contact():
    return render_template('contact.html', title='CONTACT')

@app.route('/register',  methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, name=form.name.data, surname=form.surname.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'{form.username.data} adli hesab yaradildi', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='REGISTER', form=form)


@app.route('/login',  methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('index'))

        else:
            flash(f'Düzgün daxil etməmisiniz', 'danger')
    return render_template('login.html', title='LOGIN', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
