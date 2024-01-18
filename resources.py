from flask import request
from app import db, Resource
from models import Book

from schemas import BookSchema

book_schema = BookSchema()
books_schema = BookSchema(many=True)


# Resources
class NewBookReource(Resource):
    def post(self):
        book = book_schema.load(request.get_json())

        try:
            db.session.add(book)
            db.session.commit()

        except Exception as e:
            print(e)
            return {"message": "An error occurred while saving to the database"}, 500
    
        return {'message': 'Book added successfully'}, 201
    
class UpdateBookResource(Resource):
    def put(self, book_id: int):
        book = Book.query.get(book_id)

        if book:
            data = book_schema.load(request.get_json())

            book.title = data.title
            book.author = data.author
            book.publication_year = data.publication_year
            book.genre = data.genre
            
            db.session.add(book)
            db.session.commit()

            return {'message': 'Book updated successfully'}, 201
        
        else: 
            return {'message': 'Book not found'}, 404
        
        
class GetAllBooksResource(Resource):
    def get(self):
        books = Book.query.all()

        books_data = books_schema.dump(books)
        return {'message': books_data}
    
class GetBookResource(Resource):
    def get(self, book_id: int):
        book = Book.query.get(book_id)

        if book:
          return book_schema.dump(book)
        else:
            return {'message': 'Book not found'}, 404

class DeleteBooksResource(Resource):
    def delete(self, book_id: int):
        book = Book.query.get(book_id)

        if book: 
            db.session.delete(book)
            db.session.commit()
            return {'message': 'Book Deleted successfully'}
        
        else:
           return {'message': 'Book not found'}, 404
    
