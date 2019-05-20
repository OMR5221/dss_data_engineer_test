from flask.cli import FlaskGroup
from task1 import create_app, db
from task1.models import KeyMetrics


app = create_app()
cli = FlaskGroup(create_app=create_app)


if __name__ == '__main__':
    cli()
