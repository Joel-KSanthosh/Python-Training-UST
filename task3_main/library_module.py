class Book:
    def __init__(self,book_id : int,title : str,author : str):
        self.id = book_id
        self.title = title
        self.author = author

    def display_book_details(self) -> str:
        return f'Book id = {self.id}, Book title = {self.title}, Book author = {self.author}'


class Library:
    def __init__(self):
        self.books : dict[int : dict] = {}

    def add_book(self,book : Book):
        if book.id in self.books:
            return f'Book with ID {book.id} already exits!'
        else:
            self.books[book.id] = book
            return f"Book '{book.title}' added to library."

    def remove_book(self,book_id : int):
        try:
            removed_book : Book = self.books.pop(book_id)
            return f"Book '{removed_book.title}' removed from library."
        except KeyError:
            return f'Book with ID {book_id} does not exist!'

    def search_book(self,title : str):
        book_list = []
        for book in self.books.values():
            if title.lower() in book.title.lower():
                book_list.append(f"{book.id}. '{book.title}' by  {book.author}")
        if book_list:
            return '\n'.join(book_list)
        else:
            return "No match found!"

    def display_all_books(self):
        for book in self.books.values():
            yield f"{book.id}. '{book.title}' by  {book.author}"


class User:
    def __init__(self,user_id : int,name : str):
        self.id = user_id
        self.name = name

    def display_user_details(self):
        return f'User ID = {self.id}, Name = {self.name}'


class LibraryUser(User):
    def __init__(self, user_id: int, name: str):
        super().__init__(user_id, name)
        self.borrowed_list : dict = {}

    def borrow_book(self,library : Library,book_id : int):
        try:
            if book_id in self.borrowed_list:
                return "You have already borrowed book with ID = {}".format(book_id)
            elif book_id not in library.books:
                return f"Book with ID {book_id} does not exist in library!"
            else:
                borrowed_book = library.books.pop(book_id)
                self.borrowed_list[book_id] = borrowed_book
                return f"Book '{borrowed_book.title}' borrowed from library."
        except KeyError:
            return f"Failed to borrow book with ID = {book_id}"

    def return_book(self,library : Library,book_id : int):
        try:
            if book_id not in self.borrowed_list:
                return f'You have not borrowed the book with ID = {book_id}!'
            elif book_id in library.books:
                return f'You have not borrowed the book with ID = {book_id}!'
            else:
                returning_book = self.borrowed_list.pop(book_id)
                library.books[book_id] = returning_book
                return f"Book '{returning_book.title}' returned to library."
        except KeyError:
            return f'Failed to return book with ID = {book_id}'


# book = Book(1,"Harry Potter","J.K Rowling")
# print(book.display_book_details())
# library = Library()
# print(library.add_book(book))
# print(library.add_book(book))
# # print(library.remove_book(1))
# # print(library.remove_book(1))
# # print(library.search_book('har'))
# print(library.display_all_books())
# # print(user.display_user_details())
# lib = LibraryUser(1,"Joel")
# print(lib.borrow_book(library,1))
# print(lib.borrow_book(library,1))
#
