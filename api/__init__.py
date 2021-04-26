from flask import Flask
from .config import DevConfig
from .utils.database import db
from .models.users import User
from .models.books import Book
from .utils.database import db
from .users.views import user_bp
from .books.views import book_bp
from .auth.login import auth_bp
from flask_jwt_extended import JWTManager




def create_app():
    app=Flask(__name__)


    app.config.from_object(DevConfig)

    db.init_app(app)

    jwt=JWTManager(app)

    app.register_blueprint(user_bp,url_prefix='/users')
    app.register_blueprint(book_bp,url_prefix='/books')
    app.register_blueprint(auth_bp,url_prefix='/auth')


    @app.shell_context_processor
    def make_shell_context():
        return {
            'db':db,
            'app':app,
            'User':User,
            'Book':Book
        }
    return app