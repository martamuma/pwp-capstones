class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print('The user\'mail has been update, the new mail is {}.'.format(self.email))

    def __repr__(self):
        return 'User {}, email: {}, books read: {}'.format(self.name, self.email, len(self.books))

    def __eq__(self, other_user):

        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        total = 0
        for rating in self.books.values():
            total += rating
        average = total / len(self.books.values())
        return average


class Book:
    def __init__(self, title, isbn, price):
        self.title = title
        self.isbn = isbn
        self.rating = []
        self.price = price

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print('The isbn has been chagend to {}'.format(self.isbn))

    def get_price(self):
        return self.price

    def add_rating(self, new_rating):
        if new_rating > 0 and new_rating < 5:
            self.rating.append(new_rating)
        else:
            print('Invalid Rating')

    def get_rating(self):
        print(self.rating)

    def __repr__(self):
        return "{}".format(self.title)

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def get_average_rating(self):
        total = 0
        for rate in self.rating:
            total += rate
        average = total / len(self.rating)
        return average

    def __hash__(self):
        return hash((self.title, self.isbn, self.price))


class Fiction(Book):
    def __init__(self, title, author, isbn, price):
        super().__init__(title, isbn, price)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{} by {}".format(self.title, self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn, price):
        super().__init__(title, isbn, price)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.subject

    def __repr__(self):
        return "{}, a {} manual on {}".format(self.title, self.level, self.subject)


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn, price):
        book = Book(title, isbn, price)
        return book

    def create_novel(self, title, author, isbn, price):
        fiction = Fiction(title, author, isbn, price)
        return fiction

    def create_non_fiction(self, title, subject, level, isbn, price):
        non_fiction = Non_Fiction(title, subject, level, isbn, price)
        return non_fiction

    def add_book_to_user(self, book, email, rating=None):

        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print('No user with email {}'.format(email))

    def add_user(self, name, email, books=None):
        user = User(name, email)
        self.users[email] = user
        if books is not None:
            for book in self.books.keys():
                user.add_book_to_user(book, email)

    def print_catalog(self):
        for books in self.books.keys():
            print(books)

    def print_users(self):
        for users in self.users.values():
            print(users)

    def most_read_book(self):
        most_read_value = 0
        most_read_book = None
        for books, values in self.books.items():
            if values > most_read_value:
                most_read_value = values
                most_read_book = books
        return most_read_book

    def highest_rated_book(self):
        highest_rated = 0
        high_rated_book = None
        for books in self.books.keys():
            if books.get_average_rating() > highest_rated:
                highest_rated = books.get_average_rating()
                high_rated_book = books
        return high_rated_book

    def most_positive_user(self):
        highest_average = 0
        positive_user = None
        for keys, values in self.users.items():
            if values.get_average_rating() > highest_average:
                highest_average = values.get_average_rating()
                positive_user = keys
        return positive_user

    def get_n_most_read_books(self, n):
        a = self.books.items()
        b = sorted(a, key=lambda x: x[1], reverse=True)
        limit = 0
        most_read = []
        for item in b:
            if limit < n:
                most_read.append(item)
                limit += 1
        return most_read







