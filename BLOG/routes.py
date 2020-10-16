from flask  import render_template, flash, redirect, url_for
from BLOG import app
from BLOG.forms import RegisterForm, LoginForm

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
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'{form.username.data} account created', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='REGISTER', form=form)


@app.route('/login',  methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'{form.username.data} account created', 'success')
        return redirect(url_for('index'))
    return render_template('login.html', title='LOGIN', form=form)