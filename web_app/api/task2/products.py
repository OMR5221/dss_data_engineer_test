from sqlalchemy import exc
from flask import Blueprint, request, render_template
from flask_restful import Resource, Api

from . import db
from .models import products


products_blueprint = Blueprint('products', __name__, template_folder='./templates')
api = Api(products_blueprint)


@products_blueprint.route('/', methods=['GET'])
def index():
    products = products.query.all()
    return render_template('index.html', products=products)


class productsTest(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'Key Metric Test!'
    }


class Dailyproducts(Resource):
    def get(self, date):
        """Get daily key metrics by date"""
        response_object = {
            'status': 'fail',
            'message': 'No Daily key Metrics'
        }
        try:
            if not daily_key_metric:
                return response_object, 404
            else:
                response_object = {
                    'status': 'success',
                    'data': {
                        'products': [km.to_json() for km in products.query.filter_by(date=date).all()]
                    }
                }
                return response_object, 200
        except ValueError:
            return response_object, 404


class productsList(Resource):
    def get(self):
        """Get all key metrics"""
        response_object = {
            'status': 'success',
            'data': {
                'products': [km.to_json() for km in products.query.all()]
            }
        }
        return response_object, 200

api.add_resource(productsTest, '/products/test')
api.add_resource(DailyProducts, '/products/<date>')
api.add_resource(productsList, '/products')
