from backend.model.user import User


class AuthMapper:
    @classmethod
    def get_logged_in_user_token(cls, user_id):
        if user_id is None or not isinstance(user_id, int):
            raise ValueError('Invalid argument: user_id')
        return 'secret_token'

    @classmethod
    def generate_auth_token(cls, user):
        # if user is None or not isinstance(user, User):
        #     raise ValueError('Invalid argumant: user')
        return 'new_token'

    @classmethod
    def dispose_token(cls, token):
        if not token:
            raise ValueError('token is empty')
        return True

    @classmethod
    def find_by_token(cls, token):
        return None
