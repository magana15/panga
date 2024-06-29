from flask import render_template, request, redirect, url_for
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



