class UserNotFound(Exception):
    def __init__(self, User_id):
        super().__init__(f"User with {User_id} is not Found")