# class Book:
#     def __init__(self, title, pages):
#         self.title = title
#         self._pages = pages
#
#     @property
#     def pages(self):
#         return self._pages
#
#     @pages.setter
#     def pages(self, new_pages):
#         if new_pages > 0:
#             self._pages = new_pages
#         else:
#             print("Xato: sahifalar soni musbat bo‘lishi kerak.")
#     @pages.deleter
#     def pages(self):
#         self._pages = 0
#
#
#     @property
#     def reading_time(self):
#         return self._pages * 2
#
#     def __str__(self):
#         return f"Kitob {self.title} {self._pages} sahifa "
#
# book = Book("Python", 300)
# book.pages = 350
# print(book.pages)
# book.pages = -20
# print(book.reading_time)
# print(book.__str__())
a = {"key": "value"}
print(a["sd"])