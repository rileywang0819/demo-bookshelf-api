import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy  # , or_
from flask_cors import CORS
import random

from models import setup_db, Book

BOOKS_PER_SHELF = 8


def paginate_books(request, books):
    """ Paginate the books. """
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * BOOKS_PER_SHELF
    end = start + BOOKS_PER_SHELF
    formatted_books = [book.format() for book in books]
    current_books = formatted_books[start: end]

    return current_books


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    setup_db(app)
    # resources={...}
    # 1st element: specify what resources we're talking about
    # 2nd element: specify what origins from the client can access those resources
    # cors = CORS(app, resources={r"*/api/*": {"origins": "*"}})
    CORS(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true'
        )
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PUT,POST,DELETE,OPTIONS'
        )
        return response

    @app.route('/books', methods=['GET'])
    def get_books():
        """ Retrieves all books, paginated. """
        books = Book.query.order_by(Book.id).all()
        current_books = paginate_books(request, books)

        if len(current_books) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'books': current_books,
            'total_books': len(books)
        })

    @app.route('/books/<int:book_id>', methods=['PATCH'])
    def update_rating(book_id):
        """ Update a specific book's rating. """
        try:
            book = Book.query.filter_by(id=book_id).one_or_none()

            if book is None:
                abort(404)
            new_rating = request.get_json().get('rating')
            book.rating = new_rating
            book.update()

            return jsonify({
                'success': True,
                'id': book.id
            })
        except:
            abort(400)  # bad request

    @app.route('/books/<int:book_id>', methods=['DELETE'])
    def delete_book(book_id):
        """ Deletes a specific book. """
        try:
            book = Book.query.filter_by(id=book_id).one_or_none()

            if book is None:
                abort(404)

            book.delete()
            books = Book.query.order_by(Book.id).all()
            current_books = paginate_books(request, books)

            return jsonify({
                'success': True,
                'deleted': book_id,
                'books': current_books,
                'total_books': len(books)
            })
        except:
            abort(422)  # unprocessable entity

    @app.route('/books', methods=['POST'])
    def create_book():
        body = request.get_json()
        new_title = body.get('title', None)
        new_author = body.get('author', None)
        new_rating = body.get('rating', None)
        try:
            book = Book(title=new_title, author=new_author, rating=new_rating)
            book.insert()
            books = Book.query.order_by(Book.id).all()
            current_books = paginate_books(request, books)

            return jsonify({
                'success': True,
                'created': book.id,
                'books': current_books,
                'total_books': len(books)
            })
        except:
            abort(422)
        
    return app
