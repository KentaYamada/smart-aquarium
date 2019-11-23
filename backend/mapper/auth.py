class AuthMapper:
    @classmethod
    def get_logged_in_user_token(cls, user_id):
        return 'demo'

    @classmethod
    def generate_auth_token(cls, user):
        return 'demo'

    @classmethod
    def dispose_token(cls, token):
        return True

    @classmethod
    def find_by_token(cls, token):
        return 'demo'
