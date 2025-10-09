import os
def get_user_name():
    return os.getenv("USER", "Guest")