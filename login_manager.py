from flask_login import UserMixin

class User(UserMixin):
    """
    User model for Flask-Login integration.
    In a real app, this would map to a DB table.
    """
    def __init__(self, id, username, role):
        self.id = id
        self.username = username
        self.role = role

class LoginService:
    """
    Service to handle user authentication logic.
    """
    
    @staticmethod
    def verify_user(username, password):
        # In production, verify against hashed passwords in DB
        # Demo logic:
        if username == "admin" and password == "admin":
            return User(id=1, username="admin", role="admin")
        return None

    @staticmethod
    def get_user_by_id(user_id):
        # Mock user retrieval
        if user_id == 1:
            return User(id=1, username="admin", role="admin")
        return None
