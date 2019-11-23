class User:
    def __init__(self, id, name, email, password, **kwargs):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def verify_password(self, request_password):
        return True
