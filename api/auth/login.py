from flask import request,Blueprint,make_response,jsonify
from flask_jwt_extended import create_access_token
from ..models.users import User
from flask_restx import Api,Resource,Namespace


auth_ns=Namespace("auth","All auth operations")



@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.doc(params={'username':'A username','password':'An Password'})
    def post(self,*args, **kwargs):
        """
        Get to login and get access
        """
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


