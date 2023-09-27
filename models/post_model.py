class Post:
    def __init__(self, data):
        self.id = data.get('id', None)
        self.image = data.get('image', None)
        self.likes = data.get('likes', None)
        self.tags = data.get('tags', None)
        self.text = data.get('text', None)
        self.publishDate = data.get('publishDate', None)
        self.owner = data.get('owner', None)

    def to_dict(self):
        return {
            'id': self.id,
            'image': self.image,
            'likes': self.likes,
            'tags': self.tags,
            'text': self.text,
            'publishDate': self.publishDate,
            'owner': self.owner,
        }
