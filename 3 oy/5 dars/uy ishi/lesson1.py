class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self._pages = pages  # protected, faqat getter orqali tekshiramiz

    def __str__(self):
        return f"Kitob: {self.title} | Muallif: {self.author} | {self.pages} bet"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if value <= 0:
            raise ValueError("Sahifalar soni musbat bo'lishi kerak.")
        self._pages = value

    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title and self.author == other.author

    def __hash__(self):
        return hash((self.title, self.author))

    def __del__(self):
        print("Kitob o‘chirildi")


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.borrowed_books = []

    def __str__(self):
        return f"Foydalanuvchi: {self.username} ({self.email})"

    def __eq__(self, other):
        return isinstance(other, User) and self.email == other.email

    def __hash__(self):
        return hash(self.email)

    def borrow(self, book):
        self.borrowed_books.append(book)

    def __len__(self):
        return len(self.borrowed_books)

    def __getitem__(self, index):
        return self.borrowed_books[index]


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                del book
                break

    def __contains__(self, title):
        for book in self.books:
            if book.title == title:
                return True
        return False

    def __getitem__(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise KeyError(f"{title} nomli kitob topilmadi.")

    def __bool__(self):
        return bool(self.books)

    @property
    def total_books(self):
        return len(self.books)

    @total_books.deleter
    def total_books(self):
        self.books.clear()
        self.users.clear()


lib = Library()
book = Book("Python", "Ali", 250)
user = User("ali", "ali@mail.com")

lib.add_book(book)
lib.add_user(user)
user.borrow(book)

print(user)
print(len(user))
print(user[0])
print("Python" in lib)
print(lib["Python"])
del book
