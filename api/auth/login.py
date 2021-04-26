from flask import request,Blueprint,make_response,jsonify
from flask_jwt_extended import create_access_token
from ..models.users import User


auth_bp=Blueprint('auth',__name__)

@auth_bp.route('/login',methods=["POST"])
def login():
    data=request.get_json()

    username=data.get('username')
    password=data.get('password')

    user=User.get_by_username(username)

    if user and user.check_password(password):
        token=create_access_token(identity=username)

        return make_response(
            jsonify(
                {
                    
                    "message":"Logged In",
                    "token":token
                
                }
            )
        )

    return jsonify({"Something Went wrong"})


