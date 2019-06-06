from sqlalchemy.sql import func
from task1 import db
from datetime import date, datetime
import datetime

class Products(db.Model):
    __tablename__ = 'task2_products'
    __table_args__ = {'useexisting': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, nullable=False)
    page_views = db.Column(db.Integer)
    visits = db.Column(db.Integer)
    unique_visitors = db.Column(db.Integer)
    bounce_rate = db.Column(db.Integer)

    def __init__(self, dt, pv, vs, uv, br):
        self.date = dt
        self.page_views = pv
        self.visits = vs
        self.unique_visitors = uv
        self.bounce_rate = br

    def to_json(self):
        return {
            'id': self.id,
            'date': self.date.strftime("%Y-%m-%d"),
            'page_views': self.page_views,
            'visits': self.visits,
            'unique_visitors': self.unique_visitors,
            'bounce_rate': self.bounce_rate
        }
