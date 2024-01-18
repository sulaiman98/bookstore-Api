from app import ma
from models import Book

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        dump_only = ('id',)
        load_instance = True