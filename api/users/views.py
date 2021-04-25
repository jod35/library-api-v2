from flask import Blueprint,jsonify,request,make_response,abort,Response
from ..models.users import User
from flask_restx import Api, Resource,fields


user_bp=Blueprint('users',__name__)



api=Api(user_bp)

user_model=api.model(

    'User',
    {
        'username':fields.String(),
        'email':fields.String(),
        'password':fields.String()
    }
)




@api.route('/')
class Hello(Resource):
    def get(self):
        return jsonify({"message":"Welcome to the users endpoint"})

@api.route('/all')
class UserResources(Resource):
    @api.marshal_list_with(user_model,envelope='users')
    def get(self,*args,**kwargs):
        users=User.query.all()
        return users

    @api.marshal_with(user_model,envelope='user',code=201)
    def post(self,*args,**kwargs):
        data=request.get_json()

     
        try:
            new_user=User(
                username=data.get('username'),
                email=data.get('email'),
            )

            new_user.create_password_hash(data.get('password'))

            new_user.save()


            return new_user,201

        except:
            return jsonify({"message":"An error occured"})
        

@api.route('/<int:id>')
class UserResource(Resource):
    @api.marshal_with(user_model,envelope="user")
    def get(self,id,*args,**kwargs):
        user=User.get_by_id(id)

        return user


    @api.marshal_with(user_model,envelope='user')
    def delete(self,id,*args,**kwargs):
        user=User.get_by_id(id)

        user.delete()

        return user



