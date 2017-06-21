
class Book(models.model):
    author = models.ForeignKey(Author)
    title = modles.TextField()
    blurb = models.TextField()

    @property
    def _cache_name(self):
        return 'json.books.{0}'.format(self.pk)

    def to_json(self):
        book_json = cache.get(self._cache_name)

        if book_json is None:
            book_json = {
                'author': self.author.name,
                'title': self.title,
                'blurb': self.blurb
            }
            cache.set(self._cache_name, book_json)

        return book_json