from backend.controller import auth
from backend.controller import user


def get_blueprints():
    """
        Get all blueprint modules
    """
    return [
        auth.bp,
        user.bp
    ]
