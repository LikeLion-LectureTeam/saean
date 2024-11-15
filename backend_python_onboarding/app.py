from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

users = []

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():

    username = request.form.get('username')
    password = request.form.get('password')
    password_confirm = request.form.get('password_confirm')
    name = request.form.get('name')
    birth_date = request.form.get('birth_date')
    email = request.form.get('email')

    if not username or not password or not password_confirm or not name or not birth_date or not email:
        return jsonify({'error': '모든 필드를 채워주세요!'}), 400
    if password != password_confirm:
        return jsonify({'error': '비밀번호가 일치하지 않습니다.'}), 400
    if len(birth_date) != 6:
        return jsonify({'error': '생년월일은 6자리여야 합니다.'}), 400

    user = {
        'username': username,
        'password': password,
        'name': name,
        'birth_date': birth_date,
        'email': email
    }
    users.append(user)

    return jsonify({'message': f'{name} 님 가입을 환영합니다!', 'users': users}), 200

if __name__ == '__main__':
    app.run(debug=True)
