from flask import Blueprint,jsonify,make_response,request
from flask_restx import Api,Resource,fields
from flask_jwt_extended import jwt_required,get_jwt_identity
from ..models.books import Book
from ..models.users import User 



book_bp=Blueprint('books',__name__)


api=Api(book_bp)

book_model=api.model('Book',{
    'id':fields.Integer(),
    'title':fields.String(),
    'author':fields.String(),
    'isbn':fields.String(),
})


@api.route('/all')
class BookResource(Resource):

    @api.marshal_list_with(book_model,envelope='books')
    @jwt_required()
    def get(self,*args,**kwargs):

        '''
            Get all books, please get an access token 
        '''
        books=Book.query.all()

        return books

    @jwt_required()
    @api.marshal_with(book_model,envelope='book',code=201)
    def post(self,*args,**kwargs):
        data=request.get_json()


        current_user=get_jwt_identity()

        user_obj=User.query.filter_by(username=current_user).first()

        title=data.get('title')
        isbn=data.get('isbn')
        author=data.get('author')

        book_to_be_created=Book(title=title,author=author,isbn=isbn,added_by=user_obj)

        book_to_be_created.save()


        return book_to_be_created,201

        



@api.route('/<int:id>')
class Book(Resource):
    @api.marshal_with(book_model,'user')
    def get(self,id,*args,**kwargs):
        book=Book.query.get_by_id(id)

        return book
