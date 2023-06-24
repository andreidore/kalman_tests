class Profile:
    def __init__(self, name, velocity):
        self.name = name
        self.velocity = velocity


class Profile1(Profile):
    def __init__(self):
        super().__init__("Profile1", 10)
