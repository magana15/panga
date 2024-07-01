from flask import render_template, request, redirect, url_for,session,flash
from app import app, db
from app.models import User, Uniform, Feedback, Order

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/catalog')
def catalog():
    uniforms = Uniform.query.all()
    return render_template('catalog.html', uniforms=uniforms)

@app.route('/size_guide')
def size_guide():
    return render_template('size_guide.html')

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        user_id = session.get('user_id')
        if not user_id:
            flash('Please log in to place an order.')
            return redirect(url_for('index'))

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
        return redirect(url_for('index'))
    
    return render_template('order.html')

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
def cart():
    user_id = session.get('user_id')
    if not user_id:
        flash('Please log in to view your cart.')
        return redirect(url_for('catalog'))

    cart_items = CartItem.query.filter_by(user_id=user_id).all()
    return render_template('cart.html', cart_items=cart_items)

@app.route('/add_to_cart/<int:uniform_id>', methods=['POST'])
def add_to_cart(uniform_id):
    user_id = session.get('user_id')
    if not user_id:
        flash('Please log in to add items to your cart.')
        return redirect(url_for('index'))

    quantity = request.form.get('quantity', 1)
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
    db.session.add_all(uniforms)
    db.session.commit()
    return "Sample data added!"
