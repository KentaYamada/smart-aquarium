from backend.model.user import User


class UserMapper:
    @classmethod
    def find_user_by_email(cls, email):
        return User(1, 'test', 'example@email.com', 'test')
