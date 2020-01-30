from flask import Blueprint, jsonify, request, redirect
from app.models import db
from app.models.users import User


user_api = Blueprint('user', __name__)

@user_api.route('/api/users/ping', methods=['GET'])
def user_api_pong():
    return 'USER API PONG.'

@user_api.route('/api/users', methods=['GET'])
def get_all_users():
    return redirect("http://google.com", code=302)
