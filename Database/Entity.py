class Entity():
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def get_title(self):
        return self.name

    def get_content(self):
        return self.content

    def set_title(self, name):
        self.name = name

    def set_content(self, content):
        self.content = content