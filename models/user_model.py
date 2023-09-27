class User:
    def __init__(self, data):
        self.id = data.get('id', None)
        self.title = data.get('title', None)
        self.firstName = data.get('firstName', None)
        self.lastName = data.get('lastName', None)
        self.picture = data.get('picture', None)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'picture': self.picture,
        }
