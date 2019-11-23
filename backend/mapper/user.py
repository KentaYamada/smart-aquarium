from backend.model.user import User


class UserMapper:
    @classmethod
    def find_users(cls):
        # todo: convert list of object to list of dictinaries
        users = (
            {
                'id': 1,
                'name': 'Taro',
                'email': 'taro@email.com',
                'password': 'taro'
            },
            {
                'id': 2,
                'name': 'Jiro',
                'email': 'jiro@email.com',
                'password': 'jiro'
            },
            {
                'id': 3,
                'name': 'Saburo',
                'email': 'sabuaro@email.com',
                'password': 'saburo'
            }
        )
        return users

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
