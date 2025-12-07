from flask import Flask, jsonify, request, render_template
from flask_login import LoginManager, login_required, login_user, logout_user
from database import db
from message_queue import MessageQueue
from login_manager import LoginService
import config

app = Flask(__name__)
app.config.from_object(config)

# Initialize extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
mq = MessageQueue(app.config['CLOUDAMQP_URL'])

@login_manager.user_loader
def load_user(user_id):
    return LoginService.get_user_by_id(int(user_id))

# --- Routes ---

@app.route('/')
def index():
    return "Energy Management Dashboard API is running."

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = LoginService.verify_user(data.get('username'), data.get('password'))
    if user:
        login_user(user)
        return jsonify({"status": "success", "message": "Logged in"})
    return jsonify({"status": "error", "message": "Invalid credentials"}), 401

@app.route('/api/trigger-crawler', methods=['POST'])
@login_required
def trigger_crawler():
    """
    Endpoint to manually trigger the crawling task via MQ.
    Shows integration between Web and Worker layers.
    """
    target_id = request.json.get('target_id')
    if not target_id:
        return jsonify({"error": "Missing target_id"}), 400

    # Send task to RabbitMQ
    message = f'{{"task": "crawl", "target": "{target_id}"}}'
    success = mq.publish_task('crawler_tasks', message)
    
    if success:
        return jsonify({"status": "queued", "target": target_id})
    else:
        return jsonify({"status": "error", "message": "MQ unavailable"}), 500

if __name__ == '__main__':
    app.run(debug=True)
