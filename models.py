from app import db

# Define Models
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publication_year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(80), nullable=False)