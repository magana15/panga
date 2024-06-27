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
        # Process order
        pass
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
