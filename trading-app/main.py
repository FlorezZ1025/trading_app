from flask import send_from_directory
from app import app

@app.route('/')
def login():
    return send_from_directory('templates', 'login.html')

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