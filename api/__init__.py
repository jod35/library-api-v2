from flask import Flask
from .config import DevConfig
from .utils.database import db
from .models.users import User
from .models.books import Book
from .utils.database import db
from .users.views import user_bp
from .books.views import book_bp




def create_app():
    app=Flask(__name__)


    app.config.from_object(DevConfig)

    db.init_app(app)

    app.register_blueprint(user_bp,url_prefix='/users')
    app.register_blueprint(book_bp,url_prefix='/books')


    @app.shell_context_processor
    def make_shell_context():
        return {
            'db':db,
            'app':app,
            'User':User,
            'Book':Book
        }
    return app