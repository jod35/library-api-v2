from flask import Blueprint,jsonify
from flask_restx import Api,Resource,fields


book_bp=Blueprint('books',__name__)

api=Api(book_bp)


@api.route('/')
class HelloBooks(Resource):
    def get(self):
        return jsonify({"message":"Welcome to the book endpoint"})