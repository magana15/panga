from app import db


class Customer(db.Model):

    __tablename__ = 'customers'

    customer_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'Person with name {self.username} and phone  {self.phone}'

class Order(db.Model):
    __tablename__ = 'orders'

    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=False)
    customer = db.relationship('Customers', backref=db.backref('orders', lazy=True))

class Uniform(db.Model):
     __tablename__ = 'uniform'

     item_id = db.Column(db.Integer, primary_key=True)
     item_name = db.Column(db.String, nullable=False)

class Shops(db.Model):
    __tablename__ = 'shops'


    shop_id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(100), nullable=False)

class Schools(db.Model):
    __tablename__ = 'schools'

    school_id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(100), nullable=False)

