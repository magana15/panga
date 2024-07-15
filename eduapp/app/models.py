from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), default='user')
    feedbacks = db.relationship('Feedback', backref='user', lazy=True)
    orders = db.relationship('Order', backref='user', lazy=True)
    is_active = db.Column(db.Boolean(), default=True)

    def __repr__(self):
        return f'<User: {self.username}, Role: {self.role}>'

    def get_id(self):
        return self.id




class Uniform(db.Model):
    __tablename__ = 'uniform'


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

    def __repr__(self):
        return f'<Uniform {self.id} - {self.school_name} ({self.color_code})>'

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
    uniform = db.relationship('Uniform', backref='orders')


class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    uniform_id = db.Column(db.Integer, db.ForeignKey('uniform.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    uniform = db.relationship('Uniform', backref='cart_items')



























