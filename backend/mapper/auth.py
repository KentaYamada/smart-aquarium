class AuthMapper:
    @classmethod
    def dispose_token(cls, token):
        if not token:
            raise ValueError('Token is empty')
        return True
