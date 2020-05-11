from app import app,db
from flask import render_template,url_for,redirect,flash,request
from app.forms import LoginForm,RegistrationForm,AddProductForm
from app.models import User,Product
from flask_login import current_user,login_user,logout_user
from werkzeug.utils import secure_filename
import os

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title='OSMS')

@app.route('/products')
def products():
    products = Product.query.all()
    return render_template("products.html",products=products,title='Products')

@app.route('/login',methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid emailid or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html',form=form,title='Sign In')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register',methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,username=form.username.data,name=form.name.data,country=form.country.data,address=form.address.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, You have registered')
        return redirect(url_for('login'))
    return render_template('register.html',form=form,title='Sign Up')

@app.route('/products/add',methods=['POST','GET'])
def add_products():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    form = AddProductForm()
    if form.validate_on_submit():
        f = form.image.data
        filename = secure_filename(f.filename)
        product = Product(name=form.name.data,category=form.category.data,price=form.price.data,description=form.description.data,image=filename,quantity=form.quantity.data)
        basedir = os.path.abspath(os.path.dirname(__file__))      
        f.save(os.path.join(basedir,'static',filename))
        db.session.add(product)
        db.session.commit()
        flash('Your product has been added')
        return redirect(url_for('products'))
    return render_template('addproduct.html',form=form,title='Add Product')
