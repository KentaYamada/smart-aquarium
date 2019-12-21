from backend.model.user import User


class UserMapper:
    @classmethod
    def find_users(cls):
        return [
            User(1, 'Taro', 'taro@email.com', 'taro'),
            User(2, 'Jiro', 'jiro@email.com', 'jiro'),
            User(3, 'Saburo', 'sabuaro@email.com', 'saburo')
        ]

    @classmethod
    def find_user_by_email(cls, email):
        return User(1, 'test', 'example@email.com', 'test')

    @classmethod
    def save(cls, user):
        return True

    @classmethod
    def delete(cls, id):
        return True

    @classmethod
    def exist_user(cls, id):
        return True
