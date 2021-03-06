from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate


db_name = 'bookshelf'
db_path = 'postgresql://{}:{}@{}/{}'.format(
    'postgres', 'password', 'localhost:5432', db_name
)

db = SQLAlchemy()
migrate = Migrate()

# ----------------------------------------------------------------------------#
# setup_db: binds a flask app and a SQLAlchemy service
# ----------------------------------------------------------------------------#

def setup_db(app, database_path=db_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    # db.create_all()
    migrate.init_app(app, db)

# ----------------------------------------------------------------------------#
# Book model
# ----------------------------------------------------------------------------#

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    author = db.Column(db.String(), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'rating': self.rating,
        }
        
