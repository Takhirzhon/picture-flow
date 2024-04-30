class User:
    def __init__(self, user_id: int, username: str, email: str, password: str):
        self.id = user_id
        self.username = username
        self.email = email
        self.password = password

    def update_email(self, new_email: str):
        self.email = new_email

    def update_password(self, new_password: str):
        self.password = new_password

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }
