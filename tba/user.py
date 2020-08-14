users = {}


def generate_user_id():
    try:
        user_id = 1 + max(users)
    except ValueError:
        user_id = 1
    return user_id


class User(object):

    def __init__(self, user_id: int, user_name: str):
        self.user_id = user_id
        self.user_name = user_name


def register_user(user_name: str) -> int:
    user_id = generate_user_id()
    participant = User(user_id=user_id, user_name=user_name)
    users[user_id] = participant
    return user_id


def get_user(user_id):
    return users[user_id]
