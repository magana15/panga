from app import app, db
from app.models import User, Uniform, Feedback, Order, CartItem


app.app_context().push()

db.create_all()
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Uniform': Uniform, 'Feedback': Feedback, 'Order': Order,'CartItem': CartItem}

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port = 5001, debug=True)
