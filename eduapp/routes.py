from flask import render_template, request

from models import Customer

def register_routes(app, db):

    @app.route('/')
    def index():
        people = Customer.query.all()
        return str(people)
