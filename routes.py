from flask import Blueprint, render_template, request, jsonify
from .companion import generate_response

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    reply = generate_response(user_message)
    return jsonify({'reply': reply})
