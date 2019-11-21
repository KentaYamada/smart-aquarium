from backend.controller import auth


def get_blueprints():
    """
        Get all blueprint modules
    """
    return [
        auth.bp
    ]
