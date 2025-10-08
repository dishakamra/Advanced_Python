class User:
    def __init__(self, username):
        self.username = username

    @classmethod
    def from_email(cls, email):
        name = email.split('@')[0]
        return cls(name)
    
    @staticmethod
    def is_valid_email(email):
        return '@' in email
    
print(User.is_valid_email("disha@example.com"))