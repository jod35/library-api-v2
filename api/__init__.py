from flask import Flask
from .config import DevConfig
from .utils.database import db
from .models.users import User
from .models.books import Book
from .utils.database import db
from .users.views import user_namespace
from .books.views import book_namespace
from .auth.login import auth_bp
from flask_jwt_extended import JWTManager
from flask_restx import Api
from flasgger import Swagger



def create_app():
    app=Flask(__name__)


    app.config.from_object(DevConfig)

    db.init_app(app)

    authorizations = {
    'Basic Auth': {
        'type': 'basic',
        'in': 'header',
        'name': 'Authorization'
    },
}

    api=Api(app,doc='/',authorizations=authorizations)

    api.add_namespace(user_namespace)
    api.add_namespace(book_namespace)
    jwt=JWTManager(app)

    swagger=Swagger(app)




    @app.shell_context_processor
    def make_shell_context():
        return {
            'db':db,
            'app':app,
            'User':User,
            'Book':Book
        }
    return app