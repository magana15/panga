from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    feedbacks = db.relationship('Feedback', backref='user', lazy=True)
    orders = db.relationship('Order', backref='user', lazy=True)

class Uniform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(120), nullable=False)
    color_code = db.Column(db.String(7), nullable=False)  # Hex color code
    size = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)
    in_stock = db.Column(db.Boolean, default=True)

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
