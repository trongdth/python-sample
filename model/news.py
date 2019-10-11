class News(object):
    author = ''
    title = ''

    def __init__(self, author, title):
        self.author = author
        self.title = title

    @classmethod
    def news_from_dict(cls, dict):
        return News(
            author=dict['author'],
            title=dict['title'],
        )

    def to_string(self):
        return 'Author: {}, Title: {}'.format(self.author.encode('utf-8') if self.author is not None else '', self.title.encode('utf-8') if self.title is not None else '')
