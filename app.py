from flask import Flask, request, jsonify, redirect

from db.database_service import UserManager
from flask_cors import CORS


app = Flask(__name__)
user_manager = UserManager()
cors = CORS(app, resources={r"/user": {"origins": "https://yourjobfinder.website"}})

@app.route('/user', methods=['POST'])
def add_user():
    data = request.json
    email = data.get('email')
    position = data.get('position')
    location = data.get('location')
    job_type = data.get('jobType')
    try:
        if email is None or position is None or location is None or job_type is None:
            return jsonify({"message": "Invalid request"}), 400
        user_manager.add_user(email, position, location, job_type)
        return jsonify({"message": "User added successfully!"}), 201
    except Exception as e:
        redirect('https://yourjobfinder.website/unsubscribeError')



@app.route('/user', methods=['DELETE'])
def delete_user():
    data = request.json
    email = data.get('email')
    position = data.get('position')
    location = data.get('location')
    try:
        if email is None or position is None or location is None:
            raise Exception
        user_manager.delete_user(email, position, location)
        return redirect('https://yourjobfinder.website/unsubscribe')
    except Exception:
        redirect('https://yourjobfinder.website/unsubscribeError')


if __name__ == '__main__':
    app.run(threaded=True, port=5000)