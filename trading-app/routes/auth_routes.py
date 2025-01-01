from flask import Blueprint, request, jsonify
from utils.db import db
from models.user import User
import bcrypt


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json

    name = data.get('name') 
    email = data.get('email') 
    password = data.get('password')

    if not name or not password:
        return jsonify({'msg': 'Username and password are required'}), 400
    
    if User.query.filter_by(email=email).first():
        return jsonify({'msg': 'User already exists'}), 400

    hashed_password = password.encode('utf-8')
    sal = bcrypt.gensalt()
    encripted = bcrypt.hashpw(hashed_password, sal).decode('utf-8')

    new_user = User(email=email, name=name, password=encripted)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email') 
    password = data.get('password')
    
    #No usada
    if not email or not password:
        return jsonify({'msg': 'Email and password are required'}), 400
    
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'msg': 'User not found'}), 401

    if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):     
        return jsonify({'msg': 'Invalid password'}), 401

    return jsonify({'msg': 'Login successful'}), 200