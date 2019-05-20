from sqlalchemy import exc
from flask import Blueprint, request, render_template
from flask_restful import Resource, Api

from . import db
from .models import KeyMetrics


keymetrics_blueprint = Blueprint('key_metrics', __name__, template_folder='./templates')
api = Api(keymetrics_blueprint)


@keymetrics_blueprint.route('/', methods=['GET'])
def index():
    key_metrics = KeyMetrics.query.all()
    return render_template('index.html', key_metrics=key_metrics)


class KeyMetricsTest(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'Key Metric Test!'
    }


class DailyKeyMetrics(Resource):
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
                        'key_metrics': [km.to_json() for km in KeyMetrics.query.filter_by(date=date).all()]
                    }
                }
                return response_object, 200
        except ValueError:
            return response_object, 404


class KeyMetricsList(Resource):
    def get(self):
        """Get all key metrics"""
        response_object = {
            'status': 'success',
            'data': {
                'key_metrics': [km.to_json() for km in KeyMetrics.query.all()]
            }
        }
        return response_object, 200

api.add_resource(KeyMetricsTest, '/key_metrics/test')
api.add_resource(DailyKeyMetrics, '/key_metrics/<date>')
api.add_resource(KeyMetricsList, '/key_metrics')
