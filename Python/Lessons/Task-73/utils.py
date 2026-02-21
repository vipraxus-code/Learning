from pathlib import Path
from json import dumps, loads


class UserData:
    def __init__(self, userid, username, favorite_number):
        self.userid = userid
        self.path = Path(__file__).parent / "Users" / f"User{self.userid}"
        self.username = username
        self.favorite_number = favorite_number
    
    def dump_data(self):
        data = {
            "user_id": self.userid,
            "username": self.username,
            "favorite_number": self.favorite_number,
        }        
        self.path.write_text(dumps(data), encoding="utf-8")
        return "Data saved."
    
    def load_data(self):
        try:
            return loads(self.path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            return "There is no such file."

    def greet(self):
        return f"Hello, {self.username}!"