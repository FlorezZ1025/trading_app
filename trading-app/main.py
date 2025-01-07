from flask import jsonify, redirect, render_template, send_from_directory, url_for
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, set_access_cookies, unset_jwt_cookies
import jwt
from app import app, jwt
from models.user import User


@app.route('/')
def login():

    return send_from_directory('templates', 'login.html')

@app.route('/index')
@jwt_required()
def index():
    email_user = get_jwt_identity()

    user = User.query.filter_by(email=email_user).first()

    return render_template('index.html', current_user=user)

@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return redirect('/')

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    response = jsonify({'msg': 'Token has expired'})
    response.delete_cookie('access_token')
    return redirect('/')

@app.route('/register')
def register():
    return send_from_directory('templates', 'register.html') 

@app.route('/<path:filename>')
def custom_templates(filename):
    return send_from_directory('templates', filename)


@app.route('/assets/<path:filename>')
def custom_assets(filename):
    return send_from_directory('assets', filename)



if __name__ == '__main__':
    app.run(debug=True)