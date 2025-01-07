from flask import Flask, request, jsonify

from db.user_manager import UserManager

app = Flask(__name__)
user_manager = UserManager()


@app.route('/user', methods=['POST'])
def add_user():
    data = request.json
    print(data)
    email = data.get('email')
    position = data.get('position')
    location = data.get('location')
    job_type = data.get('job_type')
    if email is None or position is None or location is None or job_type is None:
        return jsonify({"message": "Invalid request"}), 400
    user_manager.add_user(email, position, location, job_type)
    return jsonify({"message": "User added successfully!"}), 201


@app.route('/user', methods=['DELETE'])
def delete_user():
    data = request.json
    email = data.get('email')
    position = data.get('position')
    location = data.get('location')
    if email is None or position is None or location is None:
        return jsonify({"message": "Invalid request"}), 400
    user_manager.delete_user(email, position, location)
    return jsonify({"message": "User deleted successfully!"}), 200


if __name__ == '__main__':
    app.run()
