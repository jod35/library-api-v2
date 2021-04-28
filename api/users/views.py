from flask import Blueprint,jsonify,request,make_response,abort,Response
from ..models.users import User
from flask_restx import Api, Resource,fields,Namespace



user_namespace=Namespace('users',description='User related operations')

user_model=user_namespace.model(

    'User',
    {
        'username':fields.String(),
        'email':fields.String(),
        'password':fields.String()
    }
)






@user_namespace.route('/users')
class UserResources(Resource):
    @user_namespace.marshal_list_with(user_model,envelope='users')
    def get(self,*args,**kwargs):
        """
        Get all users
        """
        users=User.query.all()
        return users

    @user_namespace.marshal_with(user_model,envelope='user',code=201)
    def post(self,*args,**kwargs):

        """
            Create a new user
        """
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
        

@user_namespace.route('/user/<int:id>')
class UserResource(Resource):
    def get(self,id,*args,**kwargs):
        """
        Get a single user
        """
        user=User.get_by_id(id)

        return user


    @user_namespace.marshal_with(user_model,envelope='user')
    def delete(self,id,*args,**kwargs):
        """
            Delete a user
        """
        user=User.get_by_id(id)

        user.delete()

        return user



