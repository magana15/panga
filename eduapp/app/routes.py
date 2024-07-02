from flask import render_template, request, redirect, url_for,session,flash
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, login_manager
from app.models import User, Uniform, Feedback, Order, CartItem
from app.forms import LoginForm, RegistrationForm


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/catalog')
def catalog():
    uniforms = Uniform.query.all()
    return render_template('catalog.html', uniforms=uniforms)

@app.route('/size_guide')
def size_guide():
    return render_template('size_guide.html')

@app.route('/order', methods=['GET', 'POST'])
@login_required
def order():

    if request.method == 'POST':
        user_id = current_user.id
        cart_items = CartItem.query.filter_by(user_id=user_id).all()
        if not cart_items:
            flash('Your cart is empty.')
            return redirect(url_for('catalog'))

        for item in cart_items:
            order = Order(
                user_id=user_id,
                uniform_id=item.uniform_id,
                quantity=item.quantity,
                total_price=item.quantity * item.uniform.price,
            )
            db.session.add(order)
            db.session.delete(item)

        db.session.commit()
        flash('Order placed successfully.')
        return redirect(url_for('order'))
    orders = Order.query.filter_by(user_id=user_id).all()
    return render_template('order.html', orders=orders)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        # Process feedback
        pass
    return render_template('feedback.html')

@app.route('/color_verification')
def color_verification():
    return render_template('color_verification.html')

@app.route('/cart')
@login_required
def cart():

    user_id = current_user.id
    cart_items = CartItem.query.filter_by(user_id=user_id).all()
    return render_template('cart.html', cart_items=cart_items)

@app.route('/add_to_cart/<int:uniform_id>', methods=['POST'])
@login_required
def add_to_cart(uniform_id):

    user_id = current_user.id
    quantity = int(request.form.get('quantity', 1))
    cart_item = CartItem.query.filter_by(user_id=user_id, uniform_id=uniform_id).first()

    if cart_item:
        cart_item.quantity += int(quantity)
    else:
        uniform = Uniform.query.get(uniform_id)
        if not uniform:
            flash('Uniform not found.')
            return redirect(url_for('catalog'))
        cart_item = CartItem(user_id=user_id, uniform_id=uniform_id, quantity=int(quantity))
        db.session.add(cart_item)

    db.session.commit()
    flash('Item added to cart.')
    return redirect(url_for('catalog'))
@app.route('/add_sample_data')
def add_sample_data():
    uniforms = [
        Uniform(school_name='Kamae Primary', size='M', color_code='#FF5733', price=20.0, photo_url='kamae_primary.jpg'),
        Uniform(school_name='Kiwanja Secondary', size='L', color_code='#33FF57', price=25.0, photo_url='kiwanja_secondary.jpg'),
        Uniform(school_name='Soweto High', size='S', color_code='#3357FF', price=30.0, photo_url='soweto_high.jpg'),
        Uniform(school_name='Vintage Academy', size='XL', color_code='#FFFF33', price=35.0, photo_url='vintage_academy.jpg'),
        Uniform(school_name='Masaku Primary', size='M', color_code='#FF33FF', price=22.0, photo_url='masaku_primary.jpg'),
        Uniform(school_name='Kamae High', size='L', color_code='#33FFFF', price=28.0, photo_url='kamae_high.jpg'),
        Uniform(school_name='Kiwanja Primary', size='S', color_code='#FF3333', price=26.0, photo_url='kiwanja_primary.jpg'),
        Uniform(school_name='Soweto Primary', size='M', color_code='#33FF33', price=21.0, photo_url='soweto_primary.jpg'),
        Uniform(school_name='Vintage Secondary', size='L', color_code='#5733FF', price=32.0, photo_url='vintage_secondary.jpg'),
        Uniform(school_name='Masaku Secondary', size='XL', color_code='#FF5733', price=34.0, photo_url='masaku_secondary.jpg')
    ]
    users = [
            User(id=120, username='magana', email='magana@mail.com', pasword_hash='magana', role='customer')
        ]
    db.session.add_all(uniforms)
    db.session.commit()
    return "Sample data added!"
