from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    feedbacks = db.relationship('Feedback', backref='user', lazy=True)
    orders = db.relationship('Order', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Uniform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(100), nullable=False)
    size = db.Column(db.String(50), nullable=False)
    color_code = db.Column(db.String(7), nullable=False)
    price = db.Column(db.Float, nullable=False)
    photo_url = db.Column(db.String(200), nullable=True)

    def __init__(self, school_name, size, color_code, price, photo_url):
        self.school_name = school_name
        self.size = size
        self.color_code = color_code
        self.price = price
        self.photo_url = photo_url

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text, nullable=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    uniform_id = db.Column(db.Integer, db.ForeignKey('uniform.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='Pending')


class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    uniform_id = db.Column(db.Integer, db.ForeignKey('uniform.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    uniform = db.relationship('Uniform', backref='cart_items')
