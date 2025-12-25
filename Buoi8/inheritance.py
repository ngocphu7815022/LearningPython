class Document:
    def __init__(self, title):
        self.title = title

    def show_info(self):
        return f"Tên tiêu đề: {self.title}"


class Article(Document):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def show_info(self):
        return f"Bài báo: {self.title} - Tác giả: {self.author}"


class Email(Document):
    def __init__(self, title, sender):
        super().__init__(title)
        self.sender = sender

    def show_info(self):
        return f"Email: {self.title} - Người gửi: {self.sender}"


obj_art = Article("Doc2", "Phu")
print(obj_art.show_info())

obj_email = Email("Email title", "John")
print(obj_email.show_info())
