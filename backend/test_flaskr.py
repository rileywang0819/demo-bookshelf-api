import os
import json
import unittest
from flask_sqlalchemy import SQLAlchemy
from flaskr import create_app
from models import setup_db, Book


class BookshelfTestCase(unittest.TestCase):
    """ This class represents the bookshelf api test case. """

    def setUp(self):
        """ Define test variables and initialize app. """
        self.app = create_app()
        self.client = self.app.test_client
        self.db_name = 'bookshelf_test'
        self.db_path = 'postgresql://{}:{}@{}/{}'.format(
            'postgres', 'password', 'localhost:5432', self.db_name
        )
        setup_db(self.app, self.db_path)
        
        self.new_book = {
            'title': 'Anansi Boys',
            'author': 'Neil Gaiman',
            'rating': 5
        }
    
      
    def tearDown(self):
        """ Executes after each test. """
        pass
    
    '''
    def test_get_paginated_books(self):
        """ Test getting paginated books. """
        response = self.client().get('/books')
        # decode json into Python objects
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['books'])
        self.assertTrue(len(data['books']))
    
    
    def test_404_beyond_valid_page(self):
        """ Test sending request with invalid page. """  
        response = self.client().get('/books?page=1000')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Not found")
    
    
    def test_update_rating(self):
        """ Test updating book's rating. """
        response = self.client().patch('/books/1', json={'rating': 1})
        data = json.loads(response.data)
        book = Book.query.filter(Book.id==1).one_or_none()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(book.format()['rating'], 1)
    
    
    def test_400_failed_update(self):
        """ Test sending patch request without data. """
        response = self.client().patch('/books/2')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Bad Request")
        
        
    def test_delete_book(self):
        """ Test deleting a specific book. """   
        response = self.client().delete('/books/13')
        data = json.loads(response.data)
        book = Book.query.filter(Book.id==16).one_or_none()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['books'])
        self.assertTrue(len(data['books']))
        self.assertEqual(book, None)
    
       
    def test_422_delete_book_not_exist(self):
        response = self.client().delete('/books/16')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Unprocessable")
        
    
    def test_create_book(self):
        response = self.client().post('/books', json=self.new_book)
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['books']))
    
    
    def test_405_not_allow_creation(self):
        response = self.client().post('/books/20', json=self.new_book)
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Not Allowed Method")
    '''
    
    def test_get_book_with_search(self):
        response = self.client().post('books', json={'search': 'novel'})
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['totalBooks'])
        self.assertEqual(len(data['books']), 4)
        
    
    def test_cannot_get_book_with_seach(self):
        response = self.client().post('books', json={'search': 'abcdefg'})
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertFalse(data['totalBooks'])
        self.assertEqual(len(data['books']), 0)
        

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
        
